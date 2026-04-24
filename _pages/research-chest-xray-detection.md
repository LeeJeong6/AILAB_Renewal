---
layout: single
title: "Mass and Abnormality Detection from Chest X-ray Images"
permalink: /research/chest-xray-detection/
author_profile: false
---

Chest X-rays are among the most widely used imaging modalities in clinical practice, yet detecting and localizing pathology is difficult without large, expertly annotated training sets. Our work targets this annotation bottleneck by using generative models — either to synthesize targeted abnormal cases or to learn what "normal" looks like — and then detecting abnormalities through comparison, enabling chest X-ray analysis with weaker or no lesion-level supervision.

## Research directions

- **Generative-comparison anomaly detection.** Train a model to reconstruct a healthy version of any input X-ray; the residual between the original and the reconstructed normal image yields a saliency map that localizes abnormalities without requiring bounding-box or pixel-level disease labels.
- **Disentangled targeted generation.** Disentangled contrastive learning with synthetic matching pairs separates disease-specific attributes from patient-specific anatomy, making it possible to generate controlled abnormal/normal image pairs for data augmentation and clinical education.

## Related publications

- [Abnormality Detection in Chest X-ray via Residual-Saliency from Normal Generation](/publications/2023-01-01-abnormality-detection-in-chest-x-ray-via/) — IEEE Access, 2023
- [Disentangled Contrastive Learning from Synthetic Matching Pairs for Targeted Chest X-ray Generation](/publications/2025-01-01-disentangled-contrastive-learning-from-s/) — IEEE Access, 2025
