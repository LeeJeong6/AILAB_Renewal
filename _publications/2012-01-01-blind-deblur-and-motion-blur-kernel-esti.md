---
title: "Blind deblur and motion blur kernel estimation by parallel diffusion models"
collection: publications
date: 2012-01-01
venue: 'Workshop on Image Processing and Image Understanding (IPIU)'
excerpt: '**Joowan Maeng**, TaeHyun Kim, **Soochahn Lee**'
codeurl: 'https://github.com/JuWanMaeng/Motion_Deblur_Kernel_Estimation'
htmlurl: 'http://dx.doi.org/10.1016/j.proeng.2012.06.054'
bibtex: |
    @article{Govindan_2012, title={Fast Blur Kernel Estimation with Texture Preserving DRD for Motion Deblur}, volume={38}, ISSN={1877-7058}, url={http://dx.doi.org/10.1016/j.proeng.2012.06.054}, DOI={10.1016/j.proeng.2012.06.054}, journal={Procedia Engineering}, publisher={Elsevier BV}, author={Govindan, Sheena and Saravanakumar, S.}, year={2012}, pages={442–447} }
citation_mla: |
    Govindan, Sheena, and S. Saravanakumar. “Fast Blur Kernel Estimation with Texture Preserving DRD for Motion Deblur.” Procedia Engineering, vol. 38, 2012, pp. 442–47. Crossref, https://doi.org/10.1016/j.proeng.2012.06.054.
---

<!-- NOTE: Summary based on title only - verify and expand with actual abstract -->

**Authors:** **Joowan Maeng**, TaeHyun Kim, **Soochahn Lee**

> **TL;DR:** A blind image deblurring method that estimates motion blur kernels using parallel diffusion models, enabling sharp image recovery without knowing the blur pattern in advance.

---

## What this paper is about

When a camera or subject moves during exposure, the resulting image is blurred by an unknown motion kernel. Blind deblurring aims to recover both the sharp image and the blur kernel simultaneously, which is a highly ill-posed problem.

## Key idea

The paper leverages parallel diffusion models to jointly estimate motion blur kernels and perform blind deblurring. By running diffusion processes in parallel for both the kernel and the latent sharp image, the method can disentangle the blur from the image content effectively.

## Why it matters

Motion blur is one of the most common causes of image degradation in everyday photography. This work brings modern generative modeling techniques to bear on a classical image restoration problem, with code available on GitHub for reproducibility.

<!-- TODO: Add key figures from the paper -->
<!-- ![Figure description](/images/publications/2012-01-01-blind-deblur-and-motion-blur-kernel-esti-fig1.png) -->
