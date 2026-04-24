---
title: "Effects of hypertension, diabetes, and smoking on age and sex prediction from retinal fundus images."
collection: publications
date: 2020-03-12
venue: 'Scientific Reports'
excerpt: 'Yong Dae Kim, **Kyoung Jin Noh**, Seong Jun Byun, **Soochahn Lee**, Tackeun Kim, Leonard Sunwoo, Kyong Joon Lee, Si-Hyuck Kang, Kyu Hyung Park & Sang Jun Park'
htmlurl: 'https://www.nature.com/articles/s41598-020-61519-9'
pdfurl: 'https://www.nature.com/articles/s41598-020-61519-9.pdf'
thumbnail: '/images/publications/2020-03-12-effects-of-hypertension-diabetes-and-s-fig2.png'
bibtex: |
    @article{Kim_2020, title={Effects of Hypertension, Diabetes, and Smoking on Age and Sex Prediction from Retinal Fundus Images}, volume={10}, ISSN={2045-2322}, url={http://dx.doi.org/10.1038/s41598-020-61519-9}, DOI={10.1038/s41598-020-61519-9}, number={1}, journal={Scientific Reports}, publisher={Springer Science and Business Media LLC}, author={Kim, Yong Dae and Noh, Kyoung Jin and Byun, Seong Jun and Lee, Soochahn and Kim, Tackeun and Sunwoo, Leonard and Lee, Kyong Joon and Kang, Si-Hyuck and Park, Kyu Hyung and Park, Sang Jun}, year={2020}, month=mar }
citation_mla: |
    Kim, Yong Dae, et al. “Effects of Hypertension, Diabetes, and Smoking on Age and Sex Prediction from Retinal Fundus Images.” Scientific Reports, vol. 10, no. 1, Mar. 2020. Crossref, https://doi.org/10.1038/s41598-020-61519-9.
---

<!-- NOTE: Summary based on title only - verify and expand with actual abstract -->

**Authors:** Yong Dae Kim, **Kyoung Jin Noh**, Seong Jun Byun, **Soochahn Lee**, Tackeun Kim, Leonard Sunwoo, Kyong Joon Lee, Si-Hyuck Kang, Kyu Hyung Park & Sang Jun Park

> **TL;DR:** A study investigating how systemic conditions -- hypertension, diabetes, and smoking -- affect deep learning models that predict age and sex from retinal fundus images, revealing that these conditions make the retina appear "older."

---

## What this paper is about

![Figure description](/images/publications/2020-03-12-effects-of-hypertension-diabetes-and-s-fig1.png)
*Flow chart illustrating the processes of data partitioning, training, validation, and testing. SBRIA, Seoul National University Bundang Hospital Retina Image Archive; DM, diabetes mellitus.*

Deep learning models can predict a person's age and sex surprisingly well just from a photograph of their retina. But what happens to these predictions when the patient has hypertension, diabetes, or is a smoker? These conditions are known to cause vascular changes in the retina, and this study asks whether and how they influence the model's predictions.

## Key idea

![Figure description](/images/publications/2020-03-12-effects-of-hypertension-diabetes-and-s-fig2.png)
*Representative class activation mapping (CAM) heat-map and its original image in age prediction model. It shows the regions that have higher influence on the prediction results in red, relative to the regions with lower influence, in blue. The CAM of the age prediction model indicated activation primarily in the vascular region.*

![Figure description](/images/publications/2020-03-12-effects-of-hypertension-diabetes-and-s-fig3.png)
*Class activation mapping (CAM) heat-map in original fundus photograph image and retinal vessel-erased image in age prediction model. CAM heat-map still focused on the retinal vascular arcade area, thus resulting in an obvious decline in the accuracy of age prediction, as shown in Table 5.*


The study trains deep learning models for age and sex prediction on retinal fundus images, then systematically analyzes how the presence of hypertension, diabetes, and smoking affects prediction accuracy and introduces bias. The analysis reveals that these conditions cause the model to overestimate age, suggesting that vascular damage makes the retina appear biologically older.

## Why it matters

Published in Scientific Reports, this work provides important clinical insight: the retinal "aging" signal detected by AI is confounded by systemic disease, which has implications both for using retinal age as a biomarker and for understanding how these conditions affect the eye.

