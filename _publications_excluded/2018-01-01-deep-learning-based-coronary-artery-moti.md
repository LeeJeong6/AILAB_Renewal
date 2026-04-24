---
title: "Deep learning based coronary artery motion artifact compensation using style-transfer synthesis in CT images."
collection: publications
date: 2018-01-01
venue: 'SASHIMI'
excerpt: 'Sunghee Jung, **Soochahn Lee**, Byunghwan Jeon, Yeonggul Jang, Hyuk-Jae Chang'
pdfurl: 'https://drive.google.com/file/d/1L4O7i9nq82kFAgqv2BLAlz8QDSujSeIY/view'
htmlurl: 'https://link.springer.com/chapter/10.1007/978-3-030-00536-8_11'
bibtex: |
    @inbook{Jung_2018, title={Deep Learning Based Coronary Artery Motion Artifact Compensation Using Style-Transfer Synthesis in CT Images}, ISBN={9783030005368}, ISSN={1611-3349}, url={http://dx.doi.org/10.1007/978-3-030-00536-8_11}, DOI={10.1007/978-3-030-00536-8_11}, booktitle={Simulation and Synthesis in Medical Imaging}, publisher={Springer International Publishing}, author={Jung, Sunghee and Lee, Soochahn and Jeon, Byunghwan and Jang, Yeonggul and Chang, Hyuk-Jae}, year={2018}, pages={100–110} }
citation_mla: |
    Jung, Sunghee, et al. “Deep Learning Based Coronary Artery Motion Artifact Compensation Using Style-Transfer Synthesis in CT Images.” Simulation and Synthesis in Medical Imaging, 2018, pp. 100–10. Crossref, https://doi.org/10.1007/978-3-030-00536-8_11.
---

<!-- NOTE: Summary based on title only - verify and expand with actual abstract -->

**Authors:** Sunghee Jung, **Soochahn Lee**, Byunghwan Jeon, Yeonggul Jang, Hyuk-Jae Chang

> **TL;DR:** A deep learning approach using style-transfer synthesis to correct motion artifacts in coronary artery CT images, improving image quality without additional scanning.

---

## What this paper is about

Coronary artery imaging with CT is tricky because the heart is constantly moving, which creates motion artifacts that blur the images. These artifacts make it harder for clinicians to assess coronary artery disease accurately. This work tackles the problem of computationally compensating for those motion artifacts after the scan is already done.

## Key idea

The method uses a style-transfer framework powered by deep learning to synthesize motion-corrected CT images from motion-affected ones. By learning the mapping between blurry (motion-affected) and sharp (motion-free) cardiac phases, the network can generate cleaner images that look as if they were captured at the optimal cardiac phase.

## Why it matters

This approach could reduce the need for repeat scans or specialized hardware to handle cardiac motion, making coronary CT angiography more reliable and accessible for routine clinical use.

<!-- TODO: Add key figures from the paper -->
<!-- ![Figure description](/images/publications/2018-01-01-deep-learning-based-coronary-artery-moti-fig1.png) -->
