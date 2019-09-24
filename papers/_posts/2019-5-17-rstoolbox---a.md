---
layout: paper
published: true
category: paper
image: /assets/images/papers/default-paper.svg
title : rstoolbox - a Python library for large-scale analysis of computational protein design data and structural bioinformatics
year : 2019
shortref : Bonet et al. BMC bioinformatics 2019
journal : BMC bioinformatics
pmid : 31092198
authors : Bonet J, Harteveld Z, Sesterhenn F, Scheck A, Correia BE
doi : 10.1186/s12859-019-2796-3
---
{% include JB/setup %}

# Abstract

Large-scale datasets of protein structures and sequences are becoming ubiquitous in many domains of biological research. Experimental approaches and computational modelling methods are generating biological data at an unprecedented rate. The detailed analysis of structure-sequence relationships is critical to unveil governing principles of protein folding, stability and function. Computational protein design (CPD) has emerged as an important structure-based approach to engineer proteins for novel functions. Generally, CPD workflows rely on the generation of large numbers of structural models to search for the optimal structure-sequence configurations. As such, an important step of the CPD process is the selection of a small subset of sequences to be experimentally characterized. Given the limitations of current CPD scoring functions, multi-step design protocols and elaborated analysis of the decoy populations have become essential for the selection of sequences for experimental characterization and the success of CPD strategies.
Here, we present the rstoolbox, a Python library for the analysis of large-scale structural data tailored for CPD applications. rstoolbox is oriented towards both CPD software users and developers, being easily integrated in analysis workflows. For users, it offers the ability to profile and select decoy sets, which may guide multi-step design protocols or for follow-up experimental characterization. rstoolbox provides intuitive solutions for the visualization of large sequence/structure datasets (e.g. logo plots and heatmaps) and facilitates the analysis of experimental data obtained through traditional biochemical techniques (e.g. circular dichroism and surface plasmon resonance) and high-throughput sequencing. For CPD software developers, it provides a framework to easily benchmark and compare different CPD approaches. Here, we showcase the rstoolbox in both types of applications.
rstoolbox is a library for the evaluation of protein structures datasets tailored for CPD data. It provides interactive access through seamless integration with IPython, while still being suitable for high-performance computing. In addition to its functionalities for data analysis and graphical representation, the inclusion of rstoolbox in protein design pipelines will allow to easily standardize the selection of design candidates, as well as, to improve the overall reproducibility and robustness of CPD selection processes.