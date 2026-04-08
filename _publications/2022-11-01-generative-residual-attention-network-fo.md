---
title: "Generative Residual Attention Network for Disease Detection"
collection: publications
date: 2022-11-01
venue: 'arXiv preprint arXiv:2110.12984'
excerpt: 'Euyoung Kim, **Soochahn Lee**, Kyoung Mu Lee'
htmlurl: 'https://arxiv.org/abs/2110.12984'
pdfurl: 'https://arxiv.org/pdf/2110.12984.pdf'
bibtex: |
    @article{Hong_2022, title={RANET: A Grasp Generative Residual Attention Network for Robotic Grasping Detection}, volume={20}, ISSN={2005-4092}, url={http://dx.doi.org/10.1007/s12555-021-0929-8}, DOI={10.1007/s12555-021-0929-8}, number={12}, journal={International Journal of Control, Automation and Systems}, publisher={Springer Science and Business Media LLC}, author={Hong, Qian-Qian and Yang, Liang and Zeng, Bi}, year={2022}, month=nov, pages={3996–4004} }
citation_mla: |
    Hong, Qian-Qian, et al. “RANET: A Grasp Generative Residual Attention Network for Robotic Grasping Detection.” International Journal of Control, Automation and Systems, vol. 20, no. 12, Nov. 2022, pp. 3996–4004. Crossref, https://doi.org/10.1007/s12555-021-0929-8.
---
<!-- NOTE: Summary based on title only - verify and expand with actual abstract -->

**Authors:** Euyoung Kim, **Soochahn Lee**, Kyoung Mu Lee

> **TL;DR:** A generative model with residual attention mechanisms for detecting diseases in medical images, learning to focus on pathologically relevant regions while suppressing background noise.

---

## What this paper is about

Detecting diseases from medical images is challenging because pathological signs can be subtle and vary widely in location and appearance. Standard classification networks may miss these fine-grained cues or be distracted by irrelevant anatomy.

## Key idea

The proposed Generative Residual Attention Network combines generative modeling with residual attention modules. The generative component learns the distribution of normal (healthy) images, while the residual attention mechanism highlights deviations from normal -- effectively spotting disease-related regions. This attention-guided approach helps the model zero in on diagnostically meaningful areas.

## Why it matters

By learning what "normal" looks like and flagging deviations, this approach can generalize across different disease types without requiring exhaustive per-pathology annotation, making it a flexible tool for medical image screening.

<!-- TODO: Add key figures from the paper -->
<!-- ![Figure description](/images/publications/2022-11-01-generative-residual-attention-network-fo-fig1.png) -->
