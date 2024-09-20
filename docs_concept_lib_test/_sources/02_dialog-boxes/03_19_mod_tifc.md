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
(i_mod_tifc)=
# {{ name_mod_tifc }}

::::::{dropdown} Assumptions, Pros, Cons
:::::{grid}

::::{grid-item-card} Assumptions
- {{ mod_tifc_assump_01 }}
- {{ mod_tifc_assump_02 }}
- {{ mod_tifc_assump_03 }}
::::
::::{grid-item-card} Pros
- {{ mod_tifc_pro_01 }}
- {{ mod_tifc_pro_02 }}
- {{ mod_tifc_pro_03 }}
::::
::::{grid-item-card} Cons
- {{ mod_tifc_con_01 }}
- {{ mod_tifc_con_02 }}
::::
:::::
::::::

:::::::{tab-set}

::::::{tab-item} Overview

**{{ term_mod_tifc }}**: {{ term_def_mod_tifc }}
This section will be available soon! In the meantime, check out the information in the other tabs!

```{figure} ../03_images/03_image_files/00_coming_soon.png
:width: 300px
:align: center
```
::::::

::::::{tab-item} Advanced
:::{note}
**This content was adapted from**: The Density Handbook, "[Using Camera Traps to Estimate Medium and Large Mammal Density: Comparison of Methods and Recommendations for Wildlife Managers](https://www.researchgate.net/publication/368601884_Using_Camera_Traps_to_Estimate_Medium_and_Large_Mammal_Density_Comparison_of_Methods_and_Recommendations_for_Wildlife_Managers)" (Clarke et al.. 2024)
:::

The time in front of the camera (TIFC) model is based on quadrat sampling. Typically, quadrats are used to sample slow- or non-moving organisms at a moment in time; as a simple example, a researcher lays a quadrat on the ground, counts the number of mussels in it and divides the count by the quadrat area. TIFC treats the camera viewshed like a vertical quadrat ({{ ref_intext_becker_et_al_2022 }}; {{ ref_intext_dickie_2022 }}). Unlike a conventional quadrat, however, the camera viewshed samples highly mobile organisms in a relatively small sliver of space and over long periods time ({{ ref_intext_becker_et_al_2022 }}; {{ ref_intext_dickie_2022 }}). The count of animals in the camera viewshed “quadrat,” then, can be thought of in “animal time” and the area covered by the quadrat in “area-time,” such that: </p><br>

```{figure} ../03_images/03_image_files/clarke_et_al_2023_eqn_tifc1.png
:width: 200px
:align: center
```  

**Clarke et al. (2023) – Fig. 8** A) Still from 中島啓裕’s (2021) video series. Example of overlaying a video recording of an animal on a reference image of the focal area (faint triangle) to determine staying time *T*. B) Still from Appendix S2 from Palencia et al. (2021). Example of superimposing the focal area on an image capture.
<br>
<p>where the numerator, animal-time, is the number of animals *N* multiplied by the time those animals spend in the viewshed *T<sub>O</sub>*, summed over all detections; and the denominator, area-time, is the area of the viewshed *A<sub>V</sub>* multiplied by the total camera operating time *T<sub>O</sub>* ({{ ref_intext_becker_et_al_2022 }}). Using this equation, density must be calculated for each species at each camera station, then averaged across the camera network. 

To calculate *A<sub>V</sub>*: in the field, markers (e.g., poles) must be placed at known distances from the camera to divide the viewshed into distance bins; during analysis, the proportion of detections in each bin is determined ({{ ref_intext_becker_et_al_2022 }}). The camera angle of view – which varies with make and model – is also needed to solve for *A<sub>V</sub>*. In most cases, *T<sub>O</sub>* will be the time from initial camera deployment to final camera collection ({{ ref_intext_becker_et_al_2022 }}). In case of displacement, damage or failure, cameras should be programmed to take time-lapse images, so end-of-operation time can be traced back to a specific day or hour ({{ ref_intext_becker_et_al_2022 }}).</p></br>

:::{figure} ../03_images/03_image_files/clarke_et_al_2023_fig9_clipped.png
:width: 350px
:align: center
:::

**Clarke et al. (2023) – Fig. 9**. Examples of behaviours that increase time in the viewshed (*𝑇~𝑣~*). A) A mule deer inspects a camera trap. &copy Cole Burton, Wildlife Coexistence Lab. B) A black bear pulls on the lock securing a camera trap to a tree. &copy Michael Procko, Wildlife Coexistence Lab. 
<br>

## Simulations and Field Experiments (Clarke et al., 2023) 
The TIFC model has been field-tested on several different species. For moose, TIFC produced similar density estimates as aerial distance sampling (DS) after TIFC-derived estimates were corrected for the time animals spent investigating equipment (camera and 5 m pole; {{ ref_intext_becker_et_al_2022 }})). This study used image data collected in Alberta at 2,990 camera stations over the course of 6 years; despite the large sample size and long study duration, estimates were not very precise.<br>

A study of five ungulate species (moose, bison, elk, mule and white-tailed deer) in two enclosed parks in Alberta found that TIFC- and aerial survey-derived density estimates were similar for moose and bison, but that TIFC significantly overestimated elk density compared with aerial surveys ({{ ref_intext_foca_2021 }}). Two potential reasons for the discrepancy in elk density are: 1) that aerial surveys underestimated density, since elk in the study area occupy forested habitats, do not form large herds during the survey period, and estimates were not corrected for sightability; and 2) cameras may have been disproportionately set in areas elk prefer ({{ ref_intext_foca_2021 }}). Group travelling behaviour may also have affected elk TIFC estimates, since detection probability and time in the viewshed (*T<sub>V</sub>*) can change with group size ({{ ref_intext_foca_2021 }}). Estimates of mule and white-tailed deer densities could not be compared with aerial survey results, since deer are not surveyed by air in this area. Foca’s (2021) TIFC analyses produced the first density estimates for deer in both parks.<br>

In Uganda, TIFC-derived estimates of antelope were comparable to results from camera trap spatial capture-recapture (SCR; {{ ref_intext_brownlee_et_al_2022 }}; {{ ref_intext_warbington_boyce_2020 }}). The model performed inconsistently for black bears, caribou, white-tailed deer and other species, however, compared to camera-based spatial count (SC), DNA markre capture and aerial survey methods (Fisher et al. in review).</p>
::::::

::::::{tab-item} Visual resources
:::::{grid} 3
:gutter: 1
:padding: 0
:margin: 0

::::{grid-item-card} {{ ref_intext_clarke_et_al_2023 }}
```{figure} ../03_images/03_image_files/clarke_et_al_2023_eqn_tifc1.png
:class: img_grid
```
**Clarke et al. (2023) - Fig. 8** A) Still from 中島啓裕’s (2021) video series. Example of overlaying a video recording of an animal on a reference image of the focal area (faint triangle) to determine staying time *T*. B) Still from Appendix S2 from Palencia et al. (2021). Example of superimposing the focal area on an image capture. 
::::

::::{grid-item-card} {{ ref_intext_clarke_et_al_2023 }}
```{figure} ../03_images/03_image_files/clarke_et_al_2023_fig9_clipped.png 
:class: img_grid
```
**Clarke et al. (2023) - Fig. 9** Examples of behaviours that increase time in the viewshed (*𝑇~𝑣~*). A) A mule deer inspects a camera trap. &copy Cole Burton, Wildlife Coexistence Lab. B) A black bear pulls on the lock securing a camera trap to a tree. &copy Michael Procko, Wildlife Coexistence Lab. 
::::

::::{grid-item-card} {{ ref_intext_becker_2024 }}
```{figure} ../03_images/03_image_files/becker_2024_slide8.png 
:class: img_grid
```

::::

:::::

:::::{grid} 3
:gutter: 1
:padding: 0
:margin: 0

::::{grid-item-card} {{ ref_intext_becker_2024 }}
```{figure} ../03_images/03_image_files/becker_2024_slide9a.png 
:class: img_grid
```
     
::::

::::{grid-item-card} {{ ref_intext_becker_2024 }}
```{figure} ../03_images/03_image_files/becker_2024_slide12.png 
:class: img_grid
```
   
::::

::::{grid-item-card} {{ ref_intext_becker_2024 }}
<iframe 
    width="100%"
    height="300"
    src="https://drive.google.com/file/d/1IdxQScbzkHd2griu-dEYM4FTFjaXalKe/preview"
    frameborder="0"
    allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture"
    allowfullscreen>
</iframe>

How to estimate density using TIFC; 
Video clip from presentation titled “Comparisons between moose densities with aerial surveys and integrated camera projects”
::::

:::::

::::::

::::::{tab-item} Shiny apps/Widgets
Check back in the future!

::::::

::::::{tab-item} Analytical tools & resources

| Type | Name | Note | URL |Reference |
|:----------------|:---------------------------------------|:----------------------------------------------------------------|:----------------------------------------------------------------|:----------------------------------------------------------------|
| Tutorial | Estimating animal density using TIFC (Time In Front of Camera) | Created by author of TIFC method. | <https://github.com/mabecker89/tifc-method> | {{ ref_bib_becker_et_al_2021 }} |
| R package | abmi.camera.extras |     | <https://mabecker89.github.io/abmi.camera.extras> | {{ ref_bib_becker_et_al_2020 }} |
| Tutorial | abmi.camera.extras: Animal Density from Camera Data |     | Main resource page <https://mabecker89.github.io/abmi.camera.extras/index.html> includes:<br>- [Overview](https://mabecker89.github.io/abmi.camera.extras/articles/overview.html)<br>- [Probabilistic gaps](https://mabecker89.github.io/abmi.camera.extras/articles/gaps.html)<br>- [Time in the camera field of view](https://mabecker89.github.io/abmi.camera.extras/articles/fov.html)<br>- [Effective detection distance](https://mabecker89.github.io/abmi.camera.extras/articles/edd.html)<br>- [Density at individual deployments](https://mabecker89.github.io/abmi.camera.extras/articles/dep-density.html)- [Lure adjustments](https://mabecker89.github.io/abmi.camera.extras/articles/lure.html)<br>- [Density in an area of interest (AOI)](https://mabecker89.github.io/abmi.camera.extras/articles/aoi-density.html)<br>- [Important assumptions](https://mabecker89.github.io/abmi.camera.extras/articles/assumptions.html) | {{ ref_bib_becker_et_al_2020 }} |
::::::

::::::{tab-item} References
{{ ref_bib_becker_et_al_2022 }}

{{ ref_bib_becker_2024 }}

{{ ref_bib_clarke_et_al_2023 }}

{{ ref_bib_dickie_2022 }}

{{ ref_bib_foca_2021 }}

{{ ref_bib_palencia_et_al_2022 }}

{{ ref_bib_warbington_boyce_2020 }}	
::::::

:::::::