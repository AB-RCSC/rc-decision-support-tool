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
:::::::{grid} 2
:gutter:2
:padding:2
:margin:0

::::::{grid-item}
:columns: 8

(home)=
# Welcome to the Remote Camera Decision Support Tool!

<br>
</br>
<font size="4.5">A free, online, interactive, visual study decision support system for remote camera projects</font>
<font size="4.5"><span style="color:whitesmoke">.</font></span>
<font size="4.5"><span style="color:whitesmoke">.</font></span>
  
**Last updated**: 2024-11-17

**Version**: v0.1 (Demo)

© Alberta Remote Camera Steering Committee<br>
<br>
<br>
<br>
<br>
<br>
*<font size="2">The Alberta Remote Camera Steering Committee (RCSC) respectfully acknowledges that we are located on the traditional lands of Treaties 4, 6, 7, 8, and 10. This territory has been traditional and ancestral land of the Cree, Dene, Blackfoot, Ojibway/Saulteaux, Nakota Sioux, Métis, and many others whose histories, languages, and cultures continue to influence our vibrant community.</font>*
::::::
::::::{grid-item}
:columns: 4

:::{figure} ./logo.png
:width: 85%
:align: left
:::

```{button-link} http://www.rc-decision-support-tool.ca/voila/render/objective.ipynb?
:color: primary
:shadow:
:align: center
Launch the tool
```

```{button-link} https://ab-rcsc.github.io/rc-decision-support-tool_concept-library
:color: primary
:shadow:
:align: center
Concept library
```
::::::
:::::::

::::::::{card}
:class-card: grid-background-white
:padding: 3

::::::{dropdown} Background & Objectives
```{include} include/00_home_01_background.md
```
::::::

## 📷 How does it work!?
This tool aims to support your decision-making process when designing a remote camera program by guiding you through a series of decision points related to your study in the form of an interactive flow chart. At each step, users will be able to access information related to the question itself, the impacts of the various choices on study design, or important related topics via “pop-up” boxes; information tabs include multiple tabs for information in different levels of complexity (new vs. advanced user) and formats (e.g., descriptions, figures, videos, Shiny apps, etc.).

Once you have answered all of the questions, study design **recommendations will be generated from your selections as a standardized report**, which will include:
a) appropriate modelling approach(es) (e.g., density – spatially explicit capture-recapture),
b) study design recommendations (e.g., camera spacing, number of cameras, etc.), and 
c) analysis considerations (e.g., variables to consider in your analysis to reduce bias).

```{include} include/00_home_02_howworks_recs.md
```

At each step, you will be able to access information related to the question in the “info-popups” that include tabs with information explained with different levels of complexity (overview vs. advanced) and accessible formats (e.g., figures, videos, Shiny apps, etc.), as well analytical tools and resources. Click on the next dropdown to learn more.

```{include} include/00_home_02_howworks_info_formats.md
```

```{include} include/00_home_02_howworks_questions.md
```

:::{attention}
The information provided herein reflects perspectives and findings from Western scientific frameworks and may not encompass alternative or indigenous knowledge systems.
:::

***

(#dev)=
## Development

```{include} include/00_home_04_dev.md
```

***

(#contact-us)=
## Contact us

Have questions, feedback, or a feature request? Have resources to contribute? Please contact us either via the form below or by emailing the RCSC Coordinator (<abwildlifecameras@gmail.com>). We'll get in touch as soon as we can.

::::::{dropdown}
:::::{card}
 <iframe id="JotFormIFrame-242607211652247" title="RC Tool User Submissions" onload="window.parent.scrollTo(0,0)" allowtransparency="true" allow="geolocation; microphone; camera; fullscreen" src="https://form.jotform.com/242607211652247" frameborder="0" style="min-width:100%;max-width:100%;height:300px;border:none;" scrolling="no" > </iframe> <script src='https://cdn.jotfor.ms/s/umd/latest/for-form-embed-handler.js'></script> <script>window.jotformEmbedHandler("iframe[id='JotFormIFrame-242607211652247']", "https://form.jotform.com/")</script> 
:::::
::::::

***

```{include} include/00_home_09_acknowledgements.md
```
::::::::