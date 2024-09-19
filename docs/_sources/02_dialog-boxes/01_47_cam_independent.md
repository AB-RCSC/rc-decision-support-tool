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
(i_cam_independent)=
# {{ title_i_cam_independent }}

:::::::{tab-set}

::::::{tab-item} Overview
To determine whether your {term}`camera locations <Camera location>` should be treated as independent samples or not, consider the following questions. First, are cameras “sharing” the same animals? If there are multiple cameras within an animal’s home range, the answer is likely “yes” and camera locations are not independent samples. Second, from a statistical perspective, are camera locations close enough together in space that there’s a good likelihood that detection at one camera affects detection at another camera? Or if the same camera locations are sampled repeatedly, is the time frame between surveys so short that detection in one time frame affects the subsequent one? If the answers to one of these questions is “yes”, camera locations should also be treated as dependent samples. The answer to these questions will depend on the biology of the Target Species (e.g., how far they move, and their grouping tendency, territoriality etc.), the survey interval and sampling design. For example, Zuckerberg et al. (2020) illustrate how stratified and systematic non-random designs may lead to biases caused by non-independence of camera locations in some cases (Figures 1 and 3). They also show the implications of independent locations on the number of camera locations. 

Whether camera locations are truly independent or not is important for several reasons. When locations are treated as independent samples, but are in actuality not, they can lead to biased and erroneous results, with potentially serious implications for species management and conservation. Common biases include narrower confidence limits than “truth” (leading to a false sense of certainty of about the results), and underestimated species richness or other metrics. It is also important to know if camera locations are truly independent if you’re interested in estimating occupancy. Knowing this information helps determine whether you’re estimating “probability of occupancy” (such as when camera locations are dependent) or “probability of use” (when locations are independent – e.g. cameras cover only a portion of an individual’s home range; {{ ref_intext_wearn_gloverkapfer_2017 }}).
::::::

::::::{tab-item} Advanced
Spatial autocorrelation (i.e., the tendency for sites that are close together to be more similar) may occur when multiple cameras are placed nearby (such as in clustered, paired or array sampling). Spatial autocorrelation is a form of pseudoreplication (Hurlbert, 1984; when observations are not statistically independent but are treated as if they are) and can be problematic because it can artificially inflate or diminish ecological effects. The degree to which this is a problem will depend on the Target Species (i.e., how far they can travel may dictate the distance at which another camera is too near) and the modelling approach. In these cases, users should consider an analytical framework that accommodates autocorrelation to avoid issues of spatial pseudoreplication ({{ ref_intext_hurlbert_1984 }}) and false conclusions ({{ ref_intext_ramage_et_al_2013 }}) (e.g., using random effects; {{ref_intext_wearn_gloverkapfer_2017 }}] or spatial autoregressive models; {{ ref_intext_kelejian_prucha_1998 }}). 

Note that pseudoreplication ({{ ref_intext_hurlbert_1984 }}) can also occur over time (e.g., if camera locations are sampled repeatedly to obtain detection rates as repeated counts, or if the inter-detection interval is too short for a subsequent detection to be truly independent of the first detection).

In some cases, it is advantageous or required to have dependent detections from multiple cameras. For example, spatially explicit capture-recapture require observations of individual animals at multiple cameras to determine activity centres for density estimation. Furthermore, a clustered or paired study design is often useful when estimating density from individually identifiable species (but see McClintock et al. \[2015\] and Augustine et al. \[2016\] for single camera approaches) or needing to increase detection probability of rare species when single independent cameras are insufficient (e.g., {{ ref_intext_oconnor_et_al_2017 }}). In the latter case, increasing survey effort (e.g., survey duration, more cameras) may achieve the same goal without leading to issues on non-independent samples highlighted above.

**{{ term_spatial_autocorrelation }}**: {{ term_def_spatial_autocorrelation }}

**{{ term_pseudoreplication }}**: {{ term_def_pseudoreplication }}
::::::

::::::{tab-item} Visual resources
:::::{grid} 3
:gutter: 1
:padding: 0
:margin: 0

::::{grid-item-card} {{ ref_intext_zuckerberg_et_al_2020 }}
```{figure} ../03_images/03_image_files/zuckerberg_et_al_2020_fig1_clipped.png
:class: img_grid
```
**Zuckerberg et al. (2020) - Fig. 1** Four experimental designs sampling species occupancy on a theoretical landscape. 
:::{dropdown}
**a** A simple random sampling scheme demonstrating classical pseudoreplication by failing to adequately sample an important environmental predictor (elevation) operating across the study area. . **b** A systematic sampling design with strong replication and landscape coverage, but with significant overlapping of landscape buffers. **c**  A systematic design that attempts to avoid overlap by reducing buffering extent. **d** A systematic design that attempts to avoid overlap by sacrificing sample size.
:::
::::

::::{grid-item-card} {{ ref_intext_zuckerberg_et_al_2020 }}
```{figure} ../03_images/03_image_files/zuckerberg_et_al_2020_fig3_clipped.png 
:class: img_grid
```
**Zuckerberg et al. (2020) - Fig. 3** Four different sampling scenarios superimposed on maps of probability of occurrence aggregated to different scales of resolution to match the corresponding landscape buffer. 
:::{dropdown}
Scenario A implemented a biased sampling scheme with 18 sampling sites stratified by only habitat and ignored the environmental gradient. Scenario B used a regular sampling approach with overlapping landscape buffers. Scenario C used the same sampling sites as scenario B, but with a finer resolution (8-grid cell) to ensure non-overlapping buffers. Scenario D used the same buffer radius as scenarios A and B, but with fewer sampling sites to remove overlapping buffers. Overlapping landscapes were allowed to extend beyond the study region in order to avoid spatial bias towards the center of the landscapes (e.g., mid-domain effect)
:::
::::

:::::

::::::

::::::{tab-item} References
{{ ref_bib_augustine_et_al_2016 }}

{{ ref_bib_oconnor_et_al_2017 }}

{{ ref_bib_hurlbert_1984 }}

{{ ref_bib_kelejian_prucha_1998 }}

{{ ref_bib_mcclintock_et_al_2015 }}

{{ ref_bib_ramage_et_al_2013 }}

{{ ref_bib_wearn_gloverkapfer_2017 }}

{{ ref_bib_zuckerberg_et_al_2020 }}
::::::

:::::::