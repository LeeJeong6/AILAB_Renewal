---
title: "Phase-based nonrigid deformation for digital subtraction angiography."
collection: publications
date: 2019-01-01
venue: 'IEEE Access'
excerpt: '**Soochahn Lee**, Changho Jeon, Leonard Sunwoo, Dong Yul Oh, Kyong Joon Lee'
htmlurl: 'https://ieeexplore.ieee.org/document/8667412'
thumbnail: '/images/publications/2019-01-01-phase-based-nonrigid-deformation-for-dig-fig2.png'
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

![Figure description](/images/publications/2019-01-01-phase-based-nonrigid-deformation-for-dig-fig1.png)
*1-D toy example to conceptually explain the proposed method. (a) Reference image. (b) Magnitude and (c) phase spectrums obtained by applying DFT to the reference image. (d) Target image. (e) Magnitude and (f) phase applying DFT to the target image. (h) Magnitude for the deformed image, copied from (b). (i) Phase for the deformed image, which is determined by comparing the magnitude of the reference (b) and that of the target (e) for each frequency. (g) Deformed image applying iDFT to (h) and (i).*

![Figure description](/images/publications/2019-01-01-phase-based-nonrigid-deformation-for-dig-fig2.png)
*Efficient computation of steerable pyramid. (a) Original input image. (b) DFT of the input image (the real part.) (c) DFT of steerable pyramid filters. Each subband represents a filter and is illustrated with different colors. [9] (d) Aggregation of filter responses. Each response can be easily calculated by multiplying corresponding subband to the DFT of input image. Applying inverse DFT to the aggregation can reconstruct the original image.*

The method uses phase-based representations of the images to estimate and correct nonrigid deformations between the mask and contrast frames. Phase-based approaches are robust to intensity differences between the two frames (one has contrast agent, one does not), making them well-suited for this cross-modal registration problem.

## Why it matters

![Figure description](/images/publications/2019-01-01-phase-based-nonrigid-deformation-for-dig-fig3.png)
**

Cleaner DSA images mean better visualization of blood vessels during diagnostic and interventional procedures, directly improving clinical workflow for neuroradiology and vascular imaging.

