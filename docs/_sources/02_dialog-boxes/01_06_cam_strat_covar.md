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
(i_cam_strat_covar)=
# {{ title_i_cam_strat_covar }}

:::::::{tab-set}

::::::{tab-item} Overview
This question relates to the number of cameras you might need, since this will depend on the number of different “strata” you might hope to include (if you are “stratifying” locations). Stratifying is a useful approach when you are interested in assessing the effect of a particular variable(s) and/or accounting for confounding variable(s) that could lead to biased results if not addressed. For example, when determining species diversity in an area, you may be interested in assessing the effects of habitat types while also accounting for distance to roads.

In a stratified design, the study area is divided into smaller strata according to distinct features (e.g., habitat types, disturbance classes). These strata can then be sampled non-randomly or randomly. Non-random sampling] means that the different strata are sampled in proportion to specific criteria, as determined by the study objective (e.g., behaviour). For example, more cameras may be placed in strata that are more likely to detect the species of interest, such as in mixed wood forest to monitor moose behaviour. Conversely, in a [stratified random design ](#sampledesign_stratified_random), the different strata are sampled in proportion to their availability in the study area (e.g., 75% of your camera sites would occur in mixed wood forests if this habitat type make-ups 75% of your study area). While a [random design](#sampledesign_random) may lead to fewer overall species detections, it does help ensure that all strata (e.g., habitat types) within the study area are represented in your sampling.

The number (and selection of) strata appropriate for a given study area will depend on the [study objectives](#survey_objectives), landscape diversity, spatial scale, [Target Species](#target_species), and available resources. For example, a study estimating abundance of a species that is wide-ranging and patchily distributed across a study area with a diversity of habitat types will typically have more strata than that for the same species in a simpler landscape or species distribution. Sampling effort (e.g., number of cameras, camera days) will increase with the number of strata. Wearn & Glover-Kapfer (2017) recommended at least 20 camera locations, and ideally 50 locations, per strata for reasonably precise estimates of species diversity, richness, relative abundance, and behaviours. 
::::::

::::::{tab-item} Advanced
Camera locations and their spatial arrangements are integral components of any study design and strongly influence detection probability and likelihood of species occurrence.

In a stratified non-random study design, more cameras may be strategically placed in strata known or suspected to have higher activity, that are more common, and/or that have higher expected variance within a stratum. By allocating sampling effort in strata that have higher likelihood of detection, are larger, and/or more variable, overall effort may be reduced and precision of estimates improved. However, there are several important disadvantages to using a non-random study design, including the possibility of missing individuals/species/behaviours entirely, and the inability to make inferences to the entire study area.

Generally, a stratified random placement is recommended for species diversity and richness, relative abundance, and behaviour objectives; however, the optimal design for a given study will be influenced by the expected variation in detection probabilities, available resources, and the relative importance of the pros and cons for each design. For example, an optimal study design may be considered that that provides the greatest precision for the lowest cost. Stratification may help minimize detection bias, optimize sampling effort, and ultimately result in more precise estimates. However, a stratified random study design may not adequately address some biases in detection probability due to environmental factors (e.g., vegetation denseness) and require subsequently correcting for these biases in a statistical framework. Standardizing other sampling components (e.g., camera set-up protocols) as much may help reduce some other study-specific biases.
  
It may not always be possible to address biases of confounding variables in the study design phase (e.g., using stratification, complex hierarchically structured designs) or by using standardized field and reporting protocols over time and space. Examples of these instances include when collecting data on multiple species concurrently across seasons, or when using data from different studies and sampling protocols. To address these situations, one needs to either correct for the metric of interest (e.g., relative abundance) or using use covariates in an advanced statistics framework to address known or suspected confounding variables. A covariate can be an independent variable (i.e., a variable you manipulate or change in your study because it is of direct interest). It can be instead though an unwanted, “confounding” variable that, if not accounted for, can lead to biased, and/or result in inaccurate conclusions. A common approach to correct for detection biases when estimating relative abundance, for instance, is to quantify effective detection range for example (e.g., {{ ref_intext_hofmeester_et_al_2017 }}; {{ ref_intext_rowcliffe_et_al_2011 }}). Alternatively, covariates can be used in simple multiple linear regression models and/or much more complex hierarchal (or structured) models. For example, detection probability can be modeled with covariates to obtain separate estimates for different study-specific factors introducing detection biases (e.g., habitat type, season, sex). Regression models have the limitation of only addressing single processes, and therefore are unable to differentiate between detection and ecological processes (e.g., movement versus abundance), while interpretation of hierarchical models may be complicated. Refer to Gilbert et al. (2020) and Wilgenburg et al. (2020) for examples of hierarchical models. See Esteveo et al. (2017) for fitting of habitat covariates in co-occurrence models to estimate occupancy and detection of one species in the presence of another.
::::::

::::::{tab-item} References
{{ ref_bib_esteveo_et_al_2017 }}

{{ ref_bib_gilbert_et_al_2020 }}

{{ ref_bib_hofmeester_et_al_2017 }}

{{ ref_bib_rowcliffe_et_al_2011 }}

{{ ref_bib_wearn_gloverkapfer_2017 }}

{{ ref_bib_vanwilgenburg_et_al_2020 }}
::::::

:::::::