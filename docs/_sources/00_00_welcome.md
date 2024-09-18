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
# Welcome to the Remote Camera Decision Support Tool!

:::::{grid} 2
:gutter:1
:padding:1

::::{grid-item}
:columns: 9
<font size="4.5"><br>A free, online, interactive, visual study decision support system for remote camera projects</font>

**Last updated**: 2024-09-07

**Version**: v0.1 (Demo)

© Alberta Remote Camera Steering Committee

::::

::::{grid-item}
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
::::
:::::

:::::::{dropdown} Background & Objectives
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

```{figure} ./03_images/meme_wild_west2.png
:width: 200px
:align: center
```
::::

::::{grid-item}
```{figure} ./03_images/00_confusion.png
:width: 300px
:align: center
```
::::

::::{grid-item}

```{figure} ./03_images/what-confused.gif
:width: 200px
:align: center
```
::::
:::::
::::::
:::::::
:::::::{card}

<font size="3"><b>📷 How does it work!?</font></b>

This tool aims to support your decision-making process when designing a remote camera program by guiding you through a series of decision points related to your study in the form of an interactive flow chart.

Once you have answered all of the questions, study design recommendations will be generated from your selections, which will include the following:

::::::{dropdown} Study design recommendations

:::::{grid} 2
:gutter: 2

::::{grid-item-card} Appropriate modelling approach(es)
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
::::

::::{grid-item}

:::{card} Sampling design
*(relevant to the appropriate modelling approach(es) identified)*

- <font size="3">Camera arrangement</font>

- <font size="3">Camera spacing</font>

- <font size="3">Number of camera days per camera location</font>

- <font size="3">Number of cameras</font>

- <font size="3">Survey duration</font>

- <font size="3">Total number of camera days</font>
:::

:::{card} Analysis considerations
*(e.g., variables to consider in your analysis to reduce bias)*
:::

::::
:::::
::::::

At each step, you will be able to access information related to the question in the “info popups” that include tabs with information explained with different levels of complexity (overview vs. advanced) and accessible formats (e.g., figures, videos, Shiny apps, etc.), as well analytical tools and resources. Click on the next dropdown to learn more.

<font size="3"><b>Question framework</font></b>

All questions in the tool have been created to be able to support populating recommendations from a static (non-changing) set of options created from the literature. The main sources include:
- Modifiers in Appendix A - Table A2 of the Remote Camera Survey Guidelines (RCSC et al., 2024)) (e.g., recommendations for the number of cameras required while considering species rarity)
- Clarke et al. (2023)’s “Density Handbook”
- Hofmeester et al.’s (2019) “Figure 2. Questions that lead to selection of covariates for correction in detection...”.
- Other resources with less significant influence

There has ebeen a great interest among the members of the development working group in integrating simulations more directly (e.g., via R Shiny apps that feed into the decision tool branches); we also anticipated that the remote camera community would also find this valuable. We have identified two modeling approaches to “build-out” as more simulation-driven integrations that serve as our trial development modeling approaches. Please refer to {bdg-link-primary-line}`Simulation-driven apps<dev_apps_sim>` below.
:::::::

:::::::{dropdown} 📉 Information formats
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

:::::::

(dev)=
## Development
:::::::{dropdown} 🚀 Shiny apps/Widgets in development
Currently, integrated apps are mostly "illustrative" (for the purpose of illustrating a concept), however, there are a few more intregrated apps in development, which include the following:

**Directly support answering of a specific question**:
- \[ACTIVE\] lookup home range size information from multiple sources

**User tools**:
- \[In development\] populate detection rate from tagged data, and 
- \[In development\] graph detections / detection rates in multiple formats

(#dev_apps_sim)=
**Simulation-driven apps**:
**Occupancy - Spatial power analysis**<br>
(*In development by Dr. Eric Nielsen (Wildlife Research Scientist, Canadian Forest Service; Committee Member, RCSC)*)

```{figure} ./03_images/00_demo_occupancy_app.png
:align: center
:width: 800px
```

**Expected precision of density estimates using Time in Front of the Camera (TIFC)**<br>
(*In development by Marcus Becker (Reporting Analyst, ABMI [Science Centre]; Committee Member, RCSC)*)
```{figure} ./03_images/00_demo_tifc_app.gif
:width: 800px
:align: center
```

These apps will soon be embedded available as separate, standalone apps, and eventually, incorporated into the decision-tree components of the tool (and thus use simulated information to provide more informed recommendations).
<!--
::::{admonition} It’s not an exact science
:class: warning

We're still working on this section! 

(!!!ADD INFO - Caveat about limitations)
It's not perfect, and we don't expect it ever will be! It would be essentially impossible to provide a tool that could provide everyone with the perfect study design.

Additionally, just as the documents upon which this tool is based are meant to evolve with best practices, so will this tool.

> It's not rocket science, but it IS remote camera science...
-- Marcus Becker
::::-->
:::::::

:::::::{dropdown} 🔭 Future development
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
:::::::

***
(contact-us)=
## Contact us
<!--If you have questions or would like further information, please contact Cassie Stevenson, Alberta Remote Camera Steering Committee (RCSC) / Alberta Biodiversity Monitoring Institute (ABMI), <abwildlifecameras@gmail.com>; <cjsteven@ualberta.ca>.-->
If you have questions or would like further information, or if you have feedback or a feature request, please contact us. We'll get in touch as soon as we can.

:::::::{dropdown} Question, feedback, or feature request?
::::::{card}
<div align="center"><iframe id="JotFormIFrame-241017573726052" title="Contact us" onload="window.parent.scrollTo(0,0)" allowtransparency="true" allow="geolocation; microphone; camera; fullscreen" src="https://form.jotform.com/241017573726052" frameborder="0" style="min-width:100%;max-width:100%;height:300px;border:none;" scrolling="no" > </iframe> <script src='https://cdn.jotfor.ms/s/umd/latest/for-form-embed-handler.js'></script> <script>window.jotformEmbedHandler("iframe[id='JotFormIFrame-241017573726052']", "https://form.jotform.com/")</script></div>
::::::
:::::::

:::::::{dropdown} Have resources to contribute?
::::::{card}
<div align="center">
    <iframe
      id="JotFormIFrame-242607211652247"
      title="RC Tool User Submissions"
      onload="window.parent.scrollTo(0,0)"
      allowtransparency="true"
      allow="geolocation; microphone; camera; fullscreen"
      src="https://form.jotform.com/242607211652247"
      frameborder="0"
      style="min-width:100%;max-width:100%;height:300px;border:none;"
      scrolling="no"
    >
    </iframe>
    <script src='https://cdn.jotfor.ms/s/umd/latest/for-form-embed-handler.js'></script>
    <script>window.jotformEmbedHandler("iframe[id='JotFormIFrame-242607211652247']", "https://form.jotform.com/")</script>
</div>
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