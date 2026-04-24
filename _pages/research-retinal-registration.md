---
layout: single
title: "Registration of Multimodal Retinal Images"
permalink: /research/retinal-registration/
author_profile: false
---

Aligning retinal images across modalities — color fundus, fluorescein angiography (FA), and ultra-widefield (UWF) fundus — is fundamental for transferring annotations, fusing diagnostic information, and reconstructing wide-field views from multiple captures. Each modality reveals different anatomical details under drastically different appearance statistics, making registration a challenging cross-modal correspondence problem.

## Research directions

- **Score-based and diffusion-driven alignment.** Casting cross-modal registration as an iterative refinement process guided by learned scores and random-walk correspondence search, robust to large appearance gaps and field-of-view differences.
- **Autoregressive transformation estimation.** Decomposing complex non-rigid deformations into a sequence of predicted transformation parameters, enabling accurate alignment of images with severe geometric variation.
- **Fundus–FA registration for fine-scale annotation transfer.** Aligning fundus and FA image pairs so that FA-derived vessel maps can serve as high-resolution supervision for fundus-based vessel analysis.
- **UWF enhancement and photomontage construction.** Improving UWF image quality with unpaired generative models, and stitching multiple fundus captures into coherent wide-field photomontages through learned registration and blending.

## Related publications

- [Fine-Scale Vessel Extraction in Fundus Images by Registration with Fluorescein Angiography](/publications/2019-01-01-fine-scale-vessel-extraction-in-fundus-i/) — MICCAI, 2019
- [Multimodal Registration of Fundus Images with Fluorescein Angiography for Fine-Scale Vessel Segmentation](/publications/2020-01-01-multimodal-registration-of-fundus-images/) — IEEE Access, 2020
- [Fully Leveraging Deep Learning Methods for Constructing Retinal Fundus Photomontages](/publications/2021-02-16-fully-leveraging-deep-learning-methods-f/) — Applied Sciences, 2021
- [FQ-UWF: Unpaired Generative Image Enhancement for Fundus Quality Ultra-Widefield Retinal Images](/publications/2024-06-04-fq-uwf-unpaired-generative-image-enhanc/) — Bioengineering, 2024
- [Active Diffusion Matching: Score-Based Iterative Alignment of Cross-Modal Retinal Images](/publications/2025-03-01-active-diffusion-matching-score-based-i/) — IEEE Transactions on Biomedical Engineering, 2025
- [Auto-Regressive Transformation for Image Alignment](/publications/2025-10-01-auto-regressive-transformation-for-image/) — ICCV, 2025
- [Particle Diffusion Matching: Random Walk Correspondence Search for the Alignment of Standard and Ultra-Widefield Fundus Images](/publications/2026-01-01-particle-diffusion-matching-random-walk/) — IEEE Transactions on Image Processing, 2026
