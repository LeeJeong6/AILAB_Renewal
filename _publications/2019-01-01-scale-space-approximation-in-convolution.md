---
title: "Scale space approximation in convolutional neural networks for retinal vessel segmentation."
collection: publications
date: 2019-01-01
venue: 'Computer Methods and Programs in Biomedicine'
excerpt: '**Kyoung Jin Noh**, Sang Jun Park, **Soochahn Lee**'
pdfurl: 'https://drive.google.com/file/d/1UXaC02Ip-CjeBa4ln-R1kxa2X6pQjJfG/view'
htmlurl: 'https://www.sciencedirect.com/science/article/abs/pii/S0169260719302226'
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

The method provides a theoretical analysis connecting classical scale-space theory with multi-scale CNN design, then proposes a simple yet effective network structure that approximates scale-space processing within the convolutional layers. This lets the network naturally respond to vessels at multiple scales without complex hand-designed multi-scale pipelines.

## Why it matters

Accurate segmentation of vessels at all scales is crucial for automated retinal disease screening. The principled scale-space approach provides a clean theoretical foundation for multi-scale CNN design that generalizes beyond retinal imaging.

<!-- TODO: Add key figures from the paper -->
<!-- ![Figure description](/images/publications/2019-01-01-scale-space-approximation-in-convolution-fig1.png) -->
