---
title: "Fingerprint liveness detection by a template-probe convolutional neural network."
collection: publications
date: 2019-01-01
venue: 'IEEE Access'
excerpt: 'Ho Yub Jung, Yong Seok Heo, **Soochahn Lee**'
htmlurl: 'https://ieeexplore.ieee.org/document/8809706'
bibtex: |
    @article{Jung_2019, title={Fingerprint Liveness Detection by a Template-Probe Convolutional Neural Network}, volume={7}, ISSN={2169-3536}, url={http://dx.doi.org/10.1109/access.2019.2936890}, DOI={10.1109/access.2019.2936890}, journal={IEEE Access}, publisher={Institute of Electrical and Electronics Engineers (IEEE)}, author={Jung, Ho Yub and Heo, Yong Seok and Lee, Soochahn}, year={2019}, pages={118986–118993} }
citation_mla: |
    Jung, Ho Yub, et al. “Fingerprint Liveness Detection by a Template-Probe Convolutional Neural Network.” IEEE Access, vol. 7, 2019, pp. 118986–93. Crossref, https://doi.org/10.1109/access.2019.2936890.
---

<!-- NOTE: Summary based on title only - verify and expand with actual abstract -->

**Authors:** Ho Yub Jung, Yong Seok Heo, **Soochahn Lee**

> **TL;DR:** A CNN-based fingerprint liveness detection method that compares a template fingerprint with a probe fingerprint to determine whether the probe is from a real finger or a spoof.

---

## What this paper is about

Fingerprint-based authentication systems are vulnerable to spoofing attacks using fake fingerprints made from materials like silicone or gelatin. Liveness detection -- telling apart real fingers from fakes -- is critical for securing these systems. Existing approaches often analyze a single fingerprint image in isolation.

## Key idea

Instead of looking at a single fingerprint, this method uses a template-probe CNN architecture that jointly analyzes both a stored template fingerprint and the newly captured probe fingerprint. By learning the relationship between the two, the network can better detect subtle differences that indicate whether the probe comes from a live finger or an artificial replica.

## Why it matters

This pairwise comparison approach provides a more robust liveness detection mechanism, making fingerprint authentication systems harder to fool with spoofed prints.

<!-- TODO: Add key figures from the paper -->
<!-- ![Figure description](/images/publications/2019-01-01-fingerprint-liveness-detection-by-a-temp-fig1.png) -->
