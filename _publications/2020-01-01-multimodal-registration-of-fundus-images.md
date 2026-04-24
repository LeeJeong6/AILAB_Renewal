---
title: "Multimodal registration of fundus images with fluorescein angiography for fine-scale vessel segmentation."
collection: publications
date: 2020-01-01
venue: 'IEEE Access'
excerpt: '**Kyoung Jin Noh**, **Jooyoung Kim**, Sang Jun Park, **Soochahn Lee**'
htmlurl: 'https://ieeexplore.ieee.org/abstract/document/9050794'
thumbnail: '/images/publications/2020-01-01-multimodal-registration-of-fundus-images-fig1.png'
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

**This paper is an extension of the MICCAI 2019 paper "Fine-scale vessel extraction in fundus images by registration with fluorescein angiography."**


## Key idea

![Figure description](/images/publications/2020-01-01-multimodal-registration-of-fundus-images-fig1.png)
*Visual overview of the proposed framework.*

![Figure description](/images/publications/2020-01-01-multimodal-registration-of-fundus-images-fig2.png)
*Visual overview of the process for registration of a pair of FA frames. The process comprises (top) projective registration by keypoint matching, (bottom-left) vessel extraction using a CNN with transfer learning, and (bottom-middle) non-rigid registration using thin-plate spline deformation. This process is successively performed for all adjacent frame pairs with the initial frame as the anchor frame. This figure is best viewed in color, due to color tinting of the resulting checkerboard for improved delineation of overlaid frames.*

![Figure description](/images/publications/2020-01-01-multimodal-registration-of-fundus-images-fig3.png)
*The registration framework for the aggregated FA vessel mask and fundus image.*

The method develops a robust registration pipeline specifically designed to handle the large appearance gap between fundus and FA images. Once aligned, the high-detail vessel maps visible in FA can be projected onto the fundus coordinate space, providing fine-scale vessel segmentation ground truth that would be impossible to annotate manually.

## Why it matters

![Figure description](/images/publications/2020-01-01-multimodal-registration-of-fundus-images-fig4.png)
*Qualitative results. Four sample cases are depicted in a 2 × 2 formation, with (top) the original image, (middle) the results of the proposed method, and (bottom) vessel segmentation results of the SSANet [13] trained on the public HRF [8] dataset. Left and right columns illustrate the images in full and zoomed resolutions, respectively.*


This registration framework is a key building block for multimodal retinal analysis. By bridging fundus and FA data, it enables training better vessel segmentation models and supports richer clinical analysis of retinal vascular disease.

