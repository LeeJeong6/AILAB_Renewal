---
title: "Abnormality detection in chest X-ray via residual-saliency from normal generation"
collection: publications
date: 2023-01-01
venue: 'IEEE Access'
excerpt: 'Euyoung Kim, **Soochahn Lee**, Kyoung Mu Lee'
htmlurl: 'https://ieeexplore.ieee.org/abstract/document/10057408'
# pdfurl: ''
thumbnail: '/images/publications/2023-01-01-abnormality-detection-in-chest-x-ray-via-fig3.png'
bibtex: |
    @article{Kim_2023, title={Abnormality Detection in Chest X-Ray via Residual-Saliency From Normal Generation}, volume={11}, ISSN={2169-3536}, url={http://dx.doi.org/10.1109/access.2023.3251350}, DOI={10.1109/access.2023.3251350}, journal={IEEE Access}, publisher={Institute of Electrical and Electronics Engineers (IEEE)}, author={Kim, Euyoung and Lee, Soochahn and Lee, Kyoung Mu}, year={2023}, pages={21799–21810} }
citation_mla: |
    Kim, Euyoung, et al. “Abnormality Detection in Chest X-Ray via Residual-Saliency From Normal Generation.” IEEE Access, vol. 11, 2023, pp. 21799–810. Crossref, https://doi.org/10.1109/access.2023.3251350.
---
<!-- NOTE: Summary based on title only - verify and expand with actual abstract -->

**Authors:** Euyoung Kim, **Soochahn Lee**, Kyoung Mu Lee

> **TL;DR:** An anomaly detection method for chest X-rays that generates a "normal" version of a given image, then computes a residual saliency map to localize abnormalities without needing per-lesion annotations.

---

## What this paper is about

![Figure description](/images/publications/2023-01-01-abnormality-detection-in-chest-x-ray-via-fig1.png)
*Manual diagnosis vs. automatic diagnosis. Abnormality regions can be identified by considering the differences between the input CXR and its corresponding estimated healthy CXR image.*

Chest X-ray reading is one of the most common tasks in radiology, yet collecting large annotated datasets covering every possible pathology is impractical. A more scalable approach is to learn what healthy lungs look like and flag anything that deviates from that baseline.

## Key idea

![Figure description](/images/publications/2023-01-01-abnormality-detection-in-chest-x-ray-via-fig2.png)
*Proposed framework overview. First, for a given real CXR, its corresponding matching-pair CXR is constructed. Then, the constructed matching-pair CXRs are used to train a normal CXR translator, which transforms any given image to its corresponding normal CXR image. $x^i$ and $x^i_p$ denote the $i_{th}$ abnormal CXR and its corresponding matching-normal CXR image. Lastly, the trained normal CXR translator is combined with the detector to reason about the disease.*

![Figure description](/images/publications/2023-01-01-abnormality-detection-in-chest-x-ray-via-fig3.png)
*Matching-pair CXR synthesis. Here, the descriptive example is used for constructing a matching-normal CXR from a given abnormal CXR, but the process is identical for constructing a matching-abnormal CXR from normal CXR. First, the input CXR is aligned using a spatial transformer network (STN), and then the K nearest neighbor normal CXRs are retrieved. Assuming the pathological ROI boxes are known, we crop and blend these regions from the nearest neighbors into the aligned input CXRs to obtain initial matching-pair CXRs. The initial matching-pair CXRs are then used as inputs to train a CXR translator for synthesizing the final matching-pair CXRs.*

The method trains a generative model on normal chest X-rays so it can reconstruct what a healthy version of any input image would look like. The difference (residual) between the original and the generated normal image produces a saliency map highlighting abnormal regions. This residual-saliency signal localizes pathology without requiring bounding-box or pixel-level disease labels during training.

## Why it matters

This unsupervised approach to abnormality detection can serve as a first-pass screening tool in clinical workflows, catching a broad range of pathologies -- including rare ones -- without being limited by the diseases seen during supervised training.

