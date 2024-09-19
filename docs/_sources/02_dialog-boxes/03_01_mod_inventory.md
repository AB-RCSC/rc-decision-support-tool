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
(i_mod_inventory)=
# {{ name_mod_inventory }}

::::::{dropdown} Assumptions, Pros, Cons
:::::{grid}

::::{grid-item-card} Assumptions
- {{ mod_inventory_assump_01 }}
::::
::::{grid-item-card} Pros
- {{ mod_inventory_pro_01 }}
::::
::::{grid-item-card} Cons
- {{ mod_inventory_con_01 }}
::::
:::::
::::::

:::::::{tab-set}

::::::{tab-item} Overview
**{{ term_mod_inventory }}**: {{ term_def_mod_inventory }}
Species inventories are used to determine what species are present in an area during a given time period ({{ ref_intext_wearn_gloverkapfer_2017 }}). Inventories can be considered as a “checklist”, “minimum count”, or rapid assessment survey. The goal is to detect as many species as possible. With adequate sampling effort, species inventories may be help delineate species distribution, inform habitat associations, and provide an index of common species in an area. This assumes however that species can be reliably detected with sufficient effort, which may not be the case even for common or conspicuous species as many factors may influence species detection (e.g., sampling protocols, weather, observer experience etc.). Thus, only species presence (not absence) can be reliably determined. There are no attempts to quantify aspects of communities or populations, and no formal modeling approach are used. 

**<font size="4"><span style="color:#2F5496">Study design</font></span>**

The study design (e.g., camera arrangement) of species inventories is very flexible. However, if you’re targeting a single species the design should ideally still be informed by the species’ biology to maximize the likelihood of detecting individuals that are present. Information on preferred habitats, travel routes, or high activity areas (e.g., mineral licks, burrows) can be especially useful in determining where to strategically place cameras. When the species biology is **well known**, putting cameras at these targeted (non-random) locations may be beneficial. Alternatively, such as when the species biology is **poorly known**, randomly placing cameras across the study area may be the best approach to help ensures that all habitats are sampled in proportion to their availability ({{ ref_intext_wearn_gloverkapfer_2017 }}). The area sampled should in these cases be representative of the entire study area. Interestingly, in these cases, the area covered by cameras may have little effect on the number of species detected ({{ ref_intext_tobler_et_al_2008 }}).

**<font size="4"><span style="color:#2F5496"> Bait and Lure </font></span>**

The use of lure or bait may improve the likelihood of detecting some species (e.g., carnivores). 

**<font size="4"><span style="color:#2F5496"> Camera Specifications</font></span>**

There are no specific guidelines for species inventories regarding camera features or deployment (e.g., number of cameras, camera days per location etc.). However, a camera model with a white flash, high sensitivity, large detection zone, and fast trigger speed may improve species detection ({{ ref_intext_rovero_et_al_2013 }}; {{ ref_intext_wearn_gloverkapfer_2017 }}). 

Number of Cameras and Survey Duration
For species with a high probability of detection (e.g., small home range), deployment times can be short (e.g., 1-2 weeks) and moving cameras between locations can allow more sites to be sampled ({{ ref_intext_wearn_gloverkapfer_2017 }}). In contrast, cameras should be deployed longer in a location (e.g., 2-6 weeks; {{ ref_intext_wearn_gloverkapfer_2017 }}) for species with low probability of detection.  

When the target species biology is poorly known, a general rule of thumb is to use a minimum of 20 single cameras per location within the study area, spaced 1-2 km apart, for ideally a minimum of 30 days per camera location and 1,000 overall camera days ({{ ref_intext_colyn_et_al_2018 }}; {{ ref_intext_rovero_et_al_2013 }}; {{ ref_intext_rovero_tobler_2010 }}; {{ ref_intext_tobler_et_al_2008 }}; {{ ref_intext_wearn_et_al_2013 }}; {{ ref_intext_wearn_gloverkapfer_2017 }}). The more cameras deployed and/or locations sampled, generally the shorter the time needed to inventory an area. If fewer cameras are used, the cameras could be moved every 15 days, if feasible, to sample a larger area and avoid any biases associated with the camera locations ({{ ref_intext_rovero_et_al_2013 }}). In many areas, 1000-2000 camera days is sufficient to detect 60-70% of the species in the area ({{ ref_intext_ahumada_et_al_2011 }}; {{ ref_intext_tobler_et_al_2008 }}).  

**<font size="4"><span style="color:#2F5496"> Analysis</font></span>**

Caution should be exercised in comparing the results of species inventories from different times of year within the same study area, or between study areas. The amount of sampling effort will need to be accounted for when examining any results.
::::::

::::::{tab-item} Advanced
Species accumulation curves can be used to determine if the survey effort is sufficient to estimate the number of species in an area. These curves plot the survey effort per unit time (x-axis) against the cumulative number of species detected (y-axis). The survey effort per unit time is the number of camera days (i.e., number of cameras multiplied by the number of days the cameras are operating) or survey days. The optimal survey effort occurs when the accumulation curve reaches an asymptote. This leveling of the curve indicates that very few, if any, new species are detected despite increasing survey effort. Refer to “<https://ab-rcsc.github.io/rc-decision-support-tool_concept-library/02_dialog-boxes/01_10_sp_asymptote.html> for more information on species accumulation curves, and Tobler et al. (2008) for additional examples of species accumulation curves. 

Various methods are available to assess the completeness of species inventories and to estimate the true species number in incomplete surveys (e.g., {{ ref_intext_colwell_coddington_1994 }}; {{ ref_intext_colwell_et_al_2004 }}; {{ ref_intext_soberon_lorente_1993 }}). These non-parametric and species richness estimators ({{ ref_intext_colwell_coddington_1994 }}), with the former generally performing better in comparative studies ({{ ref_intext_walther_moore_2005  }}).
::::::

::::::{tab-item} Visual resources
:::::{grid} 3
:gutter: 1
:padding: 0
:margin: 0

::::{grid-item-card} {{ ref_intext_wearn_gloverkapfer_2017 }}
```{figure} ../03_images/03_image_files/wearn_gloverkapfer_2017_fig7_3.png
:class: img_grid
```
**Wearn & Glover-Kapfer (2017) – Fig. 7-3** Decision tree for short-term inventory work.
::::

::::{grid-item-card} {{ ref_intext_wearn_gloverkapfer_2017 }}
```{figure} ../03_images/03_image_files/wearn_gloverkapfer_2017_table_7_2.png 
:class: img_grid
```
**Wearn & Glover-Kapfer (2017) – Table 7-2** - Recommended survey design characteristics for the major types of camera trap study, as taken from a broad review of the camera trap literature. Key references provide survey design advice or draw attention to important survey design considerations. The quantitative recommendations made here will often need to be adjusted to the specific context of a single study; this process can be informed by pilot studies or simulation work.
::::

:::::

::::::

::::::{tab-item} Shiny apps/Widgets
Check back in the future!
::::::

::::::{tab-item} Analytical tools & resources
| Type | Name | Note | URL |Reference |
|:----------------|:---------------------------------------|:----------------------------------------------------------------|:----------------------------------------------------------------|:----------------------------------------------------------------|
| Program | Program “PRESENCE |  This package allow users to simulate the required sample size for a desired level of precision in species richness. | **Software**: <www.mbr-pwrc.usgs.gov/ software/presence.html>;<br>**Help forum**: <www.phidot.org> | {{ ref_bib_hines_2006 }} |
| Program | GENPRES | This package allow users to simulate the required sample size for a desired level of precision in species richness. |  | {{ ref_bib_bailey_et_al_2007 }} |
| R function | specaccum: Species Accumulation Curve | The specaccum function finds species accumulation curves or the number of species for a certain number of sampled sites or individuals. | <https://rdrr.io/rforge/vegan/man/specaccum.html> | {{ ref_bib_oksanen_et_al_2024 }} |
| R package | PresenceAbsence: An R package for presence absence analysis | The PresenceAbsence package for R provides a set of functions useful when evaluating
the results of presence-absence analysis. | <https://research.fs.usda.gov/treesearch/29484> | {{ ref_bib_freeman_gretchen_2008 }} |
::::::

::::::{tab-item} References
{{ ref_bib_ahumada_et_al_2011 }}

{{ ref_bib_colyn_et_al_2018 }}

{{ ref_bib_colwell_coddington_1994 }}

{{ ref_bib_colwell_et_al_2004 }}

{{ ref_bib_freeman_gretchen_2008 }}

{{ ref_bib_rcsc_et_al_2024 }}

{{ ref_bib_rovero_et_al_2013 }}

{{ ref_bib_rovero_tobler_2010 }}

{{ ref_bib_soberon_lorente_1993 }}

{{ ref_bib_tobler_et_al_2008 }}

{{ ref_bib_walther_moore_2005 }}

{{ ref_bib_wearn_et_al_2013 }}

{{ ref_bib_wearn_gloverkapfer_2017 }}	
::::::

:::::::