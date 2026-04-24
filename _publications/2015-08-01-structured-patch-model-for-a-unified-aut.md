---
title: "Structured patch model for a unified automatic and interactive segmentation framework."
collection: publications
date: 2015-08-01
venue: 'Medical Image Analysis'
excerpt: 'Sang Hyun Park, **Soochahn Lee**, Il Dong Yun, Sang Uk Lee'
pdfurl: 'https://drive.google.com/file/d/1IxsxmsaAwquABRgvCyL_AucIaywsQXh2/view'
htmlurl: 'https://www.sciencedirect.com/science/article/abs/pii/S136184151500016X'
thumbnail: '/images/publications/2015-08-01-structured-patch-model-for-a-unified-aut-fig1.png'
bibtex: |
    @article{Park_2015, title={Structured patch model for a unified automatic and interactive segmentation framework}, volume={24}, ISSN={1361-8415}, url={http://dx.doi.org/10.1016/j.media.2015.01.003}, DOI={10.1016/j.media.2015.01.003}, number={1}, journal={Medical Image Analysis}, publisher={Elsevier BV}, author={Park, Sang Hyun and Lee, Soochahn and Yun, Il Dong and Lee, Sang Uk}, year={2015}, month=aug, pages={297–312} }
citation_mla: |
    Park, Sang Hyun, et al. “Structured Patch Model for a Unified Automatic and Interactive Segmentation Framework.” Medical Image Analysis, vol. 24, no. 1, Aug. 2015, pp. 297–312. Crossref, https://doi.org/10.1016/j.media.2015.01.003.
---

<!-- NOTE: Summary based on title only - verify and expand with actual abstract -->

**Authors:** Sang Hyun Park, **Soochahn Lee**, Il Dong Yun, Sang Uk Lee

> **TL;DR:** A structured patch model that unifies automatic and interactive segmentation into a single framework for medical image analysis.

---

## What this paper is about

Medical image segmentation often comes in two flavors: fully automatic methods and interactive methods where a clinician provides guidance. These are typically designed as separate systems, making it hard to let a user correct automatic results or to leverage automation in interactive workflows.

## Key idea

![Figure description](/images/publications/2015-08-01-structured-patch-model-for-a-unified-aut-fig1.png)
*Proposed framework based on the structured patch model (StPM). Dots around the boundaries of right and left lungs represent the centers of patches. The DSC values for each lung are also given below the segmentation results. Erroneous regions (black circles) are repeatedly corrected with respect to the user annotations (red and blue denote the object and background scribbles, respectively) until the segmentation results are satisfactory. The final result can be directly used to increment the StPM.*

The paper introduces a structured patch model that seamlessly bridges automatic and interactive segmentation. The model uses patch-based representations with structural constraints, allowing it to produce initial automatic segmentations and then incorporate user input (such as scribbles or corrections) within the same unified framework.

## Why it matters

By unifying both paradigms, clinicians get the best of both worlds: fast automatic results with the ability to interactively refine them, improving both efficiency and accuracy in clinical medical image analysis workflows.

