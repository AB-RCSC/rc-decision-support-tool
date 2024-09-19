---
jupytext:
  formats: md:myst
  text_representation:
    extension: .md
    format_name: myst
    format_version: 0.17.2 <!--0.13-->
    jupytext_version: 6.5.4 <!-- 1.16.4-->
kernelspec:
  display_name: Python 3
  language: python
  name: python3
editor_options: 
  markdown: 
  wrap: none
---
(i_study_area)=
# Study area

A [study area](#study_area) is a unique area(s) within a [project](#project). There may be multiple [study areas](#study_area) within a larger [study area](#study_area). Aspects to consider when identifying the [study area](#study_area) include the spatial extent (and method of delineation), shape ({{ ref_intext_foster_harmsen_2012 }}), and composition and configuration of features within it (including habitat types, land uses and disturbances).

Several factors influence the size (spatial extent) of the study area, including the [objectives](#survey_objectives), ecosystem, the biology of the [Target Species](#target_species) (e.g., dispersal ability, habitat preferences, etc.) and/or [modelling approach](#mods_modelling_approach).

For example, [density](#density) models using the [capture-recapture (CR)](#mods_cr_cmr) [modelling approach](#mods_modelling_approach) requires that the [study area](#study_area) encompasses the entire area in which individuals can move during the [survey](#survey) and that each individual can be detected by a camera ({{ ref_intext_karanth_nichols_1998 }}). In this case, the animal’s home range size could be used (e.g., four times the home range size [{{ ref_intext_maffei_noss_2008 }}]) ({{ ref_intext_wearn_gloverkapfer_2017 }}) in combination with a finite number of cameras available (e.g., 20 cameras are available; ideally, they should be [paired](#sampledesign_paired) and there should be \> 4 cameras in each home range [{{ ref_intext_wearn_gloverkapfer_2017 }}]) to define the [project](#project)’s spatial extent.

Methods to delineate the appropriate spatial extent include, for example, minimum convex polygons (i.e., a polygon surrounding the locations of previous detections) or [kernel density estimators](#kernel_density_estimator) (e.g., via the probability of "utilization" \[{{ ref_intext_jennrich_turner_1969 }}\]). Geographic Information Systems (GIS, e.g., ESRI software) or programming languages (e.g., R) contain useful tools for these delineation methods.