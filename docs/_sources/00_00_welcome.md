---
jupytext:
  formats: md:myst
  text_representation:
    extension: .md
    format_name: myst
    format_version: '1.16'
    jupytext_version: 1.16.1
kernelspec:
  display_name: Python 3
  language: python
  name: python3
editor_options:
  markdown:
    wrap: none
---
<style>
.bd-main .bd-content .bd-article-container {
    max-width: 85%;  /* default is 60em */
  }
.bd-page-width {
    max-width: 85%;  /* default is 88rem */
}

h1 {
    font-size: 2rem;
    font-weight: bold;
}

h2 {
    font-size: 1.5rem;
    font-weight: bold;
    color: #2F5496
}
h3 {
    font-size: 1.5rem;
    font-weight: normal;
    font-style: italic;
    color: #2F5496
}
</style>
(home)=
# Welcome to the Remote Camera Decision Support Tool!
:::::::{grid} 2
:gutter:1
:padding:1

::::::{grid-item}
:columns: 9
<font size="4.5"><br>A free, online, interactive, visual study decision support system for remote camera projects</font>

**Last updated**: 2024-09-26

**Version**: v0.1 (Demo)

© Alberta Remote Camera Steering Committee

::::::
::::::{grid-item}
:columns: 3
<br>

:::{figure} ./logo.png
:width: 100%
:align: left
:::

```{button-link} http://www.rc-decision-support-tool.ca/voila/render/objective.ipynb?
:color: primary
:shadow:
:align: center
Launch the tool
```
 <!--#00827b-->
```{button-link} https://ab-rcsc.github.io/rc-decision-support-tool_concept-library
:color: primary
:shadow:
:align: center
Concept library
```
::::::
:::::::

::::::{dropdown} Background & Objectives
**<font size="4"><span style="color:#2F5496">Background</font></span>**

In 2020, the Alberta Remote Camera Steering Committee (RCSC) merged with the B.C. Wildlife Camera Committee to form WildCAM (Wildlife Cameras for Adaptive Management; <https://wildcams.ca/>) to form a remote camera network for Western Canada. This collaboration aims to address a need for tools, standards, and opportunities for sharing knowledge among remote camera users across Western Canada. 

For the past year, the RCSC has developed two companion documents, the [Remote Camera Metadata Standards for Alberta](https://ab-rcsc.github.io/RCSC-WildCAM_Remote-Camera-Survey-Guidelines-and-Metadata-Standards/2_metadata-standards/2_0.1_Citation-and-Info.html) (RCSC, 2023) and [Remote Camera Survey Guidelines](https://ab-rcsc.github.io/RCSC-WildCAM_Remote-Camera-Survey-Guidelines-and-Metadata-Standards/1_survey-guidelines/1_0.1_Citation-and-Info.html) (RCSC et al., 2023), which relate to several supporting documents and tools, including standardized [deployment and service/retrieval fieldsheets](https://ab-rcsc.github.io/RCSC-WildCAM_Remote-Camera-Survey-Guidelines-and-Metadata-Standards/1_survey-guidelines/1_10.2_AppendixA-Field-Datasheets.html), an “[EpiCollect Template](https://five.epicollect.net/project/rcsc-and-wildcam-remote-camera-survey-guidelines)” (ESRI Survey123 pending), and FWMIS loadforms (<https://www.alberta.ca/wildlife-loadforms.aspx>; available soon).

These standards and guidelines provide guidance on the types of data that should be collected and how it should be documented when using remote cameras to detect wildlife, and offer recommendations on appropriate survey design, deployment methods and data management. The RCSC aims to ensure that the resources they develop are getting into the hands of remote camera users and are inclusive of their needs, level of expertise, and feedback. Yet, as the development of such standards and tools was realized, the RCSC identified multiple factors that inhibit the ability of such standards and tools to have an impact on the ground via awareness, understanding, and buy-in from the community. The RCSC identified the need for:
- **novel approaches to engage remote camera users to ensure** resources are available and accessible, and representative of the needs of diverse remote camera users throughout Western Canada, and
- **novel approaches to disseminate information to remote camera users** since there are many groups of remote camera users in Western Canada with diverse objectives and varying levels of expertise, access to information (e.g., publications), and constraints in the delivery of remote camera programs (e.g., digital data and broadband issues, scientific literacy, etc.), as well as differing scales of study or capacity.

**<font size="4"><span style="color:#2F5496">Objective</font></span>**

This project aims to mobilize the knowledge outlined in the [Remote Camera Metadata Standards for Alberta](https://ab-rcsc.github.io/RCSC-WildCAM_Remote-Camera-Survey-Guidelines-and-Metadata-Standards/2_metadata-standards/2_0.1_Citation-and-Info.html) (RCSC, 2023) and [Remote Camera Survey Guidelines](https://ab-rcsc.github.io/RCSC-WildCAM_Remote-Camera-Survey-Guidelines-and-Metadata-Standards/1_survey-guidelines/1_0.1_Citation-and-Info.html) (RCSC et al., 2023) to create a freely available, interactive, accessible online tool (i.e., the “**Remote Camera Decision Support Tool**”). This tool will guide users through choices encountered when designing a remote camera study, suggest design choices, and provide related resources.

Users will be guided through a series of decision points related to their study. At each step, users will be able to access information related to the question itself, the impacts of the various choices on study design, or important related topics via “pop-up” boxes; information tabs include multiple tabs for information in different levels of complexity (new vs. advanced user) and formats (e.g., descriptions, figures, videos, Shiny apps, etc.).

Study design recommendations will be generated from as a standardized report that will include: a) appropriate modelling approach(es) (e.g., density – spatially explicit capture-recapture), a b) study design recommendations (e.g., camera spacing, number of cameras, etc.), and c) analysis considerations (e.g., variables to consider in your analysis to reduce bias). 

::::::{dropdown} Sparknotes rationale

:::::{grid} 3

::::{grid-item}
:::{figure} ./03_images/meme_wild_west2.png
:width: 200px
:align: center
:::
::::

::::{grid-item}
:::{figure} ./03_images/00_confusion.png
:width: 300px
:align: center
:::
::::

::::{grid-item}
:::{figure} ./03_images/what-confused.gif
:width: 200px
:align: center
:::
::::
:::::
::::::
:::::::
:::::::{card}
**<font size="4.5"><span style="color:#2F5496">📷 How does it work!?</font></span>**

This tool aims to support your decision-making process when designing a remote camera program by guiding you through a series of decision points related to your study in the form of an interactive flow chart.

Once you have answered all of the questions, **study design recommendations will be generated from your selections**, which will include the following:
::::::{dropdown} Recommendations

:::::{grid} 2
:gutter: 2

::::{grid-item}

:::{card} Appropriate modelling approach(es)
- <font size="3">Species inventory</font>

- <font size="3">Species diversity & richness</font>

- <font size="3">Relative abundance indices</font>

- <font size="3">Capture-recapture (CR) / Capture-mark-recapture (CMR)</font>

- <font size="3">Spatial capture-recapture (SCR) / Spatially explicit capture recapture (SECR)</font>

- <font size="3">Spatial mark-resight (SMR)</font>

- <font size="3">Spatial count (SC) model / Unmarked spatial capture-recapture</font>

- <font size="3">Spatial Partial Identity Model (Categorical SPIM; catSPIM)</font>

- <font size="3">Spatial Partial Identity Model (2-flank SPIM)</font>

- <font size="3">Random encounter model (REM)</font>

- <font size="3">Random encounter and staying time (REST)</font>

- <font size="3">Time in front of the camera (TIFC)</font>

- <font size="3">Distance sampling (DS)</font>

- <font size="3">Time-to-event (TTE)</font>

- <font size="3">Space-to-event (STE)</font>

- <font size="3">Instantaneous sampling (IS)</font>

- <font size="3">Behaviour</font>
:::

:::{card} Sampling design
*(relevant to the appropriate modelling approach(es) identified)*
- <font size="3">Camera arrangement</font>
- <font size="3">Camera spacing</font>
- <font size="3">Number of camera days per camera location</font>
- <font size="3">Number of cameras</font>
- <font size="3">Survey duration</font>
- <font size="3">Total number of camera days</font>
:::

::::

::::{grid-item}
:::{card} Analysis considerations
I.e., variables to consider in your analysis to reduce bias. For example:
| Because you chose… | Consider the following in your analysis | 
|:------------------------|:-----------------------------------------------|
| Multiple study areas | Include latitude, topography, temp, and or NVDI as covariates in analysis (Hofmeester et al., 2019). | 
| Multiples study seasons | Correct for multiple seasons by including season or temperature as covariates (Hofmeester et al., 2019). | 
| Bait/lure placed at a subset of cameras | Correct for variability in bait/lure effects by including bait/lure presence as a covariate. | 
| Variable camera settings | Include each setting that differs as a covariate. | 
| Targetting multiple features | Correct for variable placement on detection probability by including FOV Target Feature "type" as a covariate. | 
| Variable camera make/model | measure sensitivity of PIR sensor of each model and use as a covariate (Hofmeester et al., 2019) or include camera model as a covariate (Kelly & Holub, 2015). | 
| Variable camera height and/or angle | include camera height and/or camera angle as covariates (Hofmeester et al., 2019). | 
| Target species - Body size\["Multiple" or "Unknown"\] | correct for variable body size of your target species by including body mass and diet as variables (O’Brien, Kinnaird, and Wibisono 2011; Hofmeester et al., 2019). |
| ... | ... |
:::::
::::::

At each step, you will be able to access information related to the question in the “info popups” that include tabs with information explained with different levels of complexity (overview vs. advanced) and accessible formats (e.g., figures, videos, Shiny apps, etc.), as well analytical tools and resources. Click on the next dropdown to learn more.

::::::{dropdown} 📉 Information formats
Information is available in the following tabs of the "info popups":
- **Overview** (default) \- short, digestible information about the topic.

- **Advanced** \- detailed descriptions; more “in the weeds” information for those who want to dig into the details.

- **Visual resources** \- related figures and videos; you can watch videos within in tool itself or click on the links within the embedded video to open YouTube.

- **Shiny apps/Widgets** \- access externally created apps already hosted online. Note that the apps included in the tabbed content mainly serve a supplemental material, however we are developing in Shiny apps/Widgets that more directly support users’ answering of a specific question and that can help to tailor recommendations to users' needs more specifically via simulation-based (apps). Refer to the next section for more information.

- **Analytical tools & resources** \- resources for implementing analyses provided as links to R packages or scripts.

- **References** \- references for all of the content in this section.

:::{card}
**Note**: contents of info popups is always available in the **[Concept Library](https://ab-rcsc.github.io/rc-decision-support-tool_concept-library/)**
:::
::::::

**<font size="4"><span style="color:#2F5496">Question framework</font></span>**

All questions in the tool have been created to be able to support populating recommendations from a static (non-changing) set of options created from the literature. The main sources include:
- Modifiers in Appendix A - Table A2 of the Remote Camera Survey Guidelines (RCSC et al., 2024)) (e.g., recommendations for the number of cameras required while considering species rarity)
- Clarke et al. (2023)’s “Density Handbook”
- Hofmeester et al.’s (2019) “Figure 2. Questions that lead to selection of covariates for correction in detection...”.
- Other resources with less significant influence

::::::{dropdown} Question included in Phase 1.0
| Level of design | Question | Options |
|:--------------------------|:-----------------------------------------------|:-------------------------------------|
| Objectives & Resources | Are you looking to design a new remote camera project, or analyze data that was already collected? | Design a new remote camera project, Analyze data that was already collected |
| Objectives & Resources | What's your objective?<br>Select "Unknown" if you're not sure. | Species inventory, Species diversity & richness, Occupancy, Relative abundance, Absolute abundance, Population size, Density, Vital rates, Behaviour, Unknown |
| Objectives & Resources | Do you have a limited number of cameras?<br>If so, how many? | YES, NO |
| Study area & Site selection constraints | Do you plan to use data from multiple study areas? | YES, NO |
| Study area & Site selection constraints | Will you place cameras across a known density gradient? | YES, NO |
| Equipment & Deployment | Was the Camera Direction either random or consistent? | YES, NO |
| Study area & Site selection constraints | Do you plan to strategically place camera locations to include multiple habitats or otherwise differing categories (e.g., different land cover types, or near vs. far from a disturbance)?<br>If so, how many covariates? (e.g., 5 different habitat types would be 5 covariates) | YES, NO |
| Study area & Site selection constraints | Can cameras be deployed close together (i.e., high camera density)? | YES, NO |
| Duration & Timing | Is there a maximum number of months you can sample?<br>If so, how many? | YES, NO |
| Duration & Timing | Is there a minimum number of months you can sample in total?<br>If so, how many? | YES, NO |
| Duration & Timing | How many months did you sample in total? | \[numeric\] |
| Duration & Timing | Do you wish to sample long enough to reach the species-accumulation asymptote? | YES, NO, I'm not sure |
| Duration & Timing | How many seasons will the study contain? | \[numeric\] |
| Target species | Are you sampling for a single species or multiple? | Single, Multiple |
| Target species | How well is the biology about of the Target Species known? | Poorly known, Well known, I'm not sure |
| Target species | Is the Target Species a carnivore or ungulate? | Carnivore, Ungulate, Other |
| Target species | Does the Target Species occur in low density? | YES, NO, I'm not sure |
| Target species | Is the distribution of the Target Species highly restricted? | YES, NO, I'm not sure |
| Target species | Is home range size information available for your Target Species (can be taken from the literature)?<br>If so, enter the home range diameter (in metres) | YES, NO |
| Target species | Are all of the Target Species within a same body size category?<br>If so, which category? | Small, Medium, Large, Multiple |
| Target species | What is the approximate size of the Target Species? | Small, Medium, Large, Multiple |
| Target species | Are all of the Target Species similarly rare or common?<br>If all are similar, which best describes the Target Species rarity? | Common, Less common, Rare, Very rare, Unknown, Multiple |
| Target species | How rare or common is the Target Species? | Common, Less common, Rare, Very rare, Unknown, Multiple |
| Target species | Are all of the Target Species similarly detectable?<br>If all are similar, which best describes the Target Species detectability? | Low, Medium, High, Unknown, Multiple |
| Target species | How detectable is the Target Species? | Low, Medium, High, Unknown, Multiple |
| Target species | Is the Target Species known or likely to investigate the camera (e.g., moose, coyote) or be camera shy (e.g., lynx)? | Exploratory, Neutral, Avoidant, I'm not sure, Variable |
| Target species | Does the \[or one of the, if multiple\] Target Species' behaviour vary by season? | YES, NO, I'm not sure |
| Target species | Do individuals have natural or artificial marks such that they can be uniquely identified?<br>(i.e. are the individuals, population, or species "marked," "unmarked," or "partially marked") | Marked, Partially marked, Unmarked |
| Target species | Are ALL or a SUBET individuals naturally/artifically marked? | All, Subset |
| Target species | Are there 3+ categories of traits that can be be used to identify individuals?<br> (i.e., information used to identify individuals that can be divided into distinct groups, e.g, sex class, age class, coat colour, markings and antler point count; Clarke et al., 2023) | YES, NO |
| Target species | Can additional information be collected/accessed?<br> If so, what type? | Cannot be collected, Distance from animals to the camera, Animal movement speed, Collecting time-lapse images, Measuring time individuals spend in front of the camera, None of these options |
| Target species | Can counts of individuals be determined? | YES, NO |
| Target species | Focal area measured or detections binned by distance? | Measured, Binned |
| Target species | Is the study population large? | YES, NO |
| Target species | Are all of the "target species" similarly likely to investigate the camera or stake?<br>(e.g., moose, coyote) or be camera shy (e.g., lynx)<br>If all are similar, which best describes the likelihood of investigating the camera? | Same behaviour - Exploratory, Same behaviour - Neutral, Same behaviour - Avoidant, I'm not sure, Variable |
| Target species | Which option best categorizes the rarest Target Species? | Common, Less common, Rare, Very rare, Unknown, Multiple |
| Target species | Which option best categorizes the most common Target Species? | Common, Less common, Rare, Very rare, Unknown, Multiple |
| Target species | How detectable is the most detectable Target Species? | Low, Medium, High, Unknown, Multiple |
| Target species | How detectable is the least detectable Target Species? | Low, Medium, High, Unknown, Multiple |
| Equipment & Deployment | Do you plan to use cameras of the same make and model? | YES, NO |
| Equipment & Deployment | Do you plan to use data from cameras with different settings?<br>(e.g., if pooling data from multiple studies, protocols for camera settings may differ) | YES, NO |
| Equipment & Deployment | Was the placement Camera Height and Camera Angle consistent or variable across Camera Locations? | Consistent, Variable |
| Equipment & Deployment | Do you plan to use bait or lure?<br>If so, will you use the same type of bait or lure, or multiple types? | No bait/lure, YES - single type of bait/lure, YES - Multiple types of bait/lure |
| Equipment & Deployment | Will bait/lure be placed at all or a subset of Camera Locations? | All Camera Locations, A subset of Camera Locations |
| Equipment & Deployment | Do you plan to target specific feature(s)?<br>(e.g., facing the camera towards a game trail or mineral lick) | YES, NO |
| Equipment & Deployment | Will all cameras target the same feature? | YES, NO |
| Data & Analysis | Will each camera location be treated as an independent sample? | YES, NO |
| Data & Analysis | Will you collect multiple samples from the same location? |, NO |
| Data & Analysis | Are you using / <br>Do you plan to use mixed models? | YES, NO |
| Data & Analysis | How many independent detections? | [numeric] |
| Data & Analysis | How many individuals were detected? | [numeric] |
| Data & Analysis | How many recaptures were detected? | [numeric] |
| Data & Analysis | Is the data overdispersed?<br>\[Poisson GLM vs. negative binomial model\] | YES, NO |
| Data & Analysis | Is the data zero-inflated? \[Poisson / Negative binomial vs. Zero-inflated / Hurdle models\] | YES, NO |
| Data & Analysis | Try using a zero-inflated model. Is overdispersion still present when accounting for by zero-inflation?<br> (i.e., is the zero-inflated model still overdispersed) \[Zero-inflated poisson vs. Zero-inflated negative binomial model\] | YES, NO |
| Data & Analysis | Try including a random effect for "Camera Location." Is the data still zero-inflated when accounting for a "Camera Location" random effect? \[Zero-inflation due to spatial autocorrelation of sites; mixed effects model\] | YES, NO |
| Data & Analysis | Do you believe that another process may be contributing to excess zeros? [Zero-inflation poisson vs. Hurdle model] | YES, NO |
::::::

:::::{note} 
Don't forget to check out {bdg-link-primary-line}`development<dev>` (below) before you leave; we've got exciting {bdg-link-primary-line}`Shiny apps/Widgets in development<dev>`.
:::::
:::::::
:::::::{card}
(#dev)=
**<font size="4.5"><span style="color:#2F5496">Development</font></span>**

::::::{dropdown} 🚀 Shiny apps/Widgets in development
Currently, integrated apps are mostly “illustrative” (for the purpose of illustrating a concept), however, there are a few more helpful apps in development; some of these include apps that **a) directly support answering of a specific question** within the RC Decision Support Tool and **b) other generally useful "user tools"**). As well, the RC Decision Support Tool working group was very interested in integrating simulations more directly  to be able to provide data-driven recommendations that are more fine-tuned to your study (i.e., **c) data/simulation-driven apps** that feed into the decision tool branches); we also anticipated that the remote camera community would also find this valuable. 

**Directly support answering of a specific question:**
- "Species home range / body size lookup" - lookup home range size information from multiple sources. \[ACTIVE; try it out {bdg-link-primary-line}`here<https://ab-rcsc.github.io/rc-decision-support-tool_concept-library/02_dialog-boxes/01_17_sp_hr_size.html#hr_body_size_lookup>`\]

:::{figure} ./03_images/home_range_lookup.png
:align: center
:width: 500px
:name: demo_hr_body_size_lookup
:::

**User tools**:
- Populate detection rate from tagged data \[In development\]
- Graph detections / detection rates in multiple formats \[In development\]

(#dev_apps_sim)=
**Data/Simulation-driven apps**:
We have identified two modeling approaches to “build-out” as more simulation-driven integrations that serve as our trial development modeling approaches.

**Occupancy - Spatial power analysis**<br>
(*In development by Dr. Eric Nielsen (Wildlife Research Scientist, Canadian Forest Service; Committee Member, RCSC)*)

:::{figure} ./03_images/00_demo_occupancy_app.png
:align: center
:width: 800px
:name: demo_occupancy
:::

**Expected precision of density estimates using Time in Front of the Camera (TIFC)**<br>
(*In development by Marcus Becker (Reporting Analyst, ABMI \[Science Centre\]; Committee Member, RCSC)*)
:::{figure} ./03_images/00_demo_tifc_app.gif
:width: 800px
:align: center
:name: demo_tifc
:::

These apps will soon be embedded available as separate, standalone apps, and eventually, incorporated into the decision-tree components of the tool (and thus use simulated information to provide more informed recommendations).
::::::

::::::{dropdown} 🔭 Future development
We have big plans! As the "demo" version of this tool develops, we will provide more details. For now, please see the following items on docket for 2025-26: 

Appropriate modelling approach(es)
- Species diversity & richness
    - Alpha richness (α)
    - Gamma richness (γ)
    - Beta-diversity (β)
- Relative abundance indices
    -  Poisson
    -  Zero-inflated poisson (ZIP)
    -  Negative binomial (NB)
    -  Zero-inflated negative binomial (ZINB)
    -  Hurdle
- Royle-Nichols
- **N-mixture
- Behaviour - More specific approaches related to behaviour

📉 Information formats
- Executable Code \- We also aim to include an “Executable code” tab in future. 

Please refer back; we will update this section continually.
::::::
:::::::
:::::::{card}
(#contact-us)=
**<font size="4.5"><span style="color:#2F5496">Contact us</font></span>**

Have questions, feedback, or a feature request? Have resources to contribute? Please contact us. We'll get in touch as soon as we can.

:::::::{dropdown}
::::::{card}
<iframe class="airtable-embed" src="https://airtable.com/embed/appEK23r7kkCemnRA/pagDjFn6B7yM8TMMB/form" frameborder="0" onmousewheel="" width="100%" height="910" style="background: transparent; border: 1px solid #ccc;"></iframe>
::::::
:::::::

***

:::::::{grid} 5
:gutter: 1

::::{grid-item}
:::{image} ./02_logos/aca_ed.png
:align: center
:::
::::

::::{grid-item}
:::{image} ./02_logos/abgov_ed.png
:align: center
:::
::::

::::{grid-item}
:::{image} ./02_logos/eccc_ed.png
:align: center
:::
::::

::::{grid-item} 
:::{image} ./02_logos/fos_ed.png
:align: center
:::
::::

::::{grid-item} 
:::{image} ./02_logos/abmi_ed.png
:align: center
:::
::::
:::::::

***

*<font size="2">This project was funded by the Alberta Conservation Association (ACA)m the Office of the Chief Scientist (OCS), and Environment and Climate Change Canada (ECCC). This project was provided in-kind support by the Alberta Remote Camera Steering Committee (RCSC), Alberta Environment and Protection Areas (EPA), Alberta Biodiversity Monitoring Institute (ABMI), and the University of Alberta Faculty of Science.</font>*
<br>

***
::::::::