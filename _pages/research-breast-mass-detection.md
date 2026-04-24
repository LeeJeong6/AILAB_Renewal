---
layout: single
title: "Mass Detection from Mammography and Ultrasound Images"
permalink: /research/breast-mass-detection/
author_profile: false
---

Early detection of breast cancer relies on accurately identifying microcalcifications in mammograms and suspicious masses in ultrasound. Our research develops automated detection pipelines that balance sensitivity, specificity, and computational efficiency, and that make effective use of the partial annotations typically available in clinical data.

## Research directions

- **Cascade and classification-based microcalcification detection.** Cascade classifier architectures progressively filter non-calcification regions, concentrating computation on promising candidates; classification-based detection with discriminative restricted Boltzmann machines learns features directly suited to separating calcifications from background tissue.
- **Weakly and semi-supervised mass detection in ultrasound.** Joint frameworks that combine image-level labels with a small set of fully annotated images, reducing annotation cost while still learning precise localization and classification of masses.

## Related publications

- [Classification Based Micro-calcification Detection using Discriminative Restricted Boltzmann Machine in Digitized Mammograms](/publications/2014-03-24-classification-based-micro-calcification/) — SPIE Medical Imaging, 2014
- [A Novel Cascade Classifier for Automatic Microcalcification Detection](/publications/2015-12-02-a-novel-cascade-classifier-for-automatic/) — PLoS ONE, 2015
- [Joint Weakly and Semi-Supervised Deep Learning for Localization and Classification of Masses in Breast Ultrasound Images](/publications/2019-03-01-joint-weakly-and-semi-supervised-deep-le/) — IEEE Transactions on Medical Imaging, 2019
