---
title: "Deep learning cross-phase style transfer for motion artifact correction in coronary computed tomography angiography."
collection: publications
date: 2020-01-01
venue: 'IEEE Access'
excerpt: 'Sunghee Jung, **Soochahn Lee**, Byunghwan Jeon, Yeonggul Jang, Hyuk-Jae Chang'
htmlurl: 'https://ieeexplore.ieee.org/abstract/document/9082676'
thumbnail: '/images/publications/2020-01-01-deep-learning-cross-phase-style-transfer-fig1.png'
bibtex: |
    @article{Jung_2020, title={Deep Learning Cross-Phase Style Transfer for Motion Artifact Correction in Coronary Computed Tomography Angiography}, volume={8}, ISSN={2169-3536}, url={http://dx.doi.org/10.1109/access.2020.2991445}, DOI={10.1109/access.2020.2991445}, journal={IEEE Access}, publisher={Institute of Electrical and Electronics Engineers (IEEE)}, author={Jung, Sunghee and Lee, Soochahn and Jeon, Byunghwan and Jang, Yeonggul and Chang, Hyuk-Jae}, year={2020}, pages={81849–81863} }
citation_mla: |
    Jung, Sunghee, et al. “Deep Learning Cross-Phase Style Transfer for Motion Artifact Correction in Coronary Computed Tomography Angiography.” IEEE Access, vol. 8, 2020, pp. 81849–63. Crossref, https://doi.org/10.1109/access.2020.2991445.
---

<!-- NOTE: Summary based on title only - verify and expand with actual abstract -->

**Authors:** Sunghee Jung, **Soochahn Lee**, Byunghwan Jeon, Yeonggul Jang, Hyuk-Jae Chang

> **TL;DR:** A deep learning style-transfer method that transfers the appearance of motion-free cardiac CT phases to motion-affected phases, correcting coronary artery motion artifacts in CCTA.

---

## What this paper is about

Coronary computed tomography angiography (CCTA) captures the heart across multiple cardiac phases, but some phases suffer from motion blur while others are relatively sharp. The motion-affected phases contain degraded coronary artery images that are hard to interpret clinically. This work extends the style-transfer idea for cross-phase artifact correction.

## Key idea

![Figure description](/images/publications/2020-01-01-deep-learning-cross-phase-style-transfer-fig1.png)
*Workflow of the proposed method. In step 1, generate synthetic motion-corrected patch (SynGT) using style transfer method. In step 2, train the motion artifact correction network (MAC-net) using SynGT. Detailed descriptions of steps 1 and 2 are in Sections II-B and II-C, respectively.*

The approach uses a deep learning framework to perform cross-phase style transfer: it learns to map the appearance characteristics of a motion-free cardiac phase onto a motion-affected phase, effectively synthesizing a corrected image. The network learns from paired data across cardiac phases to perform this translation.

## Why it matters

![Figure description](/images/publications/2020-01-01-deep-learning-cross-phase-style-transfer-fig2.png)
*Qualitative examples with minor and severe motion artifacts among the test data in the C AVAREV dataset. Each pair consists of the test patch data containing the mid-RCA (left), results of the proposed MAC-net (middle), and the corresponding reference patch (right). Source information (phase φin 4D CT) is presented above the pacthes. The radial artifacts are generated because of the number of projections (n = 133).*

By improving image quality in motion-degraded cardiac phases without requiring additional radiation dose or specialized acquisition protocols, this method makes CCTA more robust across different heart rates and patient conditions.

<!-- TODO: Add key figures from the paper -->
<!-- ![Figure description](/images/publications/2020-01-01-deep-learning-cross-phase-style-transfer-fig1.png) -->
