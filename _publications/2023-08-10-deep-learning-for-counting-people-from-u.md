---
title: "Deep learning for counting people from UWB channel impulse response signals"
collection: publications
date: 2023-08-10
venue: 'Sensors'
excerpt: '**Gun Lee**, **Subin An**, Byung-Jun Jang, **Soochahn Lee**'
htmlurl: 'https://www.mdpi.com/1424-8220/23/16/7093'
pdfurl: 'https://www.mdpi.com/1424-8220/23/16/7093/pdf?version=1691676473'
thumbnail: '/images/publications/2023-08-10-deep-learning-for-counting-people-from-u-fig1.png'
bibtex: |
    @article{Lee_2023, title={Deep Learning for Counting People from UWB Channel Impulse Response Signals}, volume={23}, ISSN={1424-8220}, url={http://dx.doi.org/10.3390/s23167093}, DOI={10.3390/s23167093}, number={16}, journal={Sensors}, publisher={MDPI AG}, author={Lee, Gun and An, Subin and Jang, Byung-Jun and Lee, Soochahn}, year={2023}, month=aug, pages={7093} }
citation_mla: |
    Lee, Gun, et al. “Deep Learning for Counting People from UWB Channel Impulse Response Signals.” Sensors, vol. 23, no. 16, Aug. 2023, p. 7093. Crossref, https://doi.org/10.3390/s23167093.
---
<!-- NOTE: Summary based on title only - verify and expand with actual abstract -->

**Authors:** **Gun Lee**, **Subin An**, Byung-Jun Jang, **Soochahn Lee**

> **TL;DR:** A deep learning method that counts the number of people in a room using Ultra-Wideband (UWB) radar channel impulse response signals, providing a privacy-preserving alternative to camera-based occupancy estimation.

---

## What this paper is about

![Figure description](/images/publications/2023-08-10-deep-learning-for-counting-people-from-u-fig1.png)
*Laboratory space configuration to estimate the number of people in a room based on the waveform of the channel impulse response (CIR) from UWB transceivers*

Knowing how many people are in a space is useful for smart buildings, energy management, and safety systems. Camera-based counting raises privacy concerns, and other sensor modalities like PIR or CO2 are slow or inaccurate. UWB radar can detect human presence through reflected signals, but extracting an accurate people count from raw channel impulse response (CIR) data is non-trivial.

## Key idea

The paper applies deep learning models to UWB CIR signals to directly regress the number of occupants. The network learns to interpret the complex multipath reflections in the impulse response -- where each person contributes additional reflected components -- and maps them to a people count, handling challenges like overlapping signal paths and varying room layouts.

## Why it matters

This approach enables occupancy counting without cameras, preserving privacy while achieving reliable performance. It opens the door to practical smart-space applications where visual monitoring is undesirable or infeasible.

