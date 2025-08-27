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
- Inpainting
- Shadow Removal
- Reflection Removal

### Image Enhancement Tasks
- Low-Light Enhancement
- Color Enhancement
- Underwater Image Enhancement
- Multi-Exposure Fusion
- Depth-aware Image Enhancement
- Rendering

### Tone Mapping Tasks
- HDR Tone Mapping 

### Face and Portrait Restoration Tasks
- Old Photo Restoration
- Face Inpainting
- Face Super-Resolution 1000
- Face Editing
- Deepfake Generation

### Image Generation Tasks
- Style Transfer (I2I)
- Cartoonization
- Text-to-Image Synthesis
- Image Outpainting

### Compression Tasks
- Traditional Compression (JPEG, WebP, HEIC, etc.)
- Learned Image Compression

### Geometry-Aware Image Generation Tasks
- Novel View Synthesis
