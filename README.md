# VisualQuality-Bench

This repository records common image processing tasks with their synthetic data construction procedures.

## Image Processing Tasks

### Image Restoration Tasks
- Super-Resolution
    - Synthetic data construction
        - For non-generative methods: Bicubic downsampling (x2, x4)
        - For generative methods: RealESRGAN degradation [Paper](https://arxiv.org/abs/2107.10833)
        ![Alt text]("images/realesrgan.png")
    - SOTA methods
        - SwinIR, HAT, SeeSR, PASD, OSEDiff,
- Denoising
- Deblurring
- Deraining
- Desnowing
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
