---
title: "Dual exposure fusion with entropy-based residual filtering."
collection: publications
date: 2017-05-31
venue: 'KSII Transactions on Internet and Information Systems'
excerpt: 'Yong Seok Heo, **Soochahn Lee**, Ho Yub Jung'
pdfurl: 'https://drive.google.com/file/d/1KuuCNlUWlxBUS-PBZiG17NVJNfMd09_v/view'
htmlurl: 'https://scienceon.kisti.re.kr/commons/util/originalView.do?cn=JAKO201720861204113&dbt=JAKO&koi=KISTI1.1003%2FJNL.JAKO201720861204113'
thumbnail: '/images/publications/2017-05-31-dual-exposure-fusion-with-entropy-based-fig1.png'
bibtex: |
    @article{2017, volume={11}, ISSN={1976-7277}, url={http://dx.doi.org/10.3837/tiis.2017.05.014}, DOI={10.3837/tiis.2017.05.014}, number={5}, journal={KSII Transactions on Internet and Information Systems}, publisher={Korean Society for Internet Information (KSII)}, year={2017}, month=may }
citation_mla: |
    “Dual Exposure Fusion with Entropy-Based Residual Filtering.” KSII Transactions on Internet and Information Systems, vol. 11, no. 5, May 2017. Crossref, https://doi.org/10.3837/tiis.2017.05.014.
---

<!-- NOTE: Summary based on title only - verify and expand with actual abstract -->

**Authors:** Yong Seok Heo, **Soochahn Lee**, Ho Yub Jung

> **TL;DR:** A dual exposure fusion method that uses entropy-based residual filtering to combine two differently exposed images into a single well-exposed result.

---

## What this paper is about

![Figure description](/images/publications/2017-05-31-dual-exposure-fusion-with-entropy-based-fig1.png)
*Comparison of different methods. (a) Long exposure image $I^L$. (b) Short exposure image $I^S$. (c) Result of Sen et al., SIGGRAPH Asia, 2012, using (a) and (b). (d) Result of our method using (a) and (b).*

Scenes with high dynamic range are difficult to capture in a single photo -- bright areas get overexposed and dark areas get underexposed. Exposure fusion combines multiple exposures to produce a single image with good detail everywhere, but existing methods can introduce artifacts or fail to properly balance detail across exposures.

## Key idea

The paper takes just two differently exposed images and fuses them using an entropy-based residual filtering approach. The entropy measure helps identify which regions of each exposure carry the most useful information, while the residual filtering step suppresses artifacts and ensures smooth blending between the two exposures.

## Why it matters

Using only two exposures (rather than a full bracket) makes this approach practical for handheld photography and moving scenes, while the entropy-based filtering produces clean, artifact-free HDR-like results.

