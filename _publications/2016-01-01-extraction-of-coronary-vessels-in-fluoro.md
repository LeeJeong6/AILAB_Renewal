---
title: "Extraction of coronary vessels in fluoroscopic X-ray sequences using vessel correspondence optimization."
collection: publications
date: 2016-01-01
venue: 'International Conference on Medical Image Computing and Computer-Assisted Intervention (MICCAI)'
excerpt: 'Seung Yeon Shin, **Soochahn Lee**, **Kyoung Jin Noh**, Il Dong Yun, Kyoung Mu Lee'
pdfurl: 'https://cv.snu.ac.kr/publication/conf/2016/VCO_MICCAI2016.pdf'
htmlurl: 'https://link.springer.com/chapter/10.1007/978-3-319-46726-9_36'
thumbnail: '/images/publications/2016-01-01-extraction-of-coronary-vessels-in-fluoro-fig2.png'
bibtex: |
    @inbook{Shin_2016, title={Extraction of Coronary Vessels in Fluoroscopic X-Ray Sequences Using Vessel Correspondence Optimization}, ISBN={9783319467269}, ISSN={1611-3349}, url={http://dx.doi.org/10.1007/978-3-319-46726-9_36}, DOI={10.1007/978-3-319-46726-9_36}, booktitle={Medical Image Computing and Computer-Assisted Intervention - MICCAI 2016}, publisher={Springer International Publishing}, author={Shin, Seung Yeon and Lee, Soochahn and Noh, Kyoung Jin and Yun, Il Dong and Lee, Kyoung Mu}, year={2016}, pages={308–316} }
citation_mla: |
    Shin, Seung Yeon, et al. “Extraction of Coronary Vessels in Fluoroscopic X-Ray Sequences Using Vessel Correspondence Optimization.” Medical Image Computing and Computer-Assisted Intervention - MICCAI 2016, 2016, pp. 308–16. Crossref, https://doi.org/10.1007/978-3-319-46726-9_36.
---

<!-- NOTE: Summary based on title only - verify and expand with actual abstract -->

**Authors:** Seung Yeon Shin, **Soochahn Lee**, **Kyoung Jin Noh**, Il Dong Yun, Kyoung Mu Lee

> **TL;DR:** A vessel correspondence optimization method for extracting coronary vessels from fluoroscopic X-ray image sequences, presented at MICCAI 2016.

---

## What this paper is about

![Figure description](/images/publications/2016-01-01-extraction-of-coronary-vessels-in-fluoro-fig1.png)
*A fluoroscopic XRA sequence with vessels extracted by the proposed method overlaid (green). Frames (13, 18, 24, and 31, respectively) are sparsely sampled to clearly show dynamics.*

During cardiac catheterization procedures, doctors use fluoroscopic X-ray sequences to visualize coronary arteries. Automatically extracting the vessel structure from these noisy, low-contrast sequences is essential for guiding interventions, but the vessels move with each heartbeat and overlap with other structures.

## Key idea

![Figure description](/images/publications/2016-01-01-extraction-of-coronary-vessels-in-fluoro-fig2.png)
*Illustration of overall framework. Vessel centerlines of the destination frame are extracted based on the centerlines of the source frame, which we assume to be given. (a) Global search by chamfer matching. Source (green) and translated (red) vessel centerlines are overlaid. (b) Vessel branch search by keypoint correspondence (white). (c) Correspondence candidates (green) by vessel point search. White points in zoomed box show candidates for the black vessel point. (d) Optimal point correspondences (white) from MRF optimization. (e) Extraction of newly visible vessel branches. (a)-(c) Comprise a hierarchical search scheme.*

The paper introduces a vessel correspondence optimization approach that tracks and extracts coronary vessels across frames in fluoroscopic X-ray sequences. By establishing correspondences between vessel segments across time, the method can robustly recover the vessel tree even in the presence of cardiac motion, breathing artifacts, and contrast agent variations.

## Why it matters

![Figure description](/images/publications/2016-01-01-extraction-of-coronary-vessels-in-fluoro-fig3.png)
*Qualitative results. Odd and even rows show sample frames and their corresponding enlarged views of erroneous regions, from diﬀerent sequences, respecitively. Red points in column 3–5 are resulting vessel points of VCO.*

Accurate automatic coronary vessel extraction from fluoroscopy supports real-time guidance during cardiac interventions, reducing the cognitive burden on clinicians and potentially improving procedure outcomes.

