---
title: "Fine-scale vessel extraction in fundus images by registration with fluorescein angiography."
collection: publications
date: 2019-01-01
venue: 'International Conference on Medical Image Computing and Computer-Assisted Intervention (MICCAI)'
excerpt: '**Kyoung Jin Noh**, Sang Jun Park, **Soochahn Lee**'
pdfurl: 'https://drive.google.com/file/d/1meVkyNyYhTCGwP8DnUo5VV_btDrbom7l/view'
htmlurl: 'https://link.springer.com/chapter/10.1007/978-3-030-32239-7_86'
thumbnail: '/images/publications/2019-01-01-fine-scale-vessel-extraction-in-fundus-i-fig2.png'
bibtex: |
    @inbook{Noh_2019, title={Fine-Scale Vessel Extraction in Fundus Images by Registration with Fluorescein Angiography}, ISBN={9783030322397}, ISSN={1611-3349}, url={http://dx.doi.org/10.1007/978-3-030-32239-7_86}, DOI={10.1007/978-3-030-32239-7_86}, booktitle={Medical Image Computing and Computer Assisted Intervention – MICCAI 2019}, publisher={Springer International Publishing}, author={Noh, Kyoung Jin and Park, Sang Jun and Lee, Soochahn}, year={2019}, pages={779–787} }
citation_mla: |
    Noh, Kyoung Jin, et al. “Fine-Scale Vessel Extraction in Fundus Images by Registration with Fluorescein Angiography.” Medical Image Computing and Computer Assisted Intervention – MICCAI 2019, 2019, pp. 779–87. Crossref, https://doi.org/10.1007/978-3-030-32239-7_86.
---

<!-- NOTE: Summary based on title only - verify and expand with actual abstract -->

**Authors:** **Kyoung Jin Noh**, Sang Jun Park, **Soochahn Lee**

> **TL;DR:** A method to extract fine-scale retinal vessels from fundus images by leveraging registration with fluorescein angiography, which reveals vessel details invisible in standard fundus photos.

---

## What this paper is about

![Figure description](/images/publications/2019-01-01-fine-scale-vessel-extraction-in-fundus-i-fig1.png)
*Qualitative comparison between (a) manual expert annotations of DRIVE [14] and (b) the results of the proposed method with minimal manual editing of minor errors. Our goal is to construct a foundational dataset for achieving superhuman accuracy in deep learning based retinal vessel segmentation.*

Standard color fundus images are the most common way to photograph the retina, but they miss many of the smaller, finer blood vessels. Fluorescein angiography (FA) lights up the vasculature with a contrast dye and captures much finer vessel detail, but it is invasive. The question is: can we transfer that fine vessel information from FA to improve vessel extraction in regular fundus images?

## Key idea

![Figure description](/images/publications/2019-01-01-fine-scale-vessel-extraction-in-fundus-i-fig2.png)
*The registration framework for a pair of FA frames.*

![Figure description](/images/publications/2019-01-01-fine-scale-vessel-extraction-in-fundus-i-fig3.png)
*The registration framework for the aggregated FA vessel mask and fundus image.*

The method registers fundus images with their corresponding fluorescein angiography counterparts, then uses the aligned FA-derived vessel maps as enhanced ground truth to train or guide vessel extraction on the fundus side. This cross-modal registration bridges the gap between what each imaging modality can reveal.

## Why it matters

![Figure description](/images/publications/2019-01-01-fine-scale-vessel-extraction-in-fundus-i-fig4.png)
*Qualitative results. Four sample cases are shown in 2 × 2 formation, with (top) the original image, (middle) the results of the proposed method, and (bottom) vessel segmentation results of the SSANet [11] trained on the public HRF [3] dataset. Left and right columns shows the images in full and zoomed resolution, respectively.*


Published at MICCAI 2019, this work enables higher-quality retinal vessel maps from non-invasive fundus photography, which is important for screening and diagnosis of diabetic retinopathy and other retinal diseases.

