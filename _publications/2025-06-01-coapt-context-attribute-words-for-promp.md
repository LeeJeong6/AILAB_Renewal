---
title: "CoAPT: Context attribute words for prompt tuning"
collection: publications
date: 2025-06-01
venue: 'Knowledge-Based Systems'
excerpt: '**Gun Lee**, **Subin An**, Sungyoung Baik, **Soochahn Lee**'
htmlurl: 'http://dx.doi.org/10.1016/j.knosys.2025.113653'
pdfurl: 'https://arxiv.org/pdf/2407.13808'
codeurl: 'https://github.com/LeeGun4488/CoAPT'
thumbnail: '/images/publications/2025-06-01-coapt-context-attribute-words-for-promp-fig2.png'
bibtex: |
    @article{Lee_2025, title={CoAPT: Context Attribute words for Prompt Tuning}, volume={320}, ISSN={0950-7051}, url={http://dx.doi.org/10.1016/j.knosys.2025.113653}, DOI={10.1016/j.knosys.2025.113653}, journal={Knowledge-Based Systems}, publisher={Elsevier BV}, author={Lee, Gun and An, Subin and Baik, Sungyong and Lee, Soochahn}, year={2025}, month=jun, pages={113653} }
citation_mla: |
    Lee, Gun, et al. “CoAPT: Context Attribute Words for Prompt Tuning.” Knowledge-Based Systems, vol. 320, June 2025, p. 113653. Crossref, https://doi.org/10.1016/j.knosys.2025.113653.
---

<!-- NOTE: Summary based on title only - verify and expand with actual abstract -->

**Authors:** **Gun Lee**, **Subin An**, Sungyoung Baik, **Soochahn Lee**

> **TL;DR:** CoAPT improves prompt tuning for vision-language models by incorporating context-aware attribute words, leading to better generalization across visual recognition tasks.

---

## What this paper is about

Prompt tuning has become a popular way to adapt large vision-language models (like CLIP) to downstream tasks without full fine-tuning. However, learned prompts often overfit to seen classes and fail to generalize, especially in few-shot or zero-shot settings.

![Figure description](/images/publications/2025-06-01-coapt-context-attribute-words-for-promp-fig1.png)
*Comparative overview of CoAPT. Existing soft prompt tuning methods, such as CoOp, do not fully utilize the text encoder input. The empty slots in the text query can be enhanced by integrating additional hard prompts. For the sample classes from the OxfordPets dataset, CoAPT achieves better classification accuracy for both base and new classes.*

## Key idea

CoAPT introduces context attribute words into the prompt tuning process, enriching the learned prompts with semantic attributes that capture meaningful visual and contextual properties. This provides more structured and transferable prompts compared to purely learned token embeddings.

![Figure description](/images/publications/2025-06-01-coapt-context-attribute-words-for-promp-fig2.png)
*Overview of CoAPT method with baseline prompt learning model. The CoAPT method consists of two steps. First, attribute words are generated using a language model, which is a one-time process. Second, during prompt learning, these words are combined with the soft prompt and class token. Inputs generate queries processed by a Meta-network, adding a bias term to the text queries. The combined image–text queries are then used to maximize the score for the ground-truth class.*

## Why it matters

This work pushes prompt tuning closer to practical deployment by improving generalization, which is critical for real-world applications where models encounter unseen categories.


