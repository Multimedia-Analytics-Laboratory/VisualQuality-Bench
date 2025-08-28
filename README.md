# VisualQuality-Bench

This repository records common image processing tasks with their synthetic data construction procedures.

## Image Processing Tasks

### Image Restoration Tasks
- Super-Resolution
    - Synthetic data construction
        - For non-generative methods: Bicubic downsampling (x2, x4)
        - For generative methods: RealESRGAN degradation [[RealESRGAN Paper](https://arxiv.org/abs/2107.10833)]<br>
            <img src="images/realesrgan.png" alt="Super-resolution example" width="500"/>
    - SOTA methods
        - SwinIR, HAT, DiffBIR, SeeSR, OSEDiff, HyperIR
- Denoising
    - Synthetic data construction
        - Camera perception: [[Unprocessing pipeline](https://arxiv.org/abs/1811.11127)]
        - CBDNet degradation: [[CBDNet](https://arxiv.org/abs/1807.04686)] (the most common)<br>
            <img src="images/cbdnet.png" alt="Super-resolution example" width="250"/>
    - SOTA methods
        - CBDNet, SwinIR, Restormer, X-Restormer, 
- Deblurring
    - Synthetic data construction
        - [[Levin Dataset Kernels](https://ieeexplore.ieee.org/document/5963691)]
        - Gaussian kernel + motion kernel + noise
    - SOTA methods
        - MAXIM, LaKDNet, EVSSM, 
- Deraining
    - Synthetic data construction
        - Rain streak, Raindrop, Rain and mist [[MPID Dataset](https://arxiv.org/abs/1903.08558)]
    - SOTA methods
        - DiffPlugin, Restormer, MPRNet,
- Desnowing
    - Synthetic data construction
        - Manual mask + random overlay + brightness change [[Snow100K](https://arxiv.org/abs/1708.04512)]
    - SOTA methods
        - DesnowNet,
- Dehazing
    - Synthetic data construction
        - Atmospheric Scattering Model [[RESIDE](https://arxiv.org/abs/1712.04143)]<br>
            <img src="images/RESIDE.png" alt="Super-resolution example" width="250"/>
    - SOTA methods
        - DehazeFormer (2023), RIDCP (2023),
- Natural Image Inpainting
    - Synthetic data construction
        - Free-form irregular masks and rectangular masks [[SN-PatchGAN](https://arxiv.org/abs/1806.03589)]
    - SOTA methods
        - SN-PatchGAN (2019),
- Shadow Removal
    - Synthetic data construction
        - [[SynShadow](https://arxiv.org/abs/2101.01713)]<br>
            <img src="images/SynShadow.png" alt="Super-resolution example" width="350"/>
    - SOTA methods
        - DHAN (2019), 
- Reflection Removal
    - Synthetic data construction
        - [[Zhang et al.](https://arxiv.org/abs/1806.05376)]<br>
            <img src="images/Reflection.png" alt="Super-resolution example" width="200"/>
    - SOTA methods
        - CEILNet (2017), Zhang et al. (2018), 
- Old Photo Restoration
    - Synthetic data construction
        - Unstructured Degradation (noise) + Structured Degradation (Scratches, holes/tears) [[Pipeline](https://arxiv.org/abs/2009.07047)]
    - SOTA methods
        - Wan et al. (2020), 
- Face Inpainting
    - Synthetic data construction
        - Free-form irregular masks and rectangular masks
    - SOTA methods
        - RePaint (2022), CodeFormer (2022),
- Face Super-Resolution
    - Synthetic data construction
        - GFPGAN degradation [[Pipeline](https://arxiv.org/abs/2101.04061)]
    - SOTA methods
        - GFPGAN (2021), CodeFormer (2022),

### Image Enhancement Tasks
- Low-Light Enhancement
    - Synthetic data construction
        - Reversed ISP + Exposure Degradation + Noise Degradation + White Balance & CCM + Tone Mapping + Forward ISP [[SynLLIE](https://ojs.aaai.org/index.php/AAAI/article/view/32617)]
    - SOTA methods
        - SNR-LLIE (2022), Retinexformer (2023), 
- Color Enhancement
    - Synthetic data construction
        - RAW to ISP, Changing EV [[Afifi et al.](https://arxiv.org/abs/2003.11596)]
    - SOTA methods
        - Afifi et al. (2021), 
- Underwater Image Enhancement
    - Synthetic data construction
        - [[Jaffe-McGlamery / Sea-thru](https://diglib.eg.org/items/e745bd5f-f8fd-48f0-b7e5-e447a4765bf3)]
        - WaterGAN (complicated)
    - SOTA methods
        - FUnIE-GAN (2020), 
- Multi-Exposure Fusion
    - Synthetic data construction
        - Inverse Gamma + Changing EV + CRF and noise
    - SOTA methods
        - U2Fusion (2020)

### Tone Mapping Tasks
- HDR Tone Mapping
    - Synthetic data construction
        - HDR datasets
    - SOTA methods
        - TMO algorithms

### Image Generation Tasks
- Style Transfer (I2I)
    - Content Image and Style Image
    - CycleGAN (2017)
- Cartoonization
    - Natural Image
    - White-box Cartoonization (2020),
- Text-to-Image Synthesis
    - GPT generation with attribution combinations
    - SD3.5 (2024), 
- Image Outpainting
    - Natural Image
    - QueryOTR (2022)

### Compression Tasks
- Image Compression
    - JPEG, WebP, HEIC, Learned algorithms

### Geometry-Aware Image Generation Tasks
- Novel View Synthesis


