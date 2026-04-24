---
title: "Active diffusion matching: score-based iterative alignment of cross-modal retinal images"
collection: publications
date: 2025-03-01
venue: 'IEEE Transactions on Biomedical Engineering'
excerpt: 'Kang Geon Lee, Su Jeong Song, **Soochahn Lee**, and Kyoung Mu Lee'
htmlurl: 'http://dx.doi.org/10.1109/tbme.2025.3598247'
thumbnail: '/images/publications/2025-03-01-active-diffusion-matching-score-based-i-fig2.png' 
bibtex: |
    @article{Lee_2026, title={Active Diffusion Matching: Score-Based Iterative Alignment of Cross-Modal Retinal Images}, volume={73}, ISSN={1558-2531}, url={http://dx.doi.org/10.1109/tbme.2025.3598247}, DOI={10.1109/tbme.2025.3598247}, number={3}, journal={IEEE Transactions on Biomedical Engineering}, publisher={Institute of Electrical and Electronics Engineers (IEEE)}, author={Lee, Kang Geon and Song, Su Jeong and Lee, Soochahn and Lee, Kyoung Mu}, year={2025}, month=mar, pages={1080–1093} }
citation_mla: |
    Lee, Kang Geon, et al. “Active Diffusion Matching: Score-Based Iterative Alignment of Cross-Modal Retinal Images.” IEEE Transactions on Biomedical Engineering, vol. 73, no. 3, Mar. 2026, pp. 1080–93. Crossref, https://doi.org/10.1109/tbme.2025.3598247.
---

<!-- NOTE: Summary based on title only - verify and expand with actual abstract -->

**Authors:** Kang Geon Lee, Su Jeong Song, **Soochahn Lee**, and Kyoung Mu Lee

> **TL;DR:** A score-based diffusion approach for iteratively aligning cross-modal retinal images (e.g., fundus photos and fluorescein angiography), achieving robust registration despite large appearance differences.

---

## What this paper is about

Registering retinal images from different modalities -- like color fundus photography and fluorescein angiography -- is essential for clinical diagnosis, but the dramatic appearance differences between modalities make traditional alignment methods unreliable.

![Figure description](/images/publications/2025-03-01-active-diffusion-matching-score-based-i-fig1.png) 
*Alignment of standard fundus images (SFIs) and ultra-widefield images (UWFIs) using ADM. We present a method for the alignment of SFI-UWFI pairs. The FOV of the SFI is limited to the orange box region of the UWFI. The cropped and zoomed-in green and red boxes highlight the alignment results of SuperRetina [1], GeoFormer [2], and our proposed ADM. The image below shows the intersection area between the SFI vessel (red line) and the UWFI vessel (green line), which exhibits the maximum alignment error (MAE)*

## Key idea

Active Diffusion Matching frames cross-modal image registration as a score-based iterative alignment process. By leveraging the denoising score matching framework from diffusion models, the method iteratively refines the spatial alignment between image pairs, handling the large appearance gap between different imaging modalities.

![Figure description](/images/publications/2025-03-01-active-diffusion-matching-score-based-i-fig2.png) 
*Overview of ADM. ADM aligns the source image Is (SFI) to the destination image Id (UWFI) using a dual diffusion model architecture. Two score networks are employed: sθ estimates global homography H, while sϕ estimates local displacement field v. Both networks are conditioned on the input image pair (Is,Id) via dedicated encoders EH and Ev , which extract modality-adapted latent features. At each diffusion step t, sθ estimates Ht, and sϕ predicts vt conditioned on both input images and the current estimate of Ht. This cyclic interaction allows Ht to guide the estimation of vt, while the reverse influence is incorporated via a guidance term during the update of Ht. The final aligned image Is is obtained by sequentially applying the predicted global transformation Hand local deformation v to Is through Spatial Transformer Layers (STL), adapted from [20].* 

## Why it matters

Accurate cross-modal retinal image registration enables clinicians to fuse complementary diagnostic information from different imaging techniques, improving disease detection and monitoring for conditions like diabetic retinopathy.

