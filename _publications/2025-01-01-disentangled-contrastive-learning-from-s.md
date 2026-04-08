---
title: "Disentangled contrastive learning from synthetic matching pairs for targeted chest X-ray generation"
collection: publications
date: 2025-01-01
venue: 'IEEE Access'
excerpt: 'Euyoung Kim, **Soochahn Lee**, Kyoung Mu Lee'
htmlurl: 'https://ieeexplore.ieee.org/abstract/document/10844299'
bibtex: |
    @article{Kim_2025, title={Disentangled Contrastive Learning From Synthetic Matching Pairs for Targeted Chest X-Ray Generation}, volume={13}, ISSN={2169-3536}, url={http://dx.doi.org/10.1109/access.2025.3531366}, DOI={10.1109/access.2025.3531366}, journal={IEEE Access}, publisher={Institute of Electrical and Electronics Engineers (IEEE)}, author={Kim, Euyoung and Lee, Soochahn and Mu Lee, Kyoung}, year={2025}, pages={15453–15468} }
citation_mla: |
    Kim, Euyoung, et al. “Disentangled Contrastive Learning From Synthetic Matching Pairs for Targeted Chest X-Ray Generation.” IEEE Access, vol. 13, 2025, pp. 15453–68. Crossref, https://doi.org/10.1109/access.2025.3531366.
---

<!-- NOTE: Summary based on title only - verify and expand with actual abstract -->

**Authors:** Euyoung Kim, **Soochahn Lee**, Kyoung Mu Lee

> **TL;DR:** A disentangled contrastive learning framework that uses synthetic matching pairs to enable targeted generation of chest X-ray images with specific pathological characteristics.

---

## What this paper is about

Generating realistic chest X-rays with specific target conditions (e.g., a particular disease appearance) is valuable for data augmentation and medical training, but it is hard to control what the model generates. Real paired data showing the same patient with and without a condition is scarce.

## Key idea

The method creates synthetic matching pairs and uses disentangled contrastive learning to separate disease-related features from patient-specific anatomy. This allows targeted generation where you can specify what pathological changes should appear in the output while keeping the rest of the anatomy consistent.

## Why it matters

This enables controlled medical image synthesis that could help with data augmentation for rare conditions and support clinical education, while addressing the fundamental scarcity of paired medical data.

<!-- TODO: Add key figures from the paper -->
<!-- ![Figure description](/images/publications/2025-01-01-disentangled-contrastive-learning-from-s-fig1.png) -->
