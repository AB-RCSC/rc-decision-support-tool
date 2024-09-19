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
(i_sp_hr_size)=
# {{ title_i_sp_hr_size }}
:::{note}
Dont have information on home range size? Check out the “Shiny Apps/Widgets” tab to see if information for your Target Species is available for in our “Species home range / body size lookup.”
:::

:::::::{tab-set}

::::::{tab-item} Overview
**<font size="4"><span style="color:#2F5496">How does this relate to study design?</font></span>**

Many aspect of site selection and study duration are often linked to the home range size of the [Target Species](#target_species); this is because many [modelling approaches](#mods_modelling_approach) (e.g. [occupancy models](#mods_occupancy) [{{ ref_intext_mackenzie_et_al_2004 }}] assume “site closure” (i.e., that there is no change in state (e.g. species presence/ absence, immigration/ emigration, births/deaths) during the [survey](#survey) period ({{ ref_intext_mackenzie_et_al_2004 }}). For some approaches, violation of the site closure [assumption](#mods_modelling_assumption) can result in an underestimate of [detection probabilities](#detection_probability) and, in turn, over-estimate [density](#density) (e.g., with spatial recapture models) or result in simply averaging detections over the sampling period (e.g., [REM](#mods_rem) [{{ ref_intext_rowcliffe_et_al_2008 }}; {{ ref_intext_rowcliffe_et_al_2023 }}], [REST](#mods_rest) [{{ ref_intext_nakashima_et_al_2018 }}] models). To meet the “site closure” [assumption](#mods_modelling_assumption), the study design might include spacing cameras far enough apart that the same individual is not detected at multiple sites (e.g., larger than the species' home range size); this is often referred to as “independent camera locations”. 

The [survey](#survey) duration must also be short enough that the probability of [occupancy](#occupancy) does not change (i.e., not confounded by other processes, e.g., by changes in the population) ({{ ref_intext_oconnell_et_al_2011 }}). 
:::{note}
Home range size information should, ideally, be chosen to reflect the conditions of your study (as closely as possible). For example, using data on home range size from a study that only reported home range size for one season (e.g., summer home range size) might bias placement if your study aims to evaluate occupancy over the entire year of a species whose movement highly varies between seasons (e.g., moves more in summer).
:::
::::::

::::::{tab-item} Visual resources
:::::{grid} 3
:gutter: 1
:padding: 0
:margin: 0

::::{grid-item-card}
```{figure} ../03_images/03_image_files/00_coming_soon.png
:width: 300px
:align: center
```
::::

:::::

::::::

::::::{tab-item} Shiny apps/Widgets

:::::{card}
A R Shiny app created for the RC Decision Support Tool to lookup information on species home range size / body size; information pulled directly from the following sources:
- Burton et al. (2015) supplementary material “S2. Average body mass and home range size for a sample of species and studies among the reviewed set of camera trap publications”
- PanTHERIA database ({{ ref_intext_jones_et_al_2009 }}) “a species-level database of life history, ecology,and geography of extant and recently extinct mammals
- HomeRange: A global database of mammalian home ranges ({{ ref_intext_broekman_et_al_2022 }})

<iframe 
    width="100%"
    height="900"
    src="https://7e2l38-cassondra-stevenson.shinyapps.io/lu_species_homerange/"
    frameborder="0" 
    allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture"
    allowfullscreen>
</iframe>
:::::

::::::

::::::{tab-item} Analytical tools & resources
| Type | Name | Note | URL |Reference |
|:----------------|:---------------------------------------|:----------------------------------------------------------------|:----------------------------------------------------------------|:----------------------------------------------------------------|
| Data/Database | HomeRange: A global database of mammalian home range | HomeRange, a global database with 75,611 home- range values across 960 different species of mammals, including terrestrial, aquatic and aerial species | Article: <https://onlinelibrary.wiley.com/doi/epdf/10.1111/geb.13625>;<br>Data: <https://github.com/SHoeks/HomeRange>/<br><https://shoeks.github.io/HomeRange/> | {{ ref_bib_broekman_et_al_2022 }} |
| Data/Database | Supplementary material; PanTHERIA: a species-level database of life history, ecology,and geography of extant and recently extinct mammals |    | <https://ecologicaldata.org/wiki/pantheria> | {{ ref_bib_jones_et_al_2009 }} |
| Data/Database | Supplementary material; Wildlife camera trapping: a review and recommendations for linking surveys to ecological processes  | **Burton et al. (2015) **<br> - Table S2. Data on body size and home range size for a sample of surveyed species.<br>-“Table S1. Bibliographic details and data summarized from camera trap publications included in the review.” | Article: <https://besjournals.onlinelibrary.wiley.com/doi/full/10.1111/1365-2664.12432>;<br>[Download the XLS](https://besjournals.onlinelibrary.wiley.com/action/downloadSupplement?doi=10.1111%2F1365-2664.12432&file=jpe12432-sup-0006-TableS2.csv) and/or<br>[Download the related references CSV ](https://besjournals.onlinelibrary.wiley.com/action/downloadSupplement?doi=10.1111%2F1365-2664.12432&file=jpe12432-sup-0005-TableS1.xlsx) | {{ ref_bib_burton_et_al_2015 }} |
::::::

::::::{tab-item} References
{{ ref_bib_broekman_et_al_2022 }}

{{ ref_bib_burton_et_al_2015 }}

{{ ref_bib_jones_et_al_2009 }}

{{ ref_bib_mackenzie_et_al_2004 }}

{{ ref_bib_nakashima_et_al_2018 }}

{{ ref_bib_oconnell_et_al_2011 }}

{{ ref_bib_rowcliffe_et_al_2008 }}

{{ ref_bib_rowcliffe_et_al_2013 }}
::::::

:::::::