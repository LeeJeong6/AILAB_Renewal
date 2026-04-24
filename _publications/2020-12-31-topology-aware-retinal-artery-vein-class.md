---
title: "Topology-aware retinal artery–vein classification via deep vascular connectivity prediction."
collection: publications
date: 2020-12-31
venue: 'Applied Sciences'
excerpt: 'Seung Yeon Shin, **Soochahn Lee**, Il Dong Yun, Kyoung Mu Lee'
htmlurl: 'https://www.mdpi.com/2076-3417/11/1/320'
pdfurl: 'https://www.mdpi.com/2076-3417/11/1/320/pdf?version=1609392765' 
thumbnail: '/images/publications/2020-12-31-topology-aware-retinal-artery-vein-class-fig1.png'
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

![Figure description](/images/publications/2020-12-31-topology-aware-retinal-artery-vein-class-fig1.png)
*Illustration of our topology-aware retinal artery–vein (AV) classification method, where estimated vessel topology is used to perform tree-wise AV classification. Red and blue colors represent classified arteries and veins, respectively. Different colors in the estimated topology map represent separate sub-trees. Tree-wise AV classification is used to correct the pixelwise classification errors on thin vessels, highlighted by white circles, which may occur due to their indistinct appearances.*

Classifying retinal vessels as arteries or veins is important for diagnosing cardiovascular and eye diseases. However, standard pixel-wise classification methods often produce inconsistent labels along connected vessel segments -- the same vessel branch might flip between artery and vein labels, which is anatomically impossible.

## Key idea

![Figure description](/images/publications/2020-12-31-topology-aware-retinal-artery-vein-class-fig2.png)
*Block diagram of the proposed method for AV classification at test time. Pixelwise prediction on the optic disc and vessel, graph construction, topology estimation, and the final AV classification are sequentially performed. Each block is also composed of several parallel or sequential steps. The arrows denote information flow. Gray-color boxes represent steps where the trained networks are involved. The thickness/orientation classifications are auxiliary tasks for the connectivity classification, and their relationship is not represented here. Please refer to the paper for details.*

The method incorporates vascular connectivity prediction into the classification pipeline. By predicting how vessel segments are connected in the vascular graph and enforcing topological consistency, the network ensures that artery/vein labels propagate coherently along each vessel branch, eliminating anatomically implausible label switches.

## Why it matters

![Figure description](/images/publications/2020-12-31-topology-aware-retinal-artery-vein-class-fig3.png)
*example results from the CT-DRIVE dataset. The six images for a single case are, in row-major order beginning from the top-left, the original input image, estimated topology of the proposed method, GT annotation of the topology, pixelwise AV classification result, tree-wise classification result of the proposed method, and AV GT annotation. Different colors in the topology GT represent separate trees. In each result, correctly classified arteries and veins are marked as red and blue, respectively. Centerlines incorrectly labeled as veins are in green, while those incorrectly labeled as arteries are in yellow.*

Topology-aware classification produces clinically meaningful artery/vein maps that respect the underlying vascular anatomy, making the results more trustworthy for downstream clinical analysis such as arteriovenous ratio measurement.

