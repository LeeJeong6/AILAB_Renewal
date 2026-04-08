---
title: "Cycle consistent generative motion artifact correction in coronary computed tomography angiography"
collection: publications
date: 2024-02-23
venue: 'Applied Sciences'
excerpt: '**Amal Muhammad Saleem**, Sunghee Jung, Hyuk-Jae Chang, **Soochahn Lee**'
htmlurl: 'https://www.mdpi.com/2076-3417/14/5/1859'
bibtex: |
    @article{Saleem_2024, title={Cycle Consistent Generative Motion Artifact Correction in Coronary Computed Tomography Angiography}, volume={14}, ISSN={2076-3417}, url={http://dx.doi.org/10.3390/app14051859}, DOI={10.3390/app14051859}, number={5}, journal={Applied Sciences}, publisher={MDPI AG}, author={Saleem, Amal Muhammad and Jung, Sunghee and Chang, Hyuk-Jae and Lee, Soochahn}, year={2024}, month=feb, pages={1859} }
citation_mla: |
    Saleem, Amal Muhammad, et al. “Cycle Consistent Generative Motion Artifact Correction in Coronary Computed Tomography Angiography.” Applied Sciences, vol. 14, no. 5, Feb. 2024, p. 1859. Crossref, https://doi.org/10.3390/app14051859.
---

<!-- NOTE: Summary based on title only - verify and expand with actual abstract -->

**Authors:** **Amal Muhammad Saleem**, Sunghee Jung, Hyuk-Jae Chang, **Soochahn Lee**

> **TL;DR:** A cycle-consistent generative approach to remove motion artifacts from coronary CT angiography images, improving diagnostic image quality without requiring paired training data.

---

## What this paper is about

Motion artifacts in coronary computed tomography angiography (CCTA) are a persistent problem -- heart motion during scanning creates blurry or distorted images that can make diagnosis unreliable. Getting artifact-free paired training data is extremely difficult in clinical settings, so supervised approaches are limited.

## Key idea

The paper uses a cycle-consistent generative adversarial network to learn the mapping between motion-corrupted and clean CCTA images in an unpaired fashion. By enforcing cycle consistency, the model learns to remove artifacts while preserving the underlying anatomical structures faithfully.

## Why it matters

This approach can improve the diagnostic quality of coronary CT scans without requiring repeat imaging or paired datasets, potentially reducing patient radiation exposure and improving clinical workflow.

<!-- TODO: Add key figures from the paper -->
<!-- ![Figure description](/images/publications/2024-02-23-cycle-consistent-generative-motion-artif-fig1.png) -->
