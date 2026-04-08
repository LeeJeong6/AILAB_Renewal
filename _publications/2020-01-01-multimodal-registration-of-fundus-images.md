---
title: "Multimodal registration of fundus images with fluorescein angiography for fine-scale vessel segmentation."
collection: publications
date: 2020-01-01
venue: 'IEEE Access'
excerpt: '**Kyoung Jin Noh**, **Jooyoung Kim**, Sang Jun Park, **Soochahn Lee**'
htmlurl: 'https://ieeexplore.ieee.org/abstract/document/9050794'
bibtex: |
    @article{Noh_2020, title={Multimodal Registration of Fundus Images With Fluorescein Angiography for Fine-Scale Vessel Segmentation}, volume={8}, ISSN={2169-3536}, url={http://dx.doi.org/10.1109/access.2020.2984372}, DOI={10.1109/access.2020.2984372}, journal={IEEE Access}, publisher={Institute of Electrical and Electronics Engineers (IEEE)}, author={Noh, Kyoung Jin and Kim, Jooyoung and Park, Sang Jun and Lee, Soochahn}, year={2020}, pages={63757–63769} }
citation_mla: |
    Noh, Kyoung Jin, et al. “Multimodal Registration of Fundus Images With Fluorescein Angiography for Fine-Scale Vessel Segmentation.” IEEE Access, vol. 8, 2020, pp. 63757–69. Crossref, https://doi.org/10.1109/access.2020.2984372.
---

<!-- NOTE: Summary based on title only - verify and expand with actual abstract -->

**Authors:** **Kyoung Jin Noh**, **Jooyoung Kim**, Sang Jun Park, **Soochahn Lee**

> **TL;DR:** A multimodal registration method that aligns fundus photographs with fluorescein angiography images, enabling fine-scale vessel segmentation by transferring detailed vascular annotations across modalities.

---

## What this paper is about

Fundus photographs and fluorescein angiography (FA) capture the retina in fundamentally different ways -- one using reflected light and the other using fluorescent dye in the bloodstream. Aligning these two modalities is challenging due to differences in appearance, contrast, and geometric distortion, but doing so unlocks the ability to combine their complementary strengths.

## Key idea

The method develops a robust registration pipeline specifically designed to handle the large appearance gap between fundus and FA images. Once aligned, the high-detail vessel maps visible in FA can be projected onto the fundus coordinate space, providing fine-scale vessel segmentation ground truth that would be impossible to annotate manually.

## Why it matters

This registration framework is a key building block for multimodal retinal analysis. By bridging fundus and FA data, it enables training better vessel segmentation models and supports richer clinical analysis of retinal vascular disease.

<!-- TODO: Add key figures from the paper -->
<!-- ![Figure description](/images/publications/2020-01-01-multimodal-registration-of-fundus-images-fig1.png) -->
