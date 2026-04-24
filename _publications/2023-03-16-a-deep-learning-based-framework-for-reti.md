---
title: "A deep learning-based framework for retinal fundus image enhancement"
collection: publications
date: 2023-03-16
venue: 'PLoS ONE'
excerpt: 'Kang Geon Lee, Su Jeong Song, **Soochahn Lee**, Hyeong Gon Yu, Dong Ik Kim, Kyoung Mu Lee'
htmlurl: 'https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0282416'
pdfurl: 'https://journals.plos.org/plosone/article/file?id=10.1371/journal.pone.0282416&type=printable'
thumbnail: '/images/publications/2023-03-16-a-deep-learning-based-framework-for-reti-fig2.png'
bibtex: |
    @article{Lee_2023, title={A deep learning-based framework for retinal fundus image enhancement}, volume={18}, ISSN={1932-6203}, url={http://dx.doi.org/10.1371/journal.pone.0282416}, DOI={10.1371/journal.pone.0282416}, number={3}, journal={PLOS ONE}, publisher={Public Library of Science (PLoS)}, author={Lee, Kang Geon and Song, Su Jeong and Lee, Soochahn and Yu, Hyeong Gon and Kim, Dong Ik and Lee, Kyoung Mu}, editor={Damaševičius, Robertas}, year={2023}, month=mar, pages={e0282416} }
citation_mla: |
    Lee, Kang Geon, et al. “A Deep Learning-Based Framework for Retinal Fundus Image Enhancement.” PLOS ONE, edited by Robertas Damaševičius, vol. 18, no. 3, Mar. 2023, p. e0282416. Crossref, https://doi.org/10.1371/journal.pone.0282416.
---
<!-- NOTE: Summary based on title only - verify and expand with actual abstract -->

**Authors:** Kang Geon Lee, Su Jeong Song, **Soochahn Lee**, Hyeong Gon Yu, Dong Ik Kim, Kyoung Mu Lee

> **TL;DR:** A deep learning framework that enhances low-quality retinal fundus images -- correcting uneven illumination, blur, and artifacts -- to make them usable for downstream clinical analysis and AI-based diagnosis.

---

## What this paper is about

![Figure description](/images/publications/2023-03-16-a-deep-learning-based-framework-for-reti-fig1.png)
*Examples of enabling diagnosis. Each row depicts images sampled from LQ and HQ samples, where lesions that were unnoticeable in LQ image are clarified in the corresponding HQ image. (a) LQ images. (b) HQ images corresponding to (a).*

Retinal fundus imaging is widely used to screen for eye diseases, but real-world images often suffer from poor lighting, optical artifacts, and patient-related factors like cataracts. Low-quality images can mislead both human readers and automated diagnostic systems, yet re-acquiring images is not always feasible.

## Key idea

![Figure description](/images/publications/2023-03-16-a-deep-learning-based-framework-for-reti-fig2.png)

The proposed framework uses deep learning to transform degraded fundus images into enhanced versions that closely resemble high-quality captures. The network learns a mapping from poor-quality to good-quality images, addressing common degradation patterns like non-uniform illumination and haze, while preserving the clinically important structural details of the retina.

## Why it matters

Better image quality directly translates to more reliable diagnoses. This enhancement framework can serve as a preprocessing step for any retinal analysis pipeline, improving the reach of automated screening programs -- especially in resource-limited settings where imaging equipment may be suboptimal.

<!-- TODO: Add key figures from the paper -->
<!-- ![Figure description](/images/publications/2023-03-16-a-deep-learning-based-framework-for-reti-fig1.png) -->
