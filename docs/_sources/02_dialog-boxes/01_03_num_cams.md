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
(i_num_cam)=
# {{ title_i_num_cams }}

:::::::{tab-set}

::::::{tab-item} Overview
If you only have a set number of cameras to deploy (e.g., 30), select “Yes” and enter the number of cameras in the numeric field.

If you aren’t limited by a certain number of cameras, select “No” and leave the numeric field blank. If you’re unsure about how many cameras you have or if you would like to see all of the options irrelevant of the number of cameras (e.g., to be gauge your options and/or to determine the number of cameras you need), you can also select “No.” This will allow you to see all of the potential options.

**<font size="4"><span style="color:#2F5496">How does this relate to study design?</font></span>**

The number of cameras available will impact the appropriate modelling approaches, and depend other aspects of your study, such as the rarity of your [Target Species](#target_species).<br>
<br>
“The optimal number of cameras required will be influenced by factors such as landscape heterogeneity, [survey](#survey) duration and spatial scale, species rarity and desired level of precision ({{ ref_intext_colyn_et_al_2018 }}; {{ ref_intext_rovero_et_al_2013 }}). For example, Kays et al. (2020) found that 25–35 cameras were needed for precise estimates of species richness, depending on the spatial scale of the [survey](#survey) and landscape diversity. The number of cameras required for precise estimates of [occupancy](#occupancy) was highly sensitive to the occurrence rate of species, with \<20 cameras required for common species and \>150 cameras required for rare species ({{ ref_intext_kays_et_al_2020 }}). In general, deploying more cameras and/or for longer durations always results in more precise estimates; however, users can consider rotating cameras across multiple sites for shorter durations (if feasible). There are several useful references and applications available to help determine the optimal number of cameras for a [survey](#survey) (e.g., {{ ref_intext_efford_boulanger_2019 }}).<br><br>

When the [objectives](#survey_objectives) and [modelling approach](#mods_modelling_approach) warrant, placing multiple cameras at a site (either on the same attachment point or nearby) can significantly increase the [detection probability](#detection_probability) of less common species (more than increasing the number of [camera days per camera location](#camera_days_per_camera_location); {{ ref_intext_oconnor_et_al_2017 }}; {{ ref_intext_pease_et_al_2016 }}; {{ ref_intext_stokeld_et_al_2016 }}) or be useful for individual identification.”<br>
--- RCSC et al. (2024)

You can refer to [Appendix A - Table A2]( https://ab-rcsc.github.io/RCSC-WildCAM_Remote-Camera-Survey-Guidelines-and-Metadata-Standards/1_survey-guidelines/1_10.1_AppendixA-Tables.html) to get a sense of the required number of cameras for each of the modelling approaches and according to the [Survey Objectives](#survey_objectives).

**RCSC et al. (2024) - Appendix A - Table A2.** Summary of appropriate [study design](#survey), [camera spacing](#camera_spacing), and [survey](#survey) effort (adapted from Wearn & Glover-Kapfer [2017] with additional references included) for various [modelling approaches](#mods_modelling_approach). **Note:** these guidelines use the best available information, however, there is uncertainty associated with each approach. To address this, the table contains ‘minimum,’ ‘ideal’ and ‘often’ used values, as well as qualifiers.

<object data="https://ab-rcsc.github.io/RCSC-WildCAM_Remote-Camera-Survey-Guidelines-and-Metadata-Standards/_downloads/a2c4924f22f971faa27c706b8bb6dd0a/Surv_Guidelines_AppendixA-Table-A2_v2.pdf" type="application/pdf" width="1120px" height="880px">
    <embed src="https://ab-rcsc.github.io/RCSC-WildCAM_Remote-Camera-Survey-Guidelines-and-Metadata-Standards/_downloads/a2c4924f22f971faa27c706b8bb6dd0a/Surv_Guidelines_AppendixA-Table-A2_v2.pdf">
        <p>This browser does not support PDFs. Please download the PDF to view it: <a href="https://ab-rcsc.github.io/RCSC-WildCAM_Remote-Camera-Survey-Guidelines-and-Metadata-Standards/_downloads/a2c4924f22f971faa27c706b8bb6dd0a/Surv_Guidelines_AppendixA-Table-A2_v2.pdf">Download PDF</a>.</p>
    </embed>
</object>  

*Download the PDF*
[Remote Camera Survey Guidelines: Appendix A - Table A2](https://ab-rcsc.github.io/RCSC-WildCAM_Remote-Camera-Survey-Guidelines-and-Metadata-Standards/_downloads/a2c4924f22f971faa27c706b8bb6dd0a/Surv_Guidelines_AppendixA-Table-A2_v2.pdf)
::::::

::::::{tab-item} References
{{ ref_bib_colyn_et_al_2018 }}

{{ ref_bib_efford_boulanger_2019 }}

{{ ref_bib_kays_et_al_2020 }}

{{ ref_bib_oconnor_et_al_2017 }}

{{ ref_bib_pease_et_al_2016 }}

{{ ref_bib_rcsc_et_al_2024 }}

{{ ref_bib_rovero_et_al_2013 }}

{{ ref_bib_stokeld_et_al_2016 }}

{{ ref_bib_wearn_gloverkapfer_2017 }}
::::::

:::::::