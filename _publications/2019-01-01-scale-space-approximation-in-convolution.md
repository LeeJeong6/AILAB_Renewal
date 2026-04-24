---
title: "Scale space approximation in convolutional neural networks for retinal vessel segmentation."
collection: publications
date: 2019-01-01
venue: 'Computer Methods and Programs in Biomedicine'
excerpt: '**Kyoung Jin Noh**, Sang Jun Park, **Soochahn Lee**'
pdfurl: 'https://drive.google.com/file/d/1UXaC02Ip-CjeBa4ln-R1kxa2X6pQjJfG/view'
htmlurl: 'https://www.sciencedirect.com/science/article/abs/pii/S0169260719302226'
thumbnail: '/images/publications/2019-01-01-scale-space-approximation-in-convolution-fig1.png'
bibtex: |
    @article{noh2019scale,
     abstract = {We present a novel and simple multi-scale convolutional neural network (CNN) structure  for retinal vessel segmentation. We first provide a theoretical analysis of existing multi-scale},
     author = {Noh, Kyoung Jin and Park, Sang Jun and Lee, Soochahn},
     journal = {Computer methods and programs in biomedicine},
     pages = {237--246},
     pub_year = {2019},
     publisher = {Elsevier},
     title = {Scale-space approximated convolutional neural networks for retinal vessel segmentation},
     venue = {Computer methods and programs in biomedicine},
     volume = {178}
    }
    
citation_mla: |
    Noh, Kyoung Jin, et al. "Scale space approximation in convolutional neural networks for retinal vessel segmentation.." Computer methods and programs in biomedicine, 2019.
---

<!-- NOTE: Summary based on title only - verify and expand with actual abstract -->

**Authors:** **Kyoung Jin Noh**, Sang Jun Park, **Soochahn Lee**

> **TL;DR:** A multi-scale CNN architecture for retinal vessel segmentation that incorporates scale-space theory to systematically handle vessels of different widths.

---

## What this paper is about

Retinal blood vessels come in a wide range of sizes -- from large arteries and veins down to tiny capillaries. Standard CNNs with fixed receptive fields struggle to detect vessels across all these scales simultaneously. This work addresses how to build scale awareness directly into the network architecture.

## Key idea

![Figure description](/images/publications/2019-01-01-scale-space-approximation-in-convolution-fig1.png)
*Comparison between (a) the structure for multi-scale feature generation of previous CNNs including those by Maninis et al. [19] and (b) the proposed multi-scale feature generation structure. The key difference is the insertion of upsampling layers, which adheres to the scale-space theory of Koenderink [11], Lindeberg [17] by better approximating the results of Gaussian blurring, and helps to give more accurate results.*

![Figure description](/images/publications/2019-01-01-scale-space-approximation-in-convolution-fig2.png)
*Visual summary of the structure of the proposed retinal scale-space approximated CNN (SSANet). By incorporating upsampling layers that approximate scale-space theory, distortions due to aliasing that may occur in the multi-scale feature generation are minimized, thereby improving the localization of vessel boundaries and segmentation of thin vessels. By also applying residual convolutional blocks of He et al. [8], the receptive field is maintained while and network capacity is increased.*

The method provides a theoretical analysis connecting classical scale-space theory with multi-scale CNN design, then proposes a simple yet effective network structure that approximates scale-space processing within the convolutional layers. This lets the network naturally respond to vessels at multiple scales without complex hand-designed multi-scale pipelines.

## Why it matters

![Figure description](/images/publications/2019-01-01-scale-space-approximation-in-convolution-fig3.png)
*Qualitative examples. From left to right, per column: original images, expert annotated ground truth vessel masks, results of DRIU [19], SSANet, and the highlighted differences between binarized vessel masks of DRIU and SSANet-3, respectively.*

Accurate segmentation of vessels at all scales is crucial for automated retinal disease screening. The principled scale-space approach provides a clean theoretical foundation for multi-scale CNN design that generalizes beyond retinal imaging.

