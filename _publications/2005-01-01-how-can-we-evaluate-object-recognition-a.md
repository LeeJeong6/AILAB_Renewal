---
title: "How Can We Evaluate Object Recognition Algorithms Using a Public Object Image Database?"
collection: publications
date: 2005-01-01
venue: 'IEEE/CVF Conference on Computer Vision and Pattern Recognition Workshop (CVPRW)'
excerpt: '**Soochahn Lee**, Duck Hoon Kim, Sang Uk Lee, Il Dong Yun'
thumbnail: '/images/publications/2005-01-01-how-can-we-evaluate-object-recognition-a-fig1.png'
pdfurl: 'https://drive.google.com/file/d/15XMYxa9Oig8ml6EJXyUVvNobJBUug9os/view'
htmlurl: 'https://ieeexplore.ieee.org/document/1565335'
bibtex: |
    @inproceedings{Soo_Chahn_Lee, title={How CanWe Evaluate Object Recognition Algorithms Using a Public Object Image Database?}, volume={3}, url={http://dx.doi.org/10.1109/cvpr.2005.468}, DOI={10.1109/cvpr.2005.468}, booktitle={2005 IEEE Computer Society Conference on Computer Vision and Pattern Recognition (CVPR’05) - Workshops}, publisher={IEEE}, author={**Soo Chahn Lee** and Duck Hoon Kim and Sang Uk Lee and Dong Yun Yun}, pages={37–37} }
citation_mla: |
    **Soo Chahn Lee**, et al. “How CanWe Evaluate Object Recognition Algorithms Using a Public Object Image Database?” 2005 IEEE Computer Society Conference on Computer Vision and Pattern Recognition (CVPR’05) - Workshops, vol. 3, pp. 37–37. Crossref, https://doi.org/10.1109/cvpr.2005.468.
---

**Authors:** **Soochahn Lee**, Duck Hoon Kim, Sang Uk Lee, Il Dong Yun

> **TL;DR:** We propose an evaluation framework for object recognition algorithms that synthesizes realistic "Virtual Scenes" from the Amsterdam Library of Object Images, enabling controlled benchmarking under varying viewpoint, illumination color, and illumination direction.

---

## What this paper is about

How do you fairly test whether an object recognition algorithm actually works? In 2005, public object image databases like the Amsterdam Library of Object Images (ALOI) existed, but there was no systematic way to use them for controlled evaluation. Simply running a detector on individual object images doesn't tell you how it performs in cluttered, realistic scenes.

## Key idea 

We build synthetic natural scenes -- called "Virtual Scenes" -- by compositing object images from ALOI. To test a specific condition (say, changing illumination direction), we select a target object and place it alongside randomly chosen distractor objects, all rendered under that condition. By generating many Virtual Scenes per condition, we can statistically analyze how a recognition algorithm degrades under each factor. As a demonstration, we evaluate a SIFT-based recognition method across variations in viewing direction, illumination color, and illumination direction.

![Figure description](/images/publications/2005-01-01-how-can-we-evaluate-object-recognition-a-fig1.png)
*(Left) An example of a virtual 3-D plane projected onto a Virtual Scene. (Right) An example of the area on which 3-D instances are placed in the virtual 3-D plane.*


## Why it matters

This framework turns a static object database into a flexible evaluation testbed, letting researchers isolate exactly which real-world factors trip up their algorithms -- something that was hard to do with existing benchmarks at the time.

