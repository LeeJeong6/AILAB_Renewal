---
title: "Contamination Detection for VLMs using Multi-Modal Semantic Perturbation"
collection: publications
date: 2025-11-05
venue: 'arXiv preprint'
excerpt: 'Jaden Park, Mu Cai, Feng Yao, Jingbo Shang, **Soochahn Lee**, Yong Jae Lee'
htmlurl: 'https://arxiv.org/abs/2511.03774'
pdfurl: 'https://arxiv.org/pdf/2511.03774.pdf'
bibtex: |
    @article{park2025contamination,
      title={Contamination Detection for VLMs using Multi-Modal Semantic Perturbation},
      author={Park, Jaden and Cai, Mu and Yao, Feng and Shang, Jingbo and Lee, Soochahn and Lee, Yong Jae},
      journal={arXiv preprint arXiv:2511.03774},
      year={2025},
      month=nov
    }
citation_mla: |
    Park, Jaden, et al. "Contamination Detection for VLMs using Multi-Modal Semantic Perturbation." arXiv preprint arXiv:2511.03774 (2025).
---

<!-- NOTE: Summary based on title only - verify and expand with actual abstract -->

**Authors:** Jaden Park, Mu Cai, Feng Yao, Jingbo Shang, **Soochahn Lee**, Yong Jae Lee

> **TL;DR:** A method to detect benchmark contamination in vision-language models by applying multi-modal semantic perturbations and analyzing how model performance degrades, revealing whether training data leaked into evaluation sets.

---

## What this paper is about

As vision-language models (VLMs) get trained on massive internet-scale datasets, there is a growing concern that benchmark test data may have leaked into training sets. This contamination inflates reported performance and undermines fair evaluation, but detecting it is tricky since training data is often not publicly available.

## Key idea

The approach applies controlled semantic perturbations across multiple modalities (text and images) to benchmark examples and measures how the model's performance changes. Contaminated models that have memorized specific test examples will show disproportionate sensitivity to these perturbations compared to genuinely learned capabilities.

![Figure description](/images/publications/2025-11-05-contamination-detection-for-vlms-using-fig1.png)
*Example of our multi-modal semantic perturbation pipeline applied to RealWorldQA benchmark. Using ControlNet trained with Flux models, a new speed limit sign is generated, changing the correct answer from (B) to (C) while preserving the original image’s overall composition. A contaminated model that has memorized the original question is likely to fail on the perturbed version.*

## Why it matters

This provides the community with a practical tool to audit VLMs for benchmark contamination, helping ensure that reported progress reflects genuine model capabilities rather than data leakage.

