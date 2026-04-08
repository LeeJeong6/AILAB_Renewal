---
title: "Topology-aware retinal artery–vein classification via deep vascular connectivity prediction."
collection: publications
date: 2020-12-31
venue: 'Applied Sciences'
excerpt: 'Seung Yeon Shin, **Soochahn Lee**, Il Dong Yun, Kyoung Mu Lee'
htmlurl: 'https://www.mdpi.com/2076-3417/11/1/320'
bibtex: |
    @article{Shin_2020, title={Topology-Aware Retinal Artery–Vein Classification via Deep Vascular Connectivity Prediction}, volume={11}, ISSN={2076-3417}, url={http://dx.doi.org/10.3390/app11010320}, DOI={10.3390/app11010320}, number={1}, journal={Applied Sciences}, publisher={MDPI AG}, author={Shin, Seung Yeon and Lee, Soochahn and Yun, Il Dong and Lee, Kyoung Mu}, year={2020}, month=dec, pages={320} }
citation_mla: |
    Shin, Seung Yeon, et al. “Topology-Aware Retinal Artery–Vein Classification via Deep Vascular Connectivity Prediction.” Applied Sciences, vol. 11, no. 1, Dec. 2020, p. 320. Crossref, https://doi.org/10.3390/app11010320.
---

<!-- NOTE: Summary based on title only - verify and expand with actual abstract -->

**Authors:** Seung Yeon Shin, **Soochahn Lee**, Il Dong Yun, Kyoung Mu Lee

> **TL;DR:** A topology-aware approach to retinal artery-vein classification that uses deep vascular connectivity prediction to ensure consistent labeling along connected vessel segments.

---

## What this paper is about

Classifying retinal vessels as arteries or veins is important for diagnosing cardiovascular and eye diseases. However, standard pixel-wise classification methods often produce inconsistent labels along connected vessel segments -- the same vessel branch might flip between artery and vein labels, which is anatomically impossible.

## Key idea

The method incorporates vascular connectivity prediction into the classification pipeline. By predicting how vessel segments are connected in the vascular graph and enforcing topological consistency, the network ensures that artery/vein labels propagate coherently along each vessel branch, eliminating anatomically implausible label switches.

## Why it matters

Topology-aware classification produces clinically meaningful artery/vein maps that respect the underlying vascular anatomy, making the results more trustworthy for downstream clinical analysis such as arteriovenous ratio measurement.

<!-- TODO: Add key figures from the paper -->
<!-- ![Figure description](/images/publications/2020-12-31-topology-aware-retinal-artery-vein-class-fig1.png) -->
