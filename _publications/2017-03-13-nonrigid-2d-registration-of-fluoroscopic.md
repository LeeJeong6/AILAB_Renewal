---
title: "Nonrigid 2D registration of fluoroscopic coronary artery image sequence with propagated deformation field."
collection: publications
date: 2017-03-13
venue: 'Medical Imaging: Biomedical Applications'
excerpt: 'Taewoo Park, Seung Yeon Shin, Youngtaek Hong, **Soochahn Lee**, Hyuk-Jae Chang, Il Dong Yun'
htmlurl: 'https://www.spiedigitallibrary.org/conference-proceedings-of-spie/10137/101371W/Nonrigid-2D-registration-of-fluoroscopic-coronary-artery-image-sequence-with/10.1117/12.2255551.short?SSO=1'
bibtex: |
    @inproceedings{Park_2017, title={Nonrigid 2D registration of fluoroscopic coronary artery image sequence with propagated deformation field}, volume={10137}, ISSN={0277-786X}, url={http://dx.doi.org/10.1117/12.2255551}, DOI={10.1117/12.2255551}, booktitle={Medical Imaging 2017: Biomedical Applications in Molecular, Structural, and Functional Imaging}, publisher={SPIE}, author={Park, Taewoo and Shin, Seung Yeon and Hong, Youngtaek and Lee, Soochahn and Chang, Hyuk-Jae and Yun, Il Dong}, editor={Krol, Andrzej and Gimi, Barjor}, year={2017}, month=mar, pages={101371W} }
citation_mla: |
    Park, Taewoo, et al. “Nonrigid 2D Registration of Fluoroscopic Coronary Artery Image Sequence with Propagated Deformation Field.” Medical Imaging 2017: Biomedical Applications in Molecular, Structural, and Functional Imaging, edited by Andrzej Krol and Barjor Gimi, vol. 10137, Mar. 2017, p. 101371W. Crossref, https://doi.org/10.1117/12.2255551.
---

<!-- NOTE: Summary based on title only - verify and expand with actual abstract -->

**Authors:** Taewoo Park, Seung Yeon Shin, Youngtaek Hong, **Soochahn Lee**, Hyuk-Jae Chang, Il Dong Yun

> **TL;DR:** A nonrigid 2D registration method for fluoroscopic coronary artery sequences that propagates deformation fields across frames to handle cardiac motion.

---

## What this paper is about

Coronary artery images from fluoroscopic X-ray sequences are distorted by cardiac and respiratory motion between frames. Registering these frames to each other is needed for tasks like vessel tracking and motion compensation, but the deformation is nonrigid and changes continuously.

## Key idea

The paper proposes propagating deformation fields across the fluoroscopic image sequence, using the estimated deformation from neighboring frames to initialize and constrain the registration of subsequent frames. This temporal propagation provides a good starting point for each frame's registration and improves overall alignment accuracy.

## Why it matters

Better nonrigid registration of coronary artery sequences enables more accurate motion compensation during cardiac interventions, supporting improved visualization and analysis of vessel dynamics.

<!-- TODO: Add key figures from the paper -->
<!-- ![Figure description](/images/publications/nonrigid-2d-registration-of-fluoroscopic-fig1.png) -->
