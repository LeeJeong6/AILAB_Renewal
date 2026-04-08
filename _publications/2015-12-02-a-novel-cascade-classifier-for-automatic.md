---
title: "A novel cascade classifier for automatic microcalcification detection."
collection: publications
date: 2015-12-02
venue: 'PLoS ONE'
excerpt: 'Seung Yeon Shin, **Soochahn Lee**, Il Dong Yun, Ho Yub Jung, Yong Seok Heo, Sun Mi Kim, Kyoung Mu Lee'
htmlurl: 'https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0143725'
bibtex: |
    @article{Shin_2015, title={A Novel Cascade Classifier for Automatic Microcalcification Detection}, volume={10}, ISSN={1932-6203}, url={http://dx.doi.org/10.1371/journal.pone.0143725}, DOI={10.1371/journal.pone.0143725}, number={12}, journal={PLOS ONE}, publisher={Public Library of Science (PLoS)}, author={Shin, Seung Yeon and Lee, Soochahn and Yun, Il Dong and Jung, Ho Yub and Heo, Yong Seok and Kim, Sun Mi and Lee, Kyoung Mu}, editor={Deng, Zhaohong}, year={2015}, month=dec, pages={e0143725} }
citation_mla: |
    Shin, Seung Yeon, et al. “A Novel Cascade Classifier for Automatic Microcalcification Detection.” PLOS ONE, edited by Zhaohong Deng, vol. 10, no. 12, Dec. 2015, p. e0143725. Crossref, https://doi.org/10.1371/journal.pone.0143725.
---

<!-- NOTE: Summary based on title only - verify and expand with actual abstract -->

**Authors:** Seung Yeon Shin, **Soochahn Lee**, Il Dong Yun, Ho Yub Jung, Yong Seok Heo, Sun Mi Kim, Kyoung Mu Lee

> **TL;DR:** A novel cascade classifier architecture for automatically detecting microcalcifications in mammograms, improving both detection sensitivity and computational efficiency.

---

## What this paper is about

Microcalcifications are tiny calcium deposits in breast tissue that can be early signs of cancer. Detecting them automatically in mammograms is hard because they are small, low-contrast, and easily confused with noise or other structures.

## Key idea

The paper designs a cascade classifier that progressively filters out non-calcification regions at each stage, allowing later stages to focus computational effort on the most promising candidates. This cascade structure balances high sensitivity (catching real calcifications) with low false positive rates by using increasingly sophisticated classifiers at each level.

## Why it matters

The cascade design achieves strong detection performance while remaining computationally efficient, making it practical for integration into clinical computer-aided detection systems for breast cancer screening.

<!-- TODO: Add key figures from the paper -->
<!-- ![Figure description](/images/publications/a-novel-cascade-classifier-for-automatic-fig1.png) -->
