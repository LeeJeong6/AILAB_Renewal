---
title: "Auto-regressive transformation for image alignment"
collection: publications
date: 2025-10-01
venue: 'IEEE/CVF International Conference on Computer Vision (ICCV)'
excerpt: 'Kanggeon Lee, **Soochahn Lee**, Kyoung Mu Lee'
posterurl: 'https://iccv.thecvf.com/media/PosterPDFs/ICCV%202025/28.png?t=1758783578.5315154'
htmlurl: 'https://openaccess.thecvf.com/content/ICCV2025/html/Lee_Auto-Regressive_Transformation_for_Image_Alignment_ICCV_2025_paper.html'
pdfurl: 'https://openaccess.thecvf.com/content/ICCV2025/papers/Lee_Auto-Regressive_Transformation_for_Image_Alignment_ICCV_2025_paper.pdf'
bibtex: |
    @inproceedings{lee2025autoregressive,
      title={Auto-regressive transformation for image alignment},
      author={Lee, Kanggeon and Lee, Soochahn and Lee, Kyoung Mu},
      booktitle={Proceedings of the IEEE/CVF International Conference on Computer Vision (ICCV)},
      year={2025},
      month=oct
    }
citation_mla: |
    Lee, Kanggeon, et al. "Auto-regressive transformation for image alignment." arXiv preprint, 2025.
---

<!-- NOTE: Summary based on title only - verify and expand with actual abstract -->

**Authors:** Kanggeon Lee, **Soochahn Lee**, Kyoung Mu Lee

> **TL;DR:** An auto-regressive approach to image alignment that sequentially predicts transformation parameters, enabling accurate registration of images with complex, non-rigid deformations.

---

## What this paper is about

Image alignment (registration) typically estimates a single global or local transformation in one shot, which can struggle with large, complex deformations. Real-world image pairs -- especially in medical or remote sensing domains -- often require handling intricate spatial relationships that are hard to capture all at once.

![Figure description](/images/publications/2025-10-01-auto-regressive-transformation-for-image-fig1.png)
***Alignment Results in Challenging Scenarios.** For image pairs with sparse features, scale differences, deformations degradations, and domain shifts, our method performs coarse-to-fine auto-regressive transformation refinement, achieving accurate alignment even in challenging scenarios where state-of-the-art methods struggle. The zoomed-in boxes show the local alignment results, and the highlighted vessel image below illustrates the intersection (yellow) between the two images (red and green).*

## Key idea

The paper reformulates image alignment as an auto-regressive process, where transformation parameters are predicted sequentially, each step conditioned on the previous ones. This decomposition allows the model to handle complex deformations by building up the transformation incrementally rather than predicting everything in a single pass.

![Figure description](/images/publications/2025-10-01-auto-regressive-transformation-for-image-fig2.png)
*Auto-Regressive Transformation (ART) iteratively refines the transformation D for image pairs I in a coarse-to-fine manner. Its sampling strategy enables effective operation across diverse domains and datasets.*

![Figure description](/images/publications/2025-10-01-auto-regressive-transformation-for-image-fig3.png)
*ART first extracts multi-scale features Fs and Fd from the input image pair Is and Id. At each sampling step k, the corresponding features, F k s and F k d , are passed through the Cross-Attention Layer (CAL) to identify the correlated features that guide the network’s focus on regions requiring refinement. The attentive feature map˜F k s→d is then used to refine the transform field parameters Dk M and Dk A to Dk+1 M and Dk+1 A through multiple convolutional neural networks. This auto-regressive process continues until the initialized transform field parameters D0 M and D0 A reach the full resolution of the input image pair Is and Id.*

## Why it matters

Presented at ICCV 2025, this approach provides a principled way to tackle difficult alignment problems and could generalize across many domains where accurate image registration is critical.

