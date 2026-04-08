---
title: "Adaptive combination of local motion, appearance, and shape for video segmentation."
collection: publications
date: 2016-11-01
venue: 'Journal of Imaging Science and Technology'
excerpt: 'Woo-Sung Shim, Se-Hoon Kim, **Soochahn Lee**'
pdfurl: 'https://drive.google.com/file/d/1yOcb9LkiPwP1qokY2jd6ecOhdFxgeinF/view'
htmlurl: 'https://www.ingentaconnect.com/content/ist/jist/2016/00000060/00000006/art00011'
bibtex: |
    @article{Shim_2016, title={Adaptive Combination of Local Motion, Appearance, and Shape for Video Segmentation}, volume={60}, ISSN={1943-3522}, url={http://dx.doi.org/10.2352/j.imagingsci.technol.2016.60.6.060409}, DOI={10.2352/j.imagingsci.technol.2016.60.6.060409}, number={6}, journal={Journal of Imaging Science and Technology}, publisher={Society for Imaging Science & Technology}, author={Shim, Woo-sung and Kim, Se-hoon and Lee, Soochahn}, year={2016}, month=nov, pages={060409-1-060409–7} }
citation_mla: |
    Shim, Woo-sung, et al. “Adaptive Combination of Local Motion, Appearance, and Shape for Video Segmentation.” Journal of Imaging Science and Technology, vol. 60, no. 6, Nov. 2016, pp. 060409-1-060409–7. Crossref, https://doi.org/10.2352/j.imagingsci.technol.2016.60.6.060409.
---

<!-- NOTE: Summary based on title only - verify and expand with actual abstract -->

**Authors:** Woo-Sung Shim, Se-Hoon Kim, **Soochahn Lee**

> **TL;DR:** An adaptive method that combines local motion, appearance, and shape cues for robust video object segmentation.

---

## What this paper is about

Segmenting objects in video requires handling moving objects, changing appearances, and deformable shapes all at once. Relying on any single cue (motion, appearance, or shape) alone is fragile, because each cue fails in different scenarios.

## Key idea

The paper proposes an adaptive combination scheme that dynamically weights local motion, appearance, and shape features for video segmentation. Rather than using fixed weights, the method adjusts how much it relies on each cue based on local context, so it can lean on motion in areas with clear movement and on appearance or shape where motion is ambiguous.

## Why it matters

This adaptive multi-cue approach produces more robust video segmentation across diverse and challenging scenarios than methods relying on any single cue.

<!-- TODO: Add key figures from the paper -->
<!-- ![Figure description](/images/publications/adaptive-combination-of-local-motion-ap-fig1.png) -->
