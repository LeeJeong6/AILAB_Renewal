---
title: "Triplanar convolution with shared 2D kernels for 3D classification and shape retrieval."
collection: publications
date: 2020-04-01
venue: 'Computer Vision and Image Understanding'
excerpt: 'Eu Young Kim, Seung Yeon Shin, **Soochahn Lee**, Kyong Joon Lee, Kyoung Ho Lee, Kyoung Mu Lee'
pdfurl: 'https://drive.google.com/file/d/1WPaOoCDSvkIp3HJCvPBq4R5-ERyWM289/view'
htmlurl: 'https://www.sciencedirect.com/science/article/abs/pii/S1077314219301791'
thumbnail: '/images/publications/2020-04-01-triplanar-convolution-with-shared-2d-ker-fig1.png'
bibtex: |
    @article{Kim_2020, title={Triplanar convolution with shared 2D kernels for 3D classification and shape retrieval}, volume={193}, ISSN={1077-3142}, url={http://dx.doi.org/10.1016/j.cviu.2019.102901}, DOI={10.1016/j.cviu.2019.102901}, journal={Computer Vision and Image Understanding}, publisher={Elsevier BV}, author={Kim, Eu Young and Shin, Seung Yeon and Lee, Soochahn and Lee, Kyong Joon and Lee, Kyoung Ho and Lee, Kyoung Mu}, year={2020}, month=apr, pages={102901} }
citation_mla: |
    Kim, Eu Young, et al. “Triplanar Convolution with Shared 2D Kernels for 3D Classification and Shape Retrieval.” Computer Vision and Image Understanding, vol. 193, Apr. 2020, p. 102901. Crossref, https://doi.org/10.1016/j.cviu.2019.102901.
---

<!-- NOTE: Summary based on title only - verify and expand with actual abstract -->

**Authors:** Eu Young Kim, Seung Yeon Shin, **Soochahn Lee**, Kyong Joon Lee, Kyoung Ho Lee, Kyoung Mu Lee

> **TL;DR:** A triplanar convolution approach that uses shared 2D kernels across three orthogonal planes to efficiently process 3D data for classification and shape retrieval, avoiding the heavy cost of full 3D convolutions.

---

## What this paper is about

![Figure description](/images/publications/2020-04-01-triplanar-convolution-with-shared-2d-ker-fig1.png)
*Triplanar CNN (S3PNet ) for 3D shape recognition. 3D data is first converted into binary voxel grids, which is then passed through the S3PNet which consists of series of planar modules. Each module consists of three branches of 2D convolutions that are iteratively applied to every cross-section of 3D input volume from different views.*

Full 3D convolutions are computationally expensive and parameter-hungry, making them impractical for many 3D recognition tasks. Triplanar approaches that process 2D slices along three orthogonal planes offer an efficient alternative, but existing methods typically use independent networks for each plane, missing cross-plane interactions.

## Key idea

![Figure description](/images/publications/2020-04-01-triplanar-convolution-with-shared-2d-ker-fig2.png)
*The shared 2D kernel-Triplanar block. The architecture of a single triplanar module. A 3D input volume is first decomposed into its respective cross-sections, then passed to each branch in a triplanar convolution. (a) 2D convolutions are applied to every cross-section of input volume on three different orthogonal views, namely, the 𝑥𝑦-plane, 𝑦𝑧-plane, and 𝑧𝑥-plane, respectively. Colored blocks represent the output feature-maps in each plane, red for the feature-maps in 𝑥𝑦-plane, blue in 𝑦𝑧-plane, and orange in 𝑧𝑥-plane. (b) Generated output feature-maps are then aggregated to form a single combined representation. After aggregating the feature-maps 1 × 1 convolution is applied to reduce feature redundancy and increase the compactness of the model.*

The method shares 2D convolutional kernels across the three orthogonal planes (axial, coronal, sagittal), which enforces consistency in feature extraction across views while keeping the parameter count low. This shared-kernel triplanar convolution captures 3D structure more efficiently than independent per-plane networks or full 3D convolutions.

## Why it matters

This work provides a practical and efficient architecture for 3D shape understanding that balances accuracy with computational cost, applicable to both medical imaging (e.g., organ classification) and general 3D shape retrieval tasks.

