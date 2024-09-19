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
(i_sp_size)=
# {{ title_i_sp_size }}
:::{note}
Unsure about the size of your Target Species? Check out the “Shiny Apps/Widgets” tab to see if information for your Target Species is available for in our “Species home range / body size lookup.”
:::

:::::::{tab-set}

::::::{tab-item} Overview
Here are a few examples of comparable species for each body size options:
- **Small**: rodents and similarly sized species in the “Mustelidae” family [i.e., weasels, badgers, otters, martens, wolverine, etc.])
- **Medium**:  small and mid-sized species, ~< 33 lbs (or 15 kilograms), such as meso-carnivores (i.e., Red, fox, Coyote) ({{ ref_intext_roemer_et_al_2009 }})
- **Large**:  bears or ungulates (i.e., large mammals with hooves, such as White-tailed deer, Elk, Moose, etc)
- **Multiple** - *select this option if your study includes multiple Target Species that vary in body size.*

**<font size="4"><span style="color:#2F5496">How does this relate to study design?</font></span>**

Body size affects the detection process (O’Brien et al., 2011). Species with a larger body size are more likely to be detected; and therefore may require lower sampling effort than smaller species ({{ ref_intext_chatterjee_et_al_2021 }}). Larger species moving through the camera’s detection zone are more likely to trigger the camera ({{ ref_intext_chatterjee_et_al_2021 }}; {{ ref_intext_rowcliffe_et_al_2011 }}; {{ ref_intext_hofmeester_et_al_2017 }}); they can also be detected farther away or occur at wider angles ({{ ref_intext_rowcliffe_et_al_2011 }}; {{ ref_intext_hofmeester_et_al_2017 }}). Whereas, small mammals are often undetected due to their small size (O’Brien,  Kinnaird, and Wibisono 2011; {{ ref_intext_anile_devillard_2016 }}) and because “small species which routinely move at fast speeds, such as stoats and weasels, are likely to have especially small detection zones” (Glen et al., 2013).

```{figure} ../03_images/03_image_files/kays_et_al_2021_fig6_clipped.png
:align: center
:width: 700px
```
**Kays et al. (2021) - Fig. 6**: Relationship between trigger probability and body mass for four focal species (ascending order by weight: gray fox, raccoon, coyote, white-tailed deer). Error bars show standard deviation. Body mass values come from North Carolina animals in the mammal collections of the NC Museum of Natural Sciences

When thinking beyond the camera's FOV, larger species generally also have larger home ranges (Garland, 1983) and daily movement distances, making them more likely to be detected at multiple cameras {{ ref_intext_chatterjee_et_al_2021 }}, therefore there are also implications for which models may be appropriate (due to assumptions of “site closure” / “independent locations”).

:::{note}
This is an especially important consideration when targetting multiple species of varying sizes.
:::

::::::

::::::{tab-item} Visual resources
:::::{grid} 3
:gutter: 1
:padding: 0
:margin: 0

::::{grid-item-card} {{ ref_intext_kays_et_al_2021 }}
```{figure} ../03_images/03_image_files/kays_et_al_2021_fig6_clipped.png
:class: img_grid
```
**Kays et al. (2021) - Fig. 6**: Relationship between trigger probability and body mass for four focal species (ascending order by weight: gray fox, raccoon, coyote, white-tailed deer). Error bars show standard deviation. Body mass values come from North Carolina animals in the mammal collections of the NC Museum of Natural Sciences
::::

::::{grid-item-card} {{ ref_intext_anile_devillard_2016 }}
```{figure} ../03_images/03_image_files/anile_devillard_2016_fig2.jpg
:class: img_grid
```
::::

::::{grid-item-card} {{ ref_intext_anile_devillard_2016 }}
```{figure} ../03_images/03_image_files/anile_devillard_2016_fig3.png
:class: img_grid
```
::::

:::::

:::::{grid} 3
:gutter: 1
:padding: 0
:margin: 0

::::{grid-item-card}
```{figure} ../03_images/03_image_files/no_ref/bodysize_movement.png 
:class: img_grid
```
::::

::::{grid-item-card} {{ ref_intext_fisher_et_al_2011 }}
```{figure} ../03_images/03_image_files/fisher_et_al_2011_fig6.png 
:class: img_grid
```
::::

::::{grid-item-card} {{ ref_intext_chatterjee_et_al_2021 }}
```{figure} ../03_images/03_image_files/chatterjee_et_al_2021_table2.png
:class: img_grid
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

::::::{tab-item} References
{{ ref_bib_anile_devillard_2016 }}

{{ ref_bib_broekman_et_al_2022 }}

{{ ref_bib_burton_et_al_2015 }}

{{ ref_bib_chatterjee_et_al_2021 }}

{{ ref_bib_fisher_et_al_2011 }}

garland_1983

{{ ref_bib_glen_et_al_2013 }}

{{ ref_bib_hofmeester_et_al_2017 }}

{{ ref_bib_jones_et_al_2009 }}

({{ ref_bib_kays_et_al_2021 }}

{{ ref_bib_labarbera_1989 }}

{{ ref_bib_obrien_et_al_2011 }}

{{ ref_bib_roemer_et_al_2009 }}

{{ ref_bib_rowcliffe_et_al_2011 }}

{{ ref_bib_rowcliffe_et_al_2011 }}
::::::

:::::::