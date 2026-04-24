---
title: "FQ-UWF: unpaired generative image enhancement for fundus quality ultra-widefield retinal images"
collection: publications
date: 2024-06-04
venue: 'Bioengineering'
excerpt: 'Kang Geon Lee, Su Jeong Song, **Soochahn Lee**, Bo Hee Kim, Mingui Kong, Kyoung Mu Lee'
htmlurl: 'https://www.mdpi.com/2306-5354/11/6/568'
pdfurl: 'https://www.mdpi.com/2306-5354/11/6/568/pdf?version=1718185733'
thumbnail: '/images/publications/2024-06-04-fq-uwf-unpaired-generative-image-enhanc-fig1.png'
bibtex: |
    @article{Lee_2024, title={FQ-UWF: Unpaired Generative Image Enhancement for Fundus Quality Ultra-Widefield Retinal Images}, volume={11}, ISSN={2306-5354}, url={http://dx.doi.org/10.3390/bioengineering11060568}, DOI={10.3390/bioengineering11060568}, number={6}, journal={Bioengineering}, publisher={MDPI AG}, author={Lee, Kang Geon and Song, Su Jeong and Lee, Soochahn and Kim, Bo Hee and Kong, Mingui and Lee, Kyoung Mu}, year={2024}, month=jun, pages={568} }
citation_mla: |
    Lee, Kang Geon, et al. “FQ-UWF: Unpaired Generative Image Enhancement for Fundus Quality Ultra-Widefield Retinal Images.” Bioengineering, vol. 11, no. 6, June 2024, p. 568. Crossref, https://doi.org/10.3390/bioengineering11060568.
---

<!-- NOTE: Summary based on title only - verify and expand with actual abstract -->

**Authors:** Kang Geon Lee, Su Jeong Song, **Soochahn Lee**, Bo Hee Kim, Mingui Kong, Kyoung Mu Lee

> **TL;DR:** An unpaired generative method (FQ-UWF) that enhances the quality of ultra-widefield retinal images to match the clarity of standard fundus photography, without needing paired training data.

---

## What this paper is about

<!-- TODO: Add key figures from the paper -->
![Figure description](/images/publications/2024-06-04-fq-uwf-unpaired-generative-image-enhanc-fig1.png)
*Sample results of the proposed UWF enhancement method. The top row depicts the input UWF images, and the bottom row depicts the FQ-UWF images enhanced by the proposed method. Numbered boxes are enlarged sample views of representative local regions. The clarity of anatomical structures such as vessels is greatly improved in the FQ-UWF images.*

Ultra-widefield (UWF) retinal imaging captures a much larger area of the retina than standard fundus cameras, but the image quality -- especially in terms of contrast and resolution -- often falls short. Getting paired UWF and high-quality fundus images of the same eye is impractical for supervised training.

## Key idea

![Figure description](/images/publications/2024-06-04-fq-uwf-unpaired-generative-image-enhanc-fig2.png)
*The overall architecture of the proposed method. IUW F with severe degradations and artifacts is first enhanced to $I_{E−UWF}$ via $G_{DE}$, for which the output is fed to $G_{SR}$ to generate $\times 4$ up-scaled $I_{FQ−UWF}$. $I_{fundus}$ is down-scaled to $I_{DS−fundus}$ with a scaling factor of 4. $D_{DE}$ and $D_{SR}$ measure the similarity between $I_{E−UWF}$ and $I_{DS−fundus}$ to train $G_{DE}$ and the similarity between $I_{FQ−UWF}$ and $I_{fundus}$ to train $G_{SR}$, respectively.*

FQ-UWF uses an unpaired generative image enhancement framework to translate low-quality UWF images into fundus-quality versions. The approach learns the quality characteristics of standard fundus images and applies them to UWF images without requiring pixel-aligned training pairs.

## Why it matters

Better UWF image quality means clinicians can leverage the wide coverage of UWF imaging without sacrificing the diagnostic detail they rely on from traditional fundus photography.

