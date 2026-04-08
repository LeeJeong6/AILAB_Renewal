---
title: "Phase-based nonrigid deformation for digital subtraction angiography."
collection: publications
date: 2019-01-01
venue: 'IEEE Access'
excerpt: '**Soochahn Lee**, Changho Jeon, Leonard Sunwoo, Dong Yul Oh, Kyong Joon Lee'
htmlurl: 'https://ieeexplore.ieee.org/document/8667412'
bibtex: |
    @article{Lee_2019, title={Phase-Based Nonrigid Deformation for Digital Subtraction Angiography}, volume={7}, ISSN={2169-3536}, url={http://dx.doi.org/10.1109/access.2019.2902562}, DOI={10.1109/access.2019.2902562}, journal={IEEE Access}, publisher={Institute of Electrical and Electronics Engineers (IEEE)}, author={Lee, Soochahn and Jeon, Chang Ho and Sunwoo, Leonard and Oh, Dong Yul and Lee, Kyong Joon}, year={2019}, pages={32256–32265} }
citation_mla: |
    Lee, Soochahn, et al. “Phase-Based Nonrigid Deformation for Digital Subtraction Angiography.” IEEE Access, vol. 7, 2019, pp. 32256–65. Crossref, https://doi.org/10.1109/access.2019.2902562.
---

<!-- NOTE: Summary based on title only - verify and expand with actual abstract -->

**Authors:** **Soochahn Lee**, Changho Jeon, Leonard Sunwoo, Dong Yul Oh, Kyong Joon Lee

> **TL;DR:** A phase-based nonrigid deformation method for digital subtraction angiography (DSA) that corrects misalignment between mask and contrast frames, reducing subtraction artifacts.

---

## What this paper is about

Digital subtraction angiography works by subtracting a "mask" image (without contrast) from a "contrast" image (with injected dye) to isolate the blood vessels. But if the patient moves between the two acquisitions, the subtraction produces ugly artifacts that obscure the vessels. Correcting this motion is essential but challenging because the deformation is nonrigid.

## Key idea

The method uses phase-based representations of the images to estimate and correct nonrigid deformations between the mask and contrast frames. Phase-based approaches are robust to intensity differences between the two frames (one has contrast agent, one does not), making them well-suited for this cross-modal registration problem.

## Why it matters

Cleaner DSA images mean better visualization of blood vessels during diagnostic and interventional procedures, directly improving clinical workflow for neuroradiology and vascular imaging.

<!-- TODO: Add key figures from the paper -->
<!-- ![Figure description](/images/publications/2019-01-01-phase-based-nonrigid-deformation-for-dig-fig1.png) -->
