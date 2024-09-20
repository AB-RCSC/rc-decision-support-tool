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
(i_objective)=
# {{ title_i_objective }}

:::::::::{div} full-width

:::::::{tab-set}

::::::{tab-item} Overview

Definitions for each option are as follows (with a few additional notes):

- **{{ name_mod_inventory }}**: {{ term_def_mod_inventory }}

- **{{ name_mod_divers_rich }}**

    - **{{ term_mod_divers_rich_rich }}**: {{ term_def_mod_divers_rich_rich }}

    - **{{ term_mod_divers_rich_divers }}**: {{ term_def_mod_divers_rich_divers }}

    - Note that there are multiple “levels” to Species diversity & richness, these include:

        -   **{{ term_mod_divers_rich_alpha }}**: {{ term_def_mod_divers_rich_alpha }}

        -   **{{ term_mod_divers_rich_beta }}**: {{ term_def_mod_divers_rich_beta }}

        -   **{{ term_mod_divers_rich_gamma }}**: {{ term_def_mod_divers_rich_gamma }}

- **{{ name_obj_occupancy }}**: {{ name_def_obj_occupancy }}

- **Abundance (Relative vs. Absolute)**:..

    - **{{ name_obj_abundance }}**: {{ name_def_obj_abundance }}
  
    - **{{ name_obj_rel_abund }}**: {{ name_def_obj_rel_abund }}

- **{{ name_obj_density }}**: {{ name_def_obj_density }}

- **{{ name_obj_vital_rate }}**: {{ name_def_obj_vital_rate }}

- **{{ name_obj_behaviour }}**: {{ name_def_obj_behaviour }}

***

One of the first choices you will make when designing your study, is what it is that you plan to measure (or your “state variable”; a formal measure that summarizes the state of a community or population at a particular time \[{{ ref_intext_wearn_gloverkapfer_2017 }}\]). Since this concept might be easy to confuse with [Survey Objective(s)](#survey_objectives) (and since “objective” is often referred to interchangeably with “state variable”), consider the following figure:

**<font size="4"><span style="color:#2F5496">Objective *vs.* State Variable</font></span>**

```{figure} ../03_images/03_image_files/00_FIG_obj_state_var.png
:width: 900px
:align: center
```

:::::{card}
An essential first step when designing any [survey](#survey) is to clearly define its [objectives](#survey_objectives). [Survey Objectives](#survey_objectives) should be specific, measurable, achievable, relevant and time-bound (i.e., SMART). [Survey Objectives](#survey_objectives) should describe the following:

-   [Target Species](#target_species) - the species that the [survey](#survey) is designed to detect,

-   [State variable(s)](#state_variable) - a formal measure that summarizes the state of a community or population at a particular time (Wearn & Glover-Kapfer, 2017) (e.g., species richness or population abundance), and

-   Proposed [modelling approach(es)](#mods_modelling_approach) - the method used to analyze the camera data, which should depend on the [state variable](#state_variable) (e.g., [occupancy models](#mods_occupancy) [MacKenzie et al., 2002], [spatially explicit capture-recapture (SECR) models](#mods_scr_secr) [e.g., Royle et al., 2009] for [density](#density) estimation, etc.) and the [Target Species](#target_species)....

An example of a clearly defined [Survey Objective](#survey_objectives) could be “to monitor trends in wolverine [occupancy](#occupancy) at 5-year intervals from March – December 2020 to 2030 in wildlife management unit 539”.

The [Survey Objective](#survey_objectives) will determine the appropriate [study design](#survey) and [deployment](#deployment) considerations (e.g., [camera spacing](#camera_spacing), [survey](#survey) effort, attractants or not). For example, based on the above objective for our wolverine [occupancy](#occupancy) [project](#project), we “randomly selected [camera locations](#camera_location) within a 15 km x 15 km grid cell with one camera per location and a total of 60 stations across our [study area](#study_area). We will place [lure](#baitlure_lure) dispensers at each [camera location](#camera_location) to increase the likelihood of detecting a wolverine.” to increase the likelihood of detecting a wolverine.”

--- **RCSC et al. (2024)**
:::::

::::::

::::::{tab-item} Visual resources
:::::{grid} 3
:gutter: 1
:padding: 0
:margin: 0

::::{grid-item-card} {{ ref_intext_rcsc_2014b }}
```{figure} ../03_images/03_image_files/00_FIG_obj_state_var.png
:class: img_grid
```

::::

::::{grid-item-card} {{ ref_intext_mccomb_et_al_2010 }}
```{figure} ../03_images/03_image_files/mccomb_et_al_2010_fig4_3_clipped.png
:class: img_grid
```
**McComb et al. (2010) – Fig 4.3**: The components of a monitoring objective.
::::
:::::
::::::

::::::{tab-item} References
{{ ref_bib_caravaggi_et_al_2020 }}

{{ ref_bib_caughley_1977 }}

{{ ref_bib_gotelli_chao_2013 }}

{{ ref_bib_mackenzie_et_al_2002 }}

{{ ref_bib_mccomb_et_al_2010 }}

{{ ref_bib_obrien_2011 }}

{{ ref_bib_pyron_2010 }}

{{ ref_bib_wearn_gloverkapfer_2017 }}
::::::

:::::::

:::::::::