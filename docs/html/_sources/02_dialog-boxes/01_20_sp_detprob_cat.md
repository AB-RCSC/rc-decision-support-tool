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
(i_sp_det_prob_cat)=
# {{ title_i_sp_detprob_cat }}

:::::::::{div} full-width

:::::::{tab-set}

::::::{tab-item} Overview
**Detection probability categories are defined as follows:**

- **Low**:
    - < 0.1 ({{ ref_intext_tobler_powell_2013 }})
    - < 0.05 ({{ ref_intext_shannon_et_al_2014 }})
    - 0–0.37 ({{ ref_intext_chatterjee_et_al_2021 }})

- **Medium**: 
    - 0.37–0.67 ({{ ref_intext_chatterjee_et_al_2021 }})

- **High**:
    - 0.67–1 ({{ ref_intext_chatterjee_et_al_2021 }})
    - \> 0.5 ({{ ref_intext_mackenzie_royle_2005 }})

- **Unknown**: select this option if you’re not sure of the detection probability of your [Target Species](#target_species) (single or multiple species)

- **Multiple**: select this option if your study include multiple [Target Species](#target_species).

\
**<font size="4"><span style="color:#2F5496">How this relates to study design</font></span>**

**{{ term_detection_probability }}**: {{ term_def_detection_probability }}

We use this information to adjust the recommended [camera days per camera location](#camera_days_per_camera_location) and [total number of camera days](#total_number_of_camera_days). For example, if the species is hard to detect, you may have to deploy cameras for longer to ensure you’ve sampled long enough to say that the species truly was not there (*vs.* it was there, but you did not detect it; “missed detections”, e.g., high cover of shrubs impeding your ability to see the species).

You may need to consult previous studies to get a sense of which category is the most appropriate for your study and Target Species.

> **Select “Unknown” if you’re not sure.**

\
**<font size="4"><span style="color:#2F5496">How does that work?</font></span>**

Individuals and/or species are not always detected when they are present (i.e., detected "imperfectly”; ({{ ref_intext_mackenzie_et_al_2004 }}). Missed detections occur or many reasons, including due characteristics of the environment (e.g., due to cover of vegetation), the time period (e.g., seasons), characteristics of the species (e.g., cryptic nature or small size), etc. **The question here is asking about detection probability as it relates to the characteristics of the species (not the species in a particular habitat type or during a specific season).**
:::::{grid} 2

::::{grid-item}
:columns: 8

**<font size="4"><span style="color:#2F5496">Why do we care?</font></span>**

When you fail to detect an individual/species that was, in fact, present, this is called a “false absence”, which may lead to incorrect conclusions from the data. Understanding and correcting for sources of this type of error is often thought of in terms of probabilities (i.e., "detection probability" aka detectability).

**Note! It’s not an exact science** - Since detectability is affected by many other processes, it's best incorporated in models (using your data) since this will result in the best suited information to inform your design.
::::

::::{grid-item}
:columns: 4

:::{image} ../03_images/03_image_files/det.gif
:width: 100%
:align: right
:::
::::
:::::
:::::{seealso} Analysis aside
:class: dropdown
Many sources of detection error can be accounted for in analysis; this is done by assessing the relationships between the characteristics of the environment that we might expect to affect detection (e.g., cover of shrubs in front of the camera), and information on where (and when) the species was and was not detected. For example, there were consistently fewer detections on cameras placed in high shrub cover. 

By assessing the relationships at locations repeatedly sampled over time, we begin to unravel the relationship between the environmental characteristics and missed detections on your cameras. We can then use this information to determine if we have sampled long enough (i.e., do we have enough information to differentiate between missed detections and true absences) and/or correct for this error in analysis by incorporating these effects in our models.
:::::
::::::

::::::{tab-item} Advanced
Before study design choices are made, there is one critical concept to understand in remote camera research, which may impact study design choices at all levels of the data hierarchy. Reliable use of remote cameras to detect wildlife species hinges on the [assumption](#mods_modelling_assumption) that what is captured on the cameras accurately reflects what is present on the landscape. However, species are often detected "imperfectly," meaning that they are not always detected when they are present (i.e., [imperfect detection](#imperfect_detection); e.g., due to cover of vegetation, cryptic nature or small size) ({{ ref_intext_mackenzie_et_al_2004 }}). [Imperfect detection](#imperfect_detection) can occur because the camera failed to capture an individual present at the site or because the animal was simply not present during the [survey](#survey) period ({{ ref_intext_martin_et_al_2005 }}).

[Imperfect detection](#imperfect_detection) results in “false absences” and may lead to incorrect conclusions from the data. Understanding and correcting for sources of “false absences” is often thought of in terms of probabilities. [Detection probability](#detection_probability) is the probability (likelihood) that an individual from the population of interest is included in the count at time or location *i* ({{ ref_intext_mackenzie_kendall_2002 }}). [Detection probability](#detection_probability) can be influenced through multiple processes and at multiple scales. Understanding the sources of “false absences” and factors that affect [detection probabilities](#detection_probability) is an essential step when designing a study, deploying cameras and analyzing camera data.

The [detection probability](#detection_probability) of an animal by a camera depends on three **conditional probabilities (Pr) of detection** that may operate alone or potentially in combination ([Figure 1](#TOC_surv_guidelines_fig_1)).

(TOC_surv_guidelines_fig_1)=

```{figure} ../03_images/03_image_files/rcsc_et_al_2024_detection_probability_2023_05_04_clipped.jpg
:height: 700px
:align: center
```

**RCSC et al. (2024) - Fig. 1.** Three conditional probabilities (Pr) of detection that may impact the [detection probability](#detection_probability) of an animal (or species) by a camera (adapted from Moeller et al. \[2023\], Hofmeester et al. \[2019\], and Findlay et al. \[2020\]).

[Detection probability](#detection_probability) can be affected by species-specific characteristics, [Camera Model](#camera_model) specifications and set-up, and environmental variables ({{ ref_intext_hofmeester_et_al_2019 }}). For example, **species-specific characteristics** (individuals or populations), such as body size (e.g., {{ ref_intext_obrien_et_al_2011 }}), behaviour (e.g., {{ ref_intext_caravaggi_et_al_2020 }}; {{ ref_intext_rowcliffe_et_al_2011 }}), and rarity can influence [detection probability](#detection_probability), with larger, bolder and more common species generally having higher [detection rates](#detection_rate). [**Camera Model**](#camera_model) **specifications and set-up**, such as the [Trigger Sensitivity](#settings_trigger_sensitivity), [Camera Height](#camera_height), or [angle](#camera_angle) may affect [detection probability](#detection_probability) in that smaller species might not be detected or identifiable if the [Trigger Sensitivity](#settings_trigger_sensitivity) is low, or the [Camera Height](#camera_height) or [angle](#camera_angle) is too high. The [Camera Direction](#camera_direction) could impact the probability of an animal triggering a camera if it is directed towards an object that impedes the [Field of View (FOV)](#field_of_view) or image quality (e.g. due to sun glare). **Environmental factors** (e.g., vegetation cover, snow depth) may affect [detection probability](#detection_probability) and occurrence (e.g., {{ ref_intext_becker_et_al_2022 }}; {{ ref_intext_hofmeester_et_al_2019 }}; {{ ref_intext_iknayan_et_al_2014 }}; {{ ref_intext_steenweg_et_al_2019 }}). For example, a low number of detections in a densely vegetated site might be because of poor camera visibility or avoidance of this habitat by the species of interest.

Hofmeester et al. (2019) suggested there are **six scales (orders) that may impact** [detection probability](#detection_probability) and that should be considered within an explicit time period (adapted from Hofmeester et al. \[2019\]; [Figure 2](#TOC_surv_guidelines_fig_2)):

1)  **Distribution range** (1st order; i.e., the physical or geographical range of a species)

2)  **Landscape** (2nd order; i.e., the location of an individual’s home range within the geographic range)

3)  **Habitat patch** (3rd order; i.e., usage of habitat components within an individual’s home range)

4)  **Microsite** (4th order; usage of microhabitats such as food items/feeding patches/nest sites/movement trails, etc. within a habitat)

5)  **Camera specification / set-up** (5th order; i.e., factors that affect the probability that an animal [triggers](#trigger_event) the camera if present)

6)  **Image** (6th order; i.e., factors that affect correct identification of animals or individuals)

(TOC_surv_guidelines_fig_2)=

```{figure} ../03_images/03_image_files/rcsc_et_al_2024_detectionprob_hofmeester_et_al_2019_fig1_clipped.png
:width: 700px
:align: center
```

**Figure 2.** Spatial scales (1-6) and processes that determine the [detection probability](#detection_probability) ({{ ref_intext_hofmeester_et_al_2019 }}; abbreviated figure caption).

It is important to consider how all these factors and scales will impact study design. Unmeasured variation in [detection probability](#detection_probability) can result in the inability to differentiate the effects of [detection probability](#detection_probability) *vs.* habitat preference ({{ ref_intext_jennelle_et_al_2002 }}) and, in turn, cause erroneous estimates of occurrence and abundance ({{ ref_intext_burton_et_al_2015 }}; {{ ref_intext_denes_et_al_2015 }}; {{ ref_intext_kays_et_al_2021 }}).

Factors that influence [detection probability](#detection_probability) at the microsite and camera specification / set-up scales are likely to result in the largest biases and thus warrant the most consideration (see Hofmeester et al. [2019] for details). Therefore, it is particularly important to consider *how* to place cameras to avoid such biases. Deploying cameras in a consistent fashion (e.g., carefully ensuring that cameras are always set at the same [Camera Height](#camera_height), orientation ([direction](#camera_direction)), and [angle](#camera_angle) is essential.
::::::

::::::{tab-item} Visual resources
:::::{grid} 3
:gutter: 1
:padding: 0
:margin: 0

::::{grid-item-card} {{ ref_intext_rcsc_et_al_2024 }}
```{figure} ../03_images/03_image_files/rcsc_et_al_2024_detection_probability_2023_05_04_clipped.jpg
:height: 300px
:align: center
```

**RCSC et al. (2024) - Fig. 1.** Three conditional probabilities (Pr) of detection that may impact the detection probability of an animal (or species) by a camera (adapted from Moeller et al. [2023], Hofmeester et al. [2019], and Findlay et al. [2020]).
::::

::::{grid-item-card} {{ ref_intext_rcsc_et_al_2024 }}
```{figure} ../03_images/03_image_files/rcsc_et_al_2024_detectionprob_hofmeester_et_al_2019_fig1_clipped.png
:width: 100%
:align: center
```

**RCSC et al. (2024) - Fig. 2.** Spatial scales (1-6) and processes that determine the detection probability (Hofmeester et al., 2019; abbreviated figure caption).
::::

::::{grid-item-card} {{ ref_intext_tourani_et_al_2020 }}
```{figure} ../03_images/03_image_files/tourani_et_al_2020_fig1_clipped.png 
:width: 100%
:align: center
```

**Tourani et al., (2020) - Fig. 1** Conceptual diagram showing different aspects of detectability during camera trap surveys and the modulating effect of biological characteristics. In addition to direct impacts on detectability, a longer visit and a closer image of focal species increase the chance of identifying the visitor, thereby increasing detectability. Colour figure can be viewed at <zslpublications.onlinelibrary.wiley.com>.

::::

:::::

:::::{grid} 3
:gutter: 1
:padding: 0
:margin: 0

::::{grid-item-card} {{ ref_intext_iknayan_et_al_2014 }}
```{figure} ../03_images/03_image_files/iknayan_et_al_2014_fig2_clipped.png 
:width: 100%
:align: center
```
**Iknayan et al., (2020) - Fig. 2** - Categories of species at surveyed sites resulting from imperfect detection and how they change with different temporal and spatial sampling strategies.

:::{dropdown}
(A) The true (unknown) species pool of a metacommunity represented at a site comprises species that have been detected there (green bin), those that have not yet been detected at the site but have been detected at other surveyed sites (yellow bin), and those that have not yet been detected at this or any site but occur in the region (white bin). (B) As temporal and spatial replication (i.e., sampling effort) increases, knowledge of the species pool changes for both the site (green bins) and the metacommunity (green + yellow + white bins). When a site is surveyed few times, the relative size of each bin depends on the factors affecting detectability (Figure 1). If there are few sites and few surveys per site, a large portion of the metacommunity may not be detected (white bin of upper left rectangle), either at the site or at other sites. As the number of surveys per site increases (temporal replication) but not the number of sites surveyed (i.e., little spatial replication), the total number of species detected per site increases (green bin in upper right rectangle), mostly as a result of detecting species that are likely to occur at other sites (yellow bin). When the total number of sites surveyed increases (spatial replication) but not the number of surveys (i.e., little temporal replication), the number of species undetected in the region decreases (white bin in lower left rectangle), but the number of species detected per site remains the same (green bin). As both the number of surveys per site and the number of sites surveyed increase, a greater proportion of species in the metacommunity will be known (green + yellow bins in lower right rectangle), either from being directly detected at the site (green bin) or by being detected at other sites (yellow bin).
:::
::::

::::{grid-item-card} {{ ref_intext_oconnell_et_al_2011 }}
```{figure} ../03_images/03_image_files/oconnell_et_al_2011_fig6_1_clipped.png 
:width: 100%
:align: center
```
**O’Connell et al. (2011) - Fig. 6.1** The cumulative likelihood of capturing an individual with a Pr(detection) per sampling occasion = *p* over *K* = 1 ... 30 sampling occasions. As *p* and *K* increase, the likelihood of detection approaches 1.
::::

::::{grid-item-card} {{ ref_intext_findlay_et_al_2020 }}
```{figure} ../03_images/03_image_files/findlay_et_al_2020_fig1_clipped.png
:width: 100%
:align: center
```
**Findlay et al. (2020) - Fig. 1** The sequential processes required to detect an animal on a cameratrap given that it is present. Failure of any of these processes leads to a false-negative; therefore, detection success requires a positive outcome from all the component processes. Specific terminology we use in this study to quantify these processes is also shown. ‘Detection probability’ can thus be considered the product of a series of conditional probabilities representing each of these processes.
::::
:::::

:::::{grid} 3
:gutter: 1
:padding: 0
:margin: 0

::::{grid-item-card} {{ ref_intext_turlapaty_2014 }}
<iframe 
    width="100%"
    height="300"
    src="https://www.youtube.com/embed/WBgWOQBlNoI?si=h16_LVMHmwT0ntPd"
    frameborder="0"
    allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture"
    allowfullscreen>
</iframe>

Probability of Detection: Eg 01
::::

:::::

::::::

::::::{tab-item} Shiny apps/Widgets
:::::{card}
::::{dropdown} Probabilistic detection calculator (online application) 
Online application used as an aid in sampling planning; calculates the probability of detecting disease (or other similar feature) with the given within-group prevalence and sample size for both finite and infinite group sizes. The detection means that at least one of the samples is detected positive. The sensitivity of the testing method can also be taken into account in the case of an imperfect test.<br>Additional information can be found here: <https://zenodo.org/records/13120206><br>
({{ ref_intext_mikkela_2024 }})

<iframe 
    width="100%"
    height="900"
    src="https://detcal-shiny.2.rahtiapp.fi/"
    frameborder="0" 
    allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture"
    allowfullscreen>
</iframe>

::::

::::{dropdown} smsPOMDP
A Shiny r app to solve the problem of when to stop managing  or surveying species under imperfect detection.<br>Additional information can be found here: <https://github.com/conservation-decisions/smsPOMDP> or <https://besjournals.onlinelibrary.wiley.com/doi/full/10.1111/2041-210X.13501><br>
({{ ref_intext_pascal_et_al_2020 }})

<iframe 
    width="100%"
    height="900"
    src="https://conservation-decisions.shinyapps.io/smsPOMDP/"
    frameborder="0" 
    allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture"
    allowfullscreen>
</iframe>

::::
:::::
::::::

::::::{tab-item} Analytical tools & resources
| Type | Name | Note | URL |Reference |
|:---------|:---------------------------------------|:----------------------------------------------------------------|:----------------------------------------------------------------|:----------------------------------------------------------------|
| R package | detect: analyzing wildlife data with detection error  | The R package implements models to analyze site occupancy and count data models with detection error. The package development was supported by the Alberta Biodiversity Monitoring Institute and the Boreal Avian Modelling (BAM) Project. | <https://github.com/psolymos/detect>;<br><https://peter.solymos.org/detect> | {{ ref_bib_solymos_et_al_2024 }} |
| R Shiny app | Probabilistic detection calculator (online application) | Online application used as an aid in sampling planning; calculates the probability of detecting disease (or other similar feature) with the given within-group prevalence and sample size for both finite and infinite group sizes.<br><br> Additional information can be found here: <https://zenodo.org/records/13120206>.  | Shiny app: <https://detcal-shiny.2.rahtiapp.fi/>;<br>Related documents: <https://zenodo.org/records/13120206> | {{ ref_bib_mikkela_2024 }} |
::::::

::::::{tab-item} References
{{  ref_bib_rcsc_et_al_2024 }} 

{{ ref_bib_hofmeester_et_al_2019 }}

{{ ref_bib_burton_et_al_2015 }}

{{ ref_bib_caravaggi_et_al_2020 }}

{{ ref_bib_chatterjee_et_al_2021 }}

{{ ref_bib_denes_et_al_2015 }}

{{ ref_bib_findlay_et_al_2020 }}

{{ ref_bib_hofmeester_et_al_2019 }}

{{ ref_bib_iknayan_et_al_2014 }}

{{ ref_bib_jennelle_et_al_2002 }}

{{ ref_bib_kays_et_al_2021 }}

{{ ref_bib_mackenzie_kendall_2002 }}

{{ ref_bib_mackenzie_royle_2005 }}

{{ ref_bib_mackenzie_et_al_2004 }}

{{ ref_bib_martin_et_al_2005 }}

{{ ref_bib_mikkela_2024 }}

{{ ref_bib_moeller_et_al_2023 }}

{{ ref_bib_obrien_et_al_2011 }}

{{ ref_bib_pascal_et_al_2020 }}

{{ ref_bib_rowcliffe_et_al_2011 }}

{{ ref_bib_shannon_et_al_2014 }}

{{ ref_bib_solymos_et_al_2024 }}

{{ ref_bib_tobler_powell_2013 }}

{{ ref_bib_tourani_et_al_2020 }}
::::::

:::::::

:::::::::