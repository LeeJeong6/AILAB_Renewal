---
layout: single
title: "The FIREFLY Dataset"
permalink: /research/firefly-dataset/
author_profile: false
---

**FIREFLY** (*Fundus Images REgistered with FLuorescein angiographY*) is a retinal imaging dataset that pairs color fundus photographs with their corresponding fluorescein angiography (FA) captures, along with fine-scale vessel segmentation masks and artery/vein classification labels. The dataset is built by registering FA sequences to their fundus counterparts, aggregating vascular detail across FA frames using CNN-based methods, producing artery/vein labels via graph-based neural networks, and validating the final annotations with clinicians and imaging technicians.

A synthetic counterpart, **FIREFLY-Gen**, extends the dataset by generating realistic retinal fundus images together with matching vessel masks using diffusion and GAN-based generative models — expanding data availability for training and evaluating vessel analysis methods.

**[Request access to the FIREFLY-Gen dataset →](/research/firefly-dataset/request/)**

## Why it matters

Standard fundus photography cannot reveal fine-scale vasculature, while FA does — at the cost of a contrast agent and a different appearance space. By registering the two modalities and distilling FA-level detail into fundus coordinates, FIREFLY enables supervision that was previously impossible: fundus-based models can now be trained and evaluated on vessel maps derived from FA-quality ground truth.

## Construction pipeline

1. **Cross-modal registration** between fundus and FA image pairs.
2. **Fine-scale vessel extraction** from FA frames and projection into fundus coordinates.
3. **Artery/vein classification** using hierarchical graph networks that leverage both modalities.
4. **Joint deep learning of fundus and FA** for improved A/V classification.
5. **Synthetic augmentation (FIREFLY-Gen)** using diffusion models to generate structurally realistic fundus images with paired vessel annotations.

## Related publications

- [Fine-Scale Vessel Extraction in Fundus Images by Registration with Fluorescein Angiography](/publications/2019-01-01-fine-scale-vessel-extraction-in-fundus-i/) — MICCAI, 2019
- [Multimodal Registration of Fundus Images with Fluorescein Angiography for Fine-Scale Vessel Segmentation](/publications/2020-01-01-multimodal-registration-of-fundus-images/) — IEEE Access, 2020
- [Combining Fundus Images and Fluorescein Angiography for Artery/Vein Classification Using the Hierarchical Vessel Graph Network](/publications/2020-01-01-combining-fundus-images-and-fluorescein/) — MICCAI, 2020
- [Combined Deep Learning of Fundus Images and Fluorescein Angiography for Retinal Artery/Vein Classification](/publications/2022-01-01-combined-deep-learning-of-fundus-images/) — IEEE Access, 2022
- [Generation of Structurally Realistic Retinal Fundus Images with Diffusion Models](/publications/2024-06-17-generation-of-structurally-realistic-ret/) — CVPRW, 2024

<!-- Legacy page reference: https://ailab.kookmin.ac.kr/firefly — port additional details, sample images, and download links when migrating. -->
