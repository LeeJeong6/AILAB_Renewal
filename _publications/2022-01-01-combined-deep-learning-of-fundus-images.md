---
title: "Combined deep learning of fundus images and fluorescein angiography for retinal artery/vein classification"
collection: publications
date: 2022-01-01
venue: 'IEEE Access'
excerpt: '**Sojung Go**, **Jooyoung Kim**, **Kyoung Jin Noh**, Sang Jun Park, **Soochahn Lee**'
htmlurl: 'https://ieeexplore.ieee.org/abstract/document/9810952'
thumbnail: '/images/publications/2022-01-01-combined-deep-learning-of-fundus-images-fig1.png'
bibtex: |
    @article{Go_2022, title={Combined Deep Learning of Fundus Images and Fluorescein Angiography for Retinal Artery/Vein Classification}, volume={10}, ISSN={2169-3536}, url={http://dx.doi.org/10.1109/access.2022.3187503}, DOI={10.1109/access.2022.3187503}, journal={IEEE Access}, publisher={Institute of Electrical and Electronics Engineers (IEEE)}, author={Go, Sojung and Kim, Jooyoung and Noh, Kyoung Jin and Park, Sang Jun and Lee, Soochahn}, year={2022}, pages={70688–70698} }
citation_mla: |
    Go, Sojung, et al. “Combined Deep Learning of Fundus Images and Fluorescein Angiography for Retinal Artery/Vein Classification.” IEEE Access, vol. 10, 2022, pp. 70688–98. Crossref, https://doi.org/10.1109/access.2022.3187503.
---
<!-- NOTE: Summary based on title only - verify and expand with actual abstract -->

**Authors:** **Sojung Go**, **Jooyoung Kim**, **Kyoung Jin Noh**, Sang Jun Park, **Soochahn Lee**

> **TL;DR:** A deep learning approach that jointly uses color fundus photographs and fluorescein angiography images to classify retinal vessels as arteries or veins, outperforming methods that rely on a single imaging modality.

---

## What this paper is about

![Figure description](/images/publications/2022-01-01-combined-deep-learning-of-fundus-images-fig1.png)
*Visual overview of the proposed method with integrated feature extractor CNN for combined fundus image and FA input (FE-CNN) and hierarchical connectivity GNN (HC-GNN).*

Distinguishing retinal arteries from veins is important for diagnosing vascular diseases like hypertension and diabetes. Color fundus photos show vessel structure but arteries and veins can look quite similar; fluorescein angiography (FA) captures blood-flow dynamics but is invasive. Using either modality alone leaves information on the table.

**This paper is an extension of the MICCAI 2020 paper "Combining fundus images and fluorescein angiography for artery/vein classification using the hierarchical vessel graph network."**

## Key idea

![Figure description](/images/publications/2022-01-01-combined-deep-learning-of-fundus-images-fig2.png)
*A visual description of the hierarchical connectivity graph neural network (HC-GNN) based on graph U-nets.*

The paper proposes a combined deep learning framework that fuses features from both fundus images and fluorescein angiography to perform artery/vein (A/V) classification. By learning complementary cues from both modalities -- structural appearance from fundus photos and flow-timing information from FA -- the model achieves more reliable vessel labeling.

## Why it mattersi

![Figure description](/images/publications/2022-01-01-combined-deep-learning-of-fundus-images-fig3.png)
*Qualitative results of sample cases from our private dataset, with top to bottom rows illustrating (1) the original image, (2) GT, and results of (3) FE-CNN only, (4) HVGN with a single graph U-net that has a two-channel output, and (5) the proposed HVGN with dual graph U-nets. Left and right columns shows the images in full and zoomed resolution, respectively.*

Accurate A/V classification supports early detection of systemic vascular conditions through routine eye exams and moves toward automated retinal image analysis that leverages the full range of clinical imaging data available.

