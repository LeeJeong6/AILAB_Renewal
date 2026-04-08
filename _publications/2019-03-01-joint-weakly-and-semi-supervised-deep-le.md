---
title: "Joint weakly and semi-supervised deep learning for localization and classification of masses in breast ultrasound images."
collection: publications
date: 2019-03-01
venue: 'IEEE Trans. Med. Imaging'
excerpt: 'Seung Yeon Shin, **Soochahn Lee**, Il Dong Yun, Sun Mi Kim, Kyoung Mu Lee'
codeurl: 'https://github.com/syshin1014/wssdl_bus'
pdfurl: 'https://drive.google.com/file/d/1AVp792-GF3oFo0UbFbc5Lep4rFIt7MrF/view'
htmlurl: 'https://ieeexplore.ieee.org/document/8471199'
bibtex: |
    @article{Shin_2019, title={Joint Weakly and Semi-Supervised Deep Learning for Localization and Classification of Masses in Breast Ultrasound Images}, volume={38}, ISSN={1558-254X}, url={http://dx.doi.org/10.1109/tmi.2018.2872031}, DOI={10.1109/tmi.2018.2872031}, number={3}, journal={IEEE Transactions on Medical Imaging}, publisher={Institute of Electrical and Electronics Engineers (IEEE)}, author={Shin, Seung Yeon and Lee, Soochahn and Yun, Il Dong and Kim, Sun Mi and Lee, Kyoung Mu}, year={2019}, month=mar, pages={762–774} }
citation_mla: |
    Shin, Seung Yeon, et al. “Joint Weakly and Semi-Supervised Deep Learning for Localization and Classification of Masses in Breast Ultrasound Images.” IEEE Transactions on Medical Imaging, vol. 38, no. 3, Mar. 2019, pp. 762–74. Crossref, https://doi.org/10.1109/tmi.2018.2872031.
---

<!-- NOTE: Summary based on title only - verify and expand with actual abstract -->

**Authors:** Seung Yeon Shin, **Soochahn Lee**, Il Dong Yun, Sun Mi Kim, Kyoung Mu Lee

> **TL;DR:** A joint weakly and semi-supervised deep learning framework for localizing and classifying breast masses in ultrasound images, reducing the annotation burden while maintaining strong performance.

---

## What this paper is about

Getting pixel-level annotations for medical images is expensive and time-consuming, especially in breast ultrasound where masses need to be precisely delineated. This creates a bottleneck for training deep learning models. The question is how to train accurate localization and classification models when only a mix of weak labels (image-level) and limited pixel-level annotations are available.

## Key idea

The framework combines weakly supervised learning (using image-level labels indicating whether a mass is present) with semi-supervised learning (using a small set of fully annotated images) in a unified training pipeline. This joint approach leverages both types of supervision to learn mass localization and classification more effectively than either strategy alone.

## Why it matters

Published in IEEE Transactions on Medical Imaging, this work significantly reduces the annotation effort needed for training breast ultrasound CAD systems, making deep learning more practical for clinical deployment in breast cancer screening.

<!-- TODO: Add key figures from the paper -->
<!-- ![Figure description](/images/publications/2019-03-01-joint-weakly-and-semi-supervised-deep-le-fig1.png) -->
