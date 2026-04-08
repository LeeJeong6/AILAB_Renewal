---
title: "Fully leveraging deep learning methods for constructing retinal fundus photomontages."
collection: publications
date: 2021-02-16
venue: 'Applied Sciences'
excerpt: '**Jooyoung Kim**, **Sojung Go**, **Kyoung Jin Noh**, Sang Jun Park, **Soochahn Lee**'
codeurl: 'https://github.com/snubhretina/Montage'
htmlurl: 'https://www.mdpi.com/2076-3417/11/4/1754'
bibtex: |
    @article{Kim_2021, title={Fully Leveraging Deep Learning Methods for Constructing Retinal Fundus Photomontages}, volume={11}, ISSN={2076-3417}, url={http://dx.doi.org/10.3390/app11041754}, DOI={10.3390/app11041754}, number={4}, journal={Applied Sciences}, publisher={MDPI AG}, author={Kim, Jooyoung and Go, Sojung and Noh, Kyoung Jin and Park, Sang Jun and Lee, Soochahn}, year={2021}, month=feb, pages={1754} }
citation_mla: |
    Kim, Jooyoung, et al. “Fully Leveraging Deep Learning Methods for Constructing Retinal Fundus Photomontages.” Applied Sciences, vol. 11, no. 4, Feb. 2021, p. 1754. Crossref, https://doi.org/10.3390/app11041754.
---
<!-- NOTE: Summary based on title only - verify and expand with actual abstract -->

**Authors:** **Jooyoung Kim**, **Sojung Go**, **Kyoung Jin Noh**, Sang Jun Park, **Soochahn Lee**

> **TL;DR:** A fully deep-learning-based pipeline for automatically stitching multiple retinal fundus photographs into a single wide-field photomontage, replacing traditional feature-matching heuristics with learned representations.

---

## What this paper is about

Retinal fundus cameras capture only a limited field of view, so clinicians often need to mentally piece together several snapshots to see the full retina. Building a seamless photomontage from these narrow-field images has traditionally relied on hand-crafted feature matching, which struggles with the low-contrast, repetitive textures of the retina.

## Key idea

This work replaces the conventional montage construction pipeline with end-to-end deep learning methods. The approach leverages deep networks for both image registration (aligning overlapping fundus photos) and blending (stitching them into a single coherent mosaic), fully automating the process without manual landmark selection.

## Why it matters

Automated wide-field montages give ophthalmologists a comprehensive view of the retina in one image, improving diagnostic efficiency for diseases like diabetic retinopathy and retinal detachment -- especially in clinics that lack expensive ultra-widefield cameras.

<!-- TODO: Add key figures from the paper -->
<!-- ![Figure description](/images/publications/2021-02-16-fully-leveraging-deep-learning-methods-f-fig1.png) -->
