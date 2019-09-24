---
layout: paper
published: true
category: paper
image: /assets/images/papers/default-paper.svg
title : Rosetta FunFolDes - A general framework for the computational design of functional proteins
year : 2018
shortref : Bonet et al. PLoS computational biology 2018
journal : PLoS computational biology
pmid : 30452434
authors : Bonet J, Wehrle S, Schriever K, Yang C, Billet A, Sesterhenn F, Scheck A, Sverrisson F, Veselkova B, Vollers S, Lourman R, Villard M, Rosset S, Krey T, Correia BE
doi : 10.1371/journal.pcbi.1006623
---
{% include JB/setup %}

# Abstract

The robust computational design of functional proteins has the potential to deeply impact translational research and broaden our understanding of the determinants of protein function and stability. The low success rates of computational design protocols and the extensive in vitro optimization often required, highlight the challenge of designing proteins that perform essential biochemical functions, such as binding or catalysis. One of the most simplistic approaches for the design of function is to adopt functional motifs in naturally occurring proteins and transplant them to computationally designed proteins. The structural complexity of the functional motif largely determines how readily one can find host protein structures that are "designable", meaning that are likely to present the functional motif in the desired conformation. One promising route to enhance the "designability" of protein structures is to allow backbone flexibility. Here, we present a computational approach that couples conformational folding with sequence design to embed functional motifs into heterologous proteins-Rosetta Functional Folding and Design (FunFolDes). We performed extensive computational benchmarks, where we observed that the enforcement of functional requirements resulted in designs distant from the global energetic minimum of the protein. An observation consistent with several experimental studies that have revealed function-stability tradeoffs. To test the design capabilities of FunFolDes we transplanted two viral epitopes into distant structural templates including one de novo "functionless" fold, which represent two typical challenges where the designability problem arises. The designed proteins were experimentally characterized showing high binding affinities to monoclonal antibodies, making them valuable candidates for vaccine design endeavors. Overall, we present an accessible strategy to repurpose old protein folds for new functions. This may lead to important improvements on the computational design of proteins, with structurally complex functional sites, that can perform elaborate biochemical functions related to binding and catalysis.