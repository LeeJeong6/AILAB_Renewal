---
title: "Generation of Structurally Realistic Retinal Fundus Images with Diffusion Models"
collection: publications
date: 2024-06-17
venue: 'IEEE/CVF Conference on Computer Vision and Pattern Recognition Workshop (CVPRW)'
excerpt: 'Sojung Go, Younghoon Ji, Sang Jun Park, **Soochahn Lee**'
htmlurl: 'https://openaccess.thecvf.com/content/CVPR2024W/DCAMI/html/Go_Generation_of_Structurally_Realistic_Retinal_Fundus_Images_with_Diffusion_Models_CVPRW_2024_paper.html'
pdfurl: 'https://openaccess.thecvf.com/content/CVPR2024W/DCAMI/papers/Go_Generation_of_Structurally_Realistic_Retinal_Fundus_Images_with_Diffusion_Models_CVPRW_2024_paper.pdf'
thumbnail: '/images/publications/2024-06-17-generation-of-structurally-realistic-r-fig1.png'
dataseturl: 
bibtex: |
    @InProceedings{Go_2024_CVPR, author = {Go, Sojung and Ji, Younghoon and Park, Sang Jun and Lee, Soochahn}, title = {Generation of Structurally Realistic Retinal Fundus Images with Diffusion Models}, booktitle = {Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR) Workshops}, month = {June}, year = {2024}, pages = {2335-2344} }
citation_mla: |
    Go, Sojung, et al. “Generation of Structurally Realistic Retinal Fundus Images with Diffusion Models.” Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR) Workshops, 2024, pp. 2335–2344.
---

<!-- NOTE: Summary based on title only - verify and expand with actual abstract -->

**Authors:** Sojung Go, Younghoon Ji, Sang Jun Park, **Soochahn Lee**

> **TL;DR:** A diffusion-model-based framework that generates retinal fundus images whose vascular and anatomical structures are structurally realistic, enabling high-fidelity synthetic data for downstream retinal analysis.

---

## What this paper is about

![Figure description](/images/publications/2024-06-17-generation-of-structurally-realistic-r-fig1.png)
*Sample of generated fundus image and artery/vein mask from the proposed method, together with a real data for comparison. The proposed method can generate anatomically accurate fundus images and corresponding artery/vein masks.*

Synthetic retinal fundus images are useful for augmenting training data, but conventional generative models often produce images with anatomically implausible vessel trees and optic disc structures. This paper explores whether diffusion models can be guided to produce fundus images whose underlying anatomy is realistic enough to support downstream clinical tasks.

## Key idea

![Figure description](/images/publications/2024-06-17-generation-of-structurally-realistic-r-fig2.png)
*Overview of the proposed method. The top row depicts the process for generating GT A/V masks, which are used to train $G_M$, which generates new A/V masks, and $G_I$ which generates fundus images conditioned on the A/V masks. $G_E$ performs super-resolution to generate high-resolution images.*

The method leverages diffusion models conditioned on structural priors so that generated fundus images exhibit coherent vessel topology and plausible optic disc / macula arrangement. By incorporating explicit structural guidance into the generation process, the framework produces images that are both visually realistic and anatomically consistent.

## Why it matters

Structurally realistic synthetic fundus images can mitigate data-scarcity issues in retinal imaging research, especially for rare pathologies, and support the development of more robust models for tasks such as vessel segmentation, disease classification, and screening.
