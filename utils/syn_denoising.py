import numpy as np
from PIL import Image
import cv2, io


def _srgb_to_linear(x):
    x = np.asarray(x, np.float32)
    a, thr = 0.055, 0.04045
    y = np.where(x <= thr, x/12.92, ((x + a)/(1 + a))**2.4)
    return np.clip(y, 0.0, 1.0)

def _linear_to_srgb(y):
    y = np.asarray(y, np.float32)
    a, thr = 0.055, 0.0031308
    x = np.where(y <= thr, y*12.92, (1 + a)*(y ** (1/2.4)) - a)
    return np.clip(x, 0.0, 1.0)

def _mosaic(rgb_lin, pattern="RGGB"):
    H, W, _ = rgb_lin.shape
    raw = np.zeros((H, W), np.float32)
    # 4 patterns
    if pattern == "RGGB":
        raw[0::2, 0::2] = rgb_lin[0::2, 0::2, 0]
        raw[0::2, 1::2] = rgb_lin[0::2, 1::2, 1]
        raw[1::2, 0::2] = rgb_lin[1::2, 0::2, 1]
        raw[1::2, 1::2] = rgb_lin[1::2, 1::2, 2]
    elif pattern == "BGGR":
        raw[0::2, 0::2] = rgb_lin[0::2, 0::2, 2]
        raw[0::2, 1::2] = rgb_lin[0::2, 1::2, 1]
        raw[1::2, 0::2] = rgb_lin[1::2, 0::2, 1]
        raw[1::2, 1::2] = rgb_lin[1::2, 1::2, 0]
    elif pattern == "GRBG":
        raw[0::2, 0::2] = rgb_lin[0::2, 0::2, 1]
        raw[0::2, 1::2] = rgb_lin[0::2, 1::2, 0]
        raw[1::2, 0::2] = rgb_lin[1::2, 0::2, 2]
        raw[1::2, 1::2] = rgb_lin[1::2, 1::2, 1]
    elif pattern == "GBRG":
        raw[0::2, 0::2] = rgb_lin[0::2, 0::2, 1]
        raw[0::2, 1::2] = rgb_lin[0::2, 1::2, 2]
        raw[1::2, 0::2] = rgb_lin[1::2, 0::2, 0]
        raw[1::2, 1::2] = rgb_lin[1::2, 1::2, 1]
    else:
        raise ValueError("Unknown Bayer pattern")
    return raw


_CV_CODES = {
    "RGGB": ["COLOR_BayerRG2BGR_EA", "COLOR_BayerRG2BGR_VNG", "COLOR_BayerRG2BGR"],
    "BGGR": ["COLOR_BayerBG2BGR_EA", "COLOR_BayerBG2BGR_VNG", "COLOR_BayerBG2BGR"],
    "GRBG": ["COLOR_BayerGR2BGR_EA", "COLOR_BayerGR2BGR_VNG", "COLOR_BayerGR2BGR"],
    "GBRG": ["COLOR_BayerGB2BGR_EA", "COLOR_BayerGB2BGR_VNG", "COLOR_BayerGB2BGR"],
}

def _demosaic_cv2(raw01, pattern):
    raw16 = np.clip(raw01 * 65535.0 + 0.5, 0, 65535).astype(np.uint16)
    code = None
    for name in _CV_CODES[pattern]:
        if hasattr(cv2, name):
            code = getattr(cv2, name)
            break
    if code is None: 
        code = getattr(cv2, _CV_CODES[pattern][-1])
    bgr = cv2.cvtColor(raw16, code).astype(np.float32) / 65535.0
    rgb = bgr[..., ::-1]
    return np.clip(rgb, 0.0, 1.0)

def _fit_color_matrix(src_lin, dst_lin, sample_px=200000, eps=1e-6):
    H, W, _ = src_lin.shape
    N = H * W
    if N > sample_px:
        idx = np.random.default_rng().choice(N, sample_px, replace=False)
        X = src_lin.reshape(-1, 3)[idx]
        Y = dst_lin.reshape(-1, 3)[idx]
    else:
        X = src_lin.reshape(-1, 3)
        Y = dst_lin.reshape(-1, 3)

    M, _, _, _ = np.linalg.lstsq(X + eps, Y, rcond=None)  # (3x3)
    return M

def _apply_matrix(img_lin, M):
    H, W, _ = img_lin.shape
    out = img_lin.reshape(-1,3) @ M
    return np.clip(out.reshape(H,W,3), 0.0, 1.0)

def _choose_pattern_and_matrix(L_ref):
    patterns = ["RGGB", "BGGR", "GRBG", "GBRG"]
    best = None
    for p in patterns:
        raw = _mosaic(L_ref, p)
        rec = _demosaic_cv2(raw, p)       
        M = _fit_color_matrix(rec, L_ref)         
        rec_corr = _apply_matrix(rec, M)
        err = np.mean((rec_corr - L_ref)**2)       
        if (best is None) or (err < best[2]):
            best = (p, M, err)
    return best  # (pattern, M, mse)

def synthesize_cbdnet_noise(input_path, output_path, seed=None, jpeg_prob=0.5):
    rng = np.random.default_rng(None if seed is None else int(seed))

    img = Image.open(input_path).convert("RGB")
    srgb = np.asarray(img, np.float32) / 255.0
    L_ref = _srgb_to_linear(srgb)

    pattern, color_M, _ = _choose_pattern_and_matrix(L_ref)

    raw_clean = _mosaic(L_ref, pattern)
    sigma_s = rng.uniform(0.0, 0.16)
    sigma_c = rng.uniform(0.0, 0.06)
    var_map = raw_clean * (sigma_s**2) + (sigma_c**2)
    noise = rng.normal(0.0, np.sqrt(var_map), size=raw_clean.shape).astype(np.float32)
    raw_noisy = np.clip(raw_clean + noise, 0.0, 1.0)

    L_noisy = _demosaic_cv2(raw_noisy, pattern)
    L_noisy = _apply_matrix(L_noisy, color_M)

    y = _linear_to_srgb(L_noisy)
    out = Image.fromarray((y*255.0 + 0.5).astype(np.uint8), "RGB")

    if rng.random() < jpeg_prob:
        Q = int(rng.integers(60, 101))
        buf = io.BytesIO()
        out.save(buf, format="JPEG", quality=Q, subsampling=0, optimize=True)
        buf.seek(0)
        out = Image.open(buf).convert("RGB")

    out.save(output_path)
