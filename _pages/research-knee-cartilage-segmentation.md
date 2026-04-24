---
layout: single
title: "Knee Cartilage Segmentation from MR Images"
permalink: /research/knee-cartilage-segmentation/
author_profile: false
---

Quantitative assessment of articular cartilage in 3D knee MR images is central to osteoarthritis research and clinical monitoring, but cartilage is thin, low-contrast, and topologically complex — making reliable segmentation a long-standing challenge. Our work in this area developed a progression of 3D segmentation frameworks built around graph-cut optimization, localized probabilistic modeling, coarse-to-fine strategies, and unified automatic/interactive pipelines, largely evaluated on MR data from the Osteoarthritis Initiative (OAI).

## Research directions

- **3D graph-cut segmentation.** Energy-minimization formulations over voxel graphs that balance image data fidelity with spatial smoothness, applied to articular cartilage and extended with iterative local branch-and-mincut for fully automatic bone compartment segmentation.
- **Localized shape and appearance modeling.** Joint optimization of local shape and appearance probabilities so that the model adapts to patient-specific anatomy rather than relying on global priors alone.
- **Hierarchical MRF with localized classifiers.** Globally consistent localized classifiers integrated into a multi-level MRF, combining spatially specialized training with global topological consistency.
- **Coarse-to-fine bone and cartilage segmentation.** Approximate localization followed by iterative boundary refinement, producing accurate 3D bone compartment segmentation in knee MR.
- **Unified automatic + interactive segmentation.** Structured patch models that seamlessly bridge automatic segmentation and interactive editing within a single framework.

## Related publications

- [3-D Segmentation of Articular Cartilages by Graph Cuts using Knee MR Images from the Osteoarthritis Initiative](/publications/2008-03-06-3-d-segmentation-of-articular-cartilages/) — SPIE Medical Imaging, 2008
- [Fully Automatic 3-D Segmentation of Knee Bone Compartments by Iterative Local Branch-and-Mincut on MR Images from OAI](/publications/2009-11-01-fully-automatic-3-d-segmentation-of-knee/) — ICIP, 2009
- [Optimization of Local Shape and Appearance Probabilities for Segmentation of Knee Cartilage in 3-D MR Images](/publications/2011-12-01-optimization-of-local-shape-and-appearan/) — Computer Vision and Image Understanding, 2011
- [Automatic Bone Segmentation in Knee MR Images using a Coarse-to-Fine Strategy](/publications/2012-02-23-automatic-bone-segmentation-in-knee-mr-i/) — SPIE Medical Imaging, 2012
- [Hierarchical MRF of Globally Consistent Localized Classifiers for 3D Medical Image Segmentation](/publications/2013-09-01-hierarchical-mrf-of-globally-consistent/) — Pattern Recognition, 2013
- [Structured Patch Model for a Unified Automatic and Interactive Segmentation Framework](/publications/2015-08-01-structured-patch-model-for-a-unified-aut/) — Medical Image Analysis, 2015
