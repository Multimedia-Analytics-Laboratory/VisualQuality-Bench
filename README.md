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
        - SwinIR, HAT, SeeSR, PASD, OSEDiff,
- Denoising
    - Synthetic data construction
        - Camera perception: [Unprocessing pipeline](chrome-extension://efaidnbmnnnibpcajpcglclefindmkaj/https://openaccess.thecvf.com/content_CVPR_2019/papers/Brooks_Unprocessing_Images_for_Learned_Raw_Denoising_CVPR_2019_paper.pdf)
        - CBDNet degradation: [CBDNet](chrome-extension://efaidnbmnnnibpcajpcglclefindmkaj/https://openaccess.thecvf.com/content_CVPR_2019/papers/Guo_Toward_Convolutional_Blind_Denoising_of_Real_Photographs_CVPR_2019_paper.pdf) (the most common)<br>
            <img src="images/cbdnet.png" alt="Super-resolution example" width="250"/>
        - [Noise Flow](chrome-extension://efaidnbmnnnibpcajpcglclefindmkaj/https://openaccess.thecvf.com/content_ICCV_2019/papers/Abdelhamed_Noise_Flow_Noise_Modeling_With_Conditional_Normalizing_Flows_ICCV_2019_paper.pdf)
    - SOTA methods
        - CBDNet, 
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
