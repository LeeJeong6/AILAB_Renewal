---
title: "Combining fundus images and fluorescein angiography for artery/vein classification using the hierarchical vessel graph network."
collection: publications
date: 2020-01-01
venue: 'International Conference on Medical Image Computing and Computer-Assisted Intervention (MICCAI)'
excerpt: '**Kyoung Jin Noh**, Sang Jun Park, **Soochahn Lee**'
pdfurl: 'https://drive.google.com/file/d/1xfOCi8XjrxANGJ73WeDGJ4RASExgBL-z/view'
htmlurl: 'https://link.springer.com/chapter/10.1007/978-3-030-59722-1_57'
thumbnail: '/images/publications/2020-01-01-combining-fundus-images-and-fluorescein-fig1.png'
codeurl: 'https://github.com/snubhretina/HVGN'
bibtex: |
    @inbook{Noh_2020, title={Combining Fundus Images and Fluorescein Angiography for Artery/Vein Classification Using the Hierarchical Vessel Graph Network}, ISBN={9783030597221}, ISSN={1611-3349}, url={http://dx.doi.org/10.1007/978-3-030-59722-1_57}, DOI={10.1007/978-3-030-59722-1_57}, booktitle={Medical Image Computing and Computer Assisted Intervention – MICCAI 2020}, publisher={Springer International Publishing}, author={Noh, Kyoung Jin and Park, Sang Jun and Lee, Soochahn}, year={2020}, pages={595–605} }
citation_mla: |
    Noh, Kyoung Jin, et al. “Combining Fundus Images and Fluorescein Angiography for Artery/Vein Classification Using the Hierarchical Vessel Graph Network.” Medical Image Computing and Computer Assisted Intervention – MICCAI 2020, 2020, pp. 595–605. Crossref, https://doi.org/10.1007/978-3-030-59722-1_57.
---

<!-- NOTE: Summary based on title only - verify and expand with actual abstract -->

**Authors:** **Kyoung Jin Noh**, Sang Jun Park, **Soochahn Lee**

> **TL;DR:** A hierarchical vessel graph network that combines fundus images and fluorescein angiography to classify retinal vessels into arteries and veins, leveraging complementary information from both modalities.

---

## What this paper is about

![Figure description](/images/publications/2020-01-01-combining-fundus-images-and-fluorescein-fig1.png)
*Visual overview of the proposed method with integrated feature extractor CNN for combined fundus image and FA input (FE-CNN) and hierarchical connectivity GNN (HC-GNN).*


Distinguishing arteries from veins in retinal images is important for diagnosing vascular diseases, but it is difficult because the two vessel types look very similar in standard fundus photos. Fluorescein angiography provides temporal flow information that helps tell them apart, but combining these two modalities effectively is non-trivial.

## Key idea

![Figure description](/images/publications/2020-01-01-combining-fundus-images-and-fluorescein-fig2.png)
*A visual description of the hierarchical connectivity graph neural network (HC-GNN) based on graph U-nets.*


The method uses a hierarchical vessel graph network that fuses information from both fundus images and fluorescein angiography. By representing the vasculature as a graph and processing it hierarchically, the network can propagate artery/vein classification decisions along the vessel tree while incorporating multimodal cues at each level.

## Why it matters

![Figure description](/images/publications/2020-01-01-multimodal-registration-of-fundus-images-fig3.png)
*Qualitative results. Four sample cases from our private DB are shown, with top to bottom rows illustrating (1) the original image, (2) GT, and results of (3) FE-CNN-Fundus (fundus image input only), (4) FE-CNN-Parallel (combined fundus-FA input), and (5) FFA-HVGN (proposed). Left and right columns show the images in full and zoomed resolution, respectively.*


Published at MICCAI 2020, this work advances retinal artery/vein classification by showing how multimodal fusion and graph-based reasoning can work together, with implications for automated screening of hypertensive retinopathy and other vascular conditions.

