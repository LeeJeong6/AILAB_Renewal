---
title: "Particle Diffusion Matching: Random Walk Correspondence Search for the Alignment of Standard and Ultra-Widefield Fundus Images"
collection: publications
date: 2026-01-01
venue: 'IEEE Transactions on Image Processing'
excerpt: 'Kang Geon Lee, **Soochahn Lee**, Kyoung Mu Lee'
thumbnail: '/images/publications/2026-01-01-particle-diffusion-matching-random-walk-fig2.png'
htmlurl: 'https://doi.org/10.1109/TIP.2026.3653198'
bibtex: |
    @article{lee2026particle,
      title={Particle Diffusion Matching: Random Walk Correspondence Search for the Alignment of Standard and Ultra-Widefield Fundus Images},
      author={Lee, Kang Geon and Lee, Soochahn and Lee, Kyoung Mu},
      journal={IEEE Transactions on Image Processing},
      volume={35},
      year={2026},
      month=jan,
      publisher={IEEE}
    }
citation_mla: |
    Lee, Kang Geon, **Soochahn Lee**, and Kyoung Mu Lee. "Particle Diffusion Matching: Random Walk Correspondence Search for the Alignment of Standard and Ultra-Widefield Fundus Images." IEEE Transactions on Image Processing 35 (2026).
---

<!-- NOTE: Summary based on title only - verify and expand with actual abstract -->

**Authors:** Kang Geon Lee, **Soochahn Lee**, Kyoung Mu Lee

> **TL;DR:** Particle Diffusion Matching uses random walk-based correspondence search to align standard fundus images with ultra-widefield fundus images, handling the extreme field-of-view and distortion differences between the two modalities.

---

## What this paper is about

Aligning standard fundus photographs with ultra-widefield (UWF) fundus images is challenging because UWF images cover a much larger retinal area with significant geometric distortion. Traditional registration methods struggle with the scale difference, non-linear distortions, and varying image content between these two capture types.

![Figure description](/images/publications/2026-01-01-particle-diffusion-matching-random-walk-fig1.png)
*Particle Diﬀusion Matching (PDM). PDM can align Standard Fundus Images (SFIs) and Ultra-Widefield Fundus Images (UWFIs), which may have extreme diﬀerences in view and scale (The resolutions of UWFI and SFI here are approximately 2600 ×2000 and 3600 ×3600, respectively.). In PDM, a particle is defined as a point pair comprising a keypoint from the SFI and a potential matching point from the UWFI. UWFI points are initialized as random Gaussian points at t = T , (bottom left) and undergo random walk correspondence search (RWCS) to eventually reach the matching points (bottom middle) to the paired SFI points (bottom right). The random walk trajectories of four sample particles have been highlighted in various colors.*

## Key idea

The paper proposes Particle Diffusion Matching, which formulates correspondence search as a random walk process inspired by particle diffusion. This stochastic search strategy explores the correspondence space more effectively than deterministic methods, finding reliable matches even under large geometric and appearance variations.

![Figure description](/images/publications/2026-01-01-particle-diffusion-matching-random-walk-fig2.png)
*Random Walk Correspondence Search (RWCS). Particles are defined as pairs of points from SFI and UWFI, respectively. Particle random walks at sample steps t + 1, t, and t−1 are depicted. Particle with correct and incorrect correspondences are marked by green and red lines, respectively. The bottom row depicts particles at one-third intervals of the entire sampling process.*

## Why it matters

PDM is a general-purpose iterative random walk framework that unifies global and local alignment through a stochastic search process, progressively refining transformations to handle both large-scale misalignment and fine-grained local deformations. While demonstrated on the challenging task of aligning standard fundus images with ultra-widefield fundus images, the approach is broadly applicable to general photograph matching problems involving significant geometric and appearance variations. 

![Figure description](/images/publications/2026-01-01-particle-diffusion-matching-random-walk-fig3.png)
*Qualitative evaluation of PDM on the KBSMC, FIRE, and FLORI21 datasets.*

![Figure description](/images/publications/2026-01-01-particle-diffusion-matching-random-walk-fig4.png)
*Qualitative evaluation of PDM on the HPatches, MegaDepth, and ScanNet datasets.*


<!-- TODO: Add key figures from the paper -->
