
``````{admonition} Click the button for more info
:class: dropdown

### Capture-recapture (CR) / Capture-mark-recapture (CMR)
**Capture-recapture (CR) model / Capture-mark-recapture (CMR) model (Karanth, 1995; Karanth & Nichols, 1998)**: A method of estimating the abundance or density of marked populations using the number of animals detected and the likelihood animals will be detected (detection probability). CR (Karanth, 1995; Karanth & Nichols, 1998) can be used to estimate vital rates where all newly detected unmarked animals become marked and are distinguishable in future (Efford, 2022). Spatially explicit capture-recapture (SECR; Borchers & Efford, 2008; Efford, 2004; Royle & Young, 2008) models have largely replaced CR and CMR models and provide more accurate density estimates (Blanc et al., 2013, Obbard et al., 2010, Sollmann et al., 2011).

:::::{dropdown} **Assumptions, Pros, Cons**
::::{grid} 3
:::{grid-item-card}  **Assumptions**
-   Demographic closure (i.e., no births or deaths)<sup>1</sup>

-   Geographic closure (i.e., no immigration or emigration)<sup>1</sup>

-   All individuals have at least some probability of being detected<sup>2</sup>

-   Sampled area encompasses the full extent of individuals’ movements<sup>2,10</sup>

-   Activity centres are randomly dispersed<sup>12</sup>

-   Activity centres are stationary<sup>12</sup>

:::
:::{grid-item-card}  **Pros** 
-   May be used as a [relative abundance index](#mods_relative_abundance) that controls for [imperfect detection](#imperfect_detection)<sup>1</sup>

-   Easy-to-use software exists to implement (e.g., CAPTURE); MARK Implements more complicated models with covariates (and must be used for [mark-resight modelling](#mods_marked__resight))<sup>1</sup>

-    Can use the robust design with “open” models to obtain recruitment and survival rate estimates<sup>1</sup>

:::
:::{grid-item-card}  **Cons**
-   Requires that individuals are distinguishable.<sup>1</sup> However, CR<sup>10,11</sup> has also been used to estimate abundance of species that lack natural markers but that have phenotypic and/or environment-induced characteristics<sup>2,13,14</sup>

-   When the sample size is large enough to reliably estimate [density](#density)  with CR,<sup>10,11</sup> individuals are unlikely to have a unique marker<sup>2,13,14</sup>

-   Dependent on the surveyed area, which is difficult to track and calculate<sup>1</sup>

-   Requires a minimum number of captures and recaptures<sup>1</sup>

-   Relatively stringent requirements for study design (e.g., no “holes” in the trapping grid)<sup>1</sup>

-   Geographic closure at the plot level, which is often unrealistic<sup>1</sup>

-   Assumes a specific relationship between abundance and detection<sup>1</sup>

-   [Density](#density) cannot be explicitly estimated because the true area animals occupy is never measured (only approximated)<sup>16</sup>
:::
::::
:::::

`````{tab-set}
:selected: true
````{tab-item}   Overview

```{image} ./CR_EMBED_LAYMAN_EXAMPLE1.png
:width: 80%
:align: center
```
```{image} ./CR_EMBED_LAYMAN_EXAMPLE2.png
:width: 90%
:align: center
```
````
````{tab-item} Advanced
\
To estimate density using camera trap CR, we must first estimate population size 𝑁. CR models use individuals’ detection histories – that is, the record of when each individual was photographed or not photographed (i.e., (re)captured or not (re)captured) – to solve for 𝑁 (Figure 3; Royle 2020). Population-level detection histories look like a matrix of 1s and 0s, where 1s signify that an individual was captured during a given sampling occasion 𝑘, and 0s signify that the individual was not captured during that occasion (Royle 2020, Royle et al. 2014). The number of individuals photographed at least once over the course of the study (i.e., the count of animals captured) is 𝑛.  
Importantly, the count of animals is not the same as the size of the population (i.e., 𝑛 ≠ 𝑁). Some individuals will never be photographed during a study, even though they are present and able to be detected (i.e., they are in 𝑁 but not in 𝑛; Royle 2020). Using the matrix of detection histories, we must therefore calculate the likelihood animals will be detected by an array of camera traps – that is, detection probability p (Royle 2020). 
Taking this information together, we can calculate population size 𝑁 as:

```{image} ./Clarke-et-al_2023_eqn_cr1.png
:width: 80px
:align: center
```

which is often referred to as the canonical estimator of population size (Royle 2020). Population size 𝑁 can then be divided by an estimate of the area of the sampling frame 𝐴 to obtain density. 
CR models have important limitations – notably that they do not consider the spatial configuration of camera traps or the spatial pattern of animal detections. This gives rise to two major issues: 
The sampling frame 𝐴 is not known (Chandler and Royle 2013). In other words: the true area animals occupy is never measured, only approximated using adhoc approaches (e.g., using a buffer strip around the trap array; Rich et al. 2014, Sollmann 2018). Consequently, density cannot be calculated explicitly (Chandler and Royle 2013), and CR-derived density estimates are somewhat arbitrary and difficult to compare across studies (Green et al. 2020, Royle et al. 2014, Sollmann 2018). 
Detection probability is assumed to be the same across all individuals and sampling occasions, even though the likelihood a given individual is detected at a given camera trap will change with its proximity to that trap. An animal that occupies territory far away from a trap is less likely to be detected there than one that lives nearby, for example (Morin et al. 2022). 
The standard CR model has largely been phased out with the advent of spatially-explicit CR models (see 2.1.2 Spatial Capture-Recapture; Burton et al. 2015, Sollmann 2008), which address the shortcomings of CR and have been shown to produce more accurate density estimates (e.g., Blanc et al. 2013, Obbard et al. 2010, Sollmann et al. 2011).

````

````{tab-item} Visual Resources
::::{grid} 3

:::{grid-item-card}
:header: J. Andrew Royle,"Spatial Capture-Recapture Modelling" ✨
:padding: 0
:margin: 0
:::{iframe} https://www.youtube.com/embed/4HKFimATq9E
:width: 100%
:::

:::{grid-item-card}
:header: PAWS: Spatial Capture Recapture Data Analysis Part 1 ✨
:::{iframe} https://www.youtube.com/embed/aTbk-jWyMcU
:width: 100%
:::

:::{grid-item-card}
:header: PAWS: Spatial Capture Recapture Data Analysis Part 2 ✨
:padding: 0
:margin: 0
:::{iframe} https://www.youtube.com/embed/IHVez1a_hqg
:width: 100%
:::
::::
````
````{tab-item} Analytical tools & resources
| Name | URL | Note | Reference |
| -- | -- | -- | -- |
| R package - “RMark” | <https://cran.r-project.org/web/packages/RMark/index.html> | "The R counterpart to MARK, allowing complex models to be fit using just a few lines of code. With some work, it is possible to get RMark functioning on Mac and Linux (see RMark documentation)." (Wearn & Glover-Kapfer, 2017) | Laake J (2013). “RMark: An R Interface for Analysis of Capture-Recapture Data with MARK.” AFSC Processed Rep. 2013-01, Alaska Fish. Sci. Cent., NOAA, Natl. Mar. Fish. Serv., Seattle, WA. https://apps-afsc.fisheries.noaa.gov/Publications/ProcRpt/PR2013-01.pdf. |
| R package - “multimark” | <https://cran.r-project.org/web/packages/multimark/index.html> | Conventional capture-recapture using multiple marks - Conventional capture-recapture (and mark-resight) "Allows for an integrated analysis of data on two individuallyidentifiable animal marks (e.g. left and right flanks of animals), as might be obtained from capture-recapture surveys which do not use paired cameras. Also implements standard models using a single mark." (Wearn & Glover-Kapfer, 2017) | McClintock BT (2015). “multimark: an R package for analysis of capture–recapture data consisting of multiple “noninvasive” marks.” Ecology and Evolution, 5(21), 4920–4931. https://doi.org/10.1002/ece3.1676. |
| Program - “MARK” | <www.phidot.org/software/mark/downloads> | Conventional capture-recapture (and mark-resight) "Relatively complex and comprehensive software with a steep learning curve. Also implements occupancy models. Fits models using maximum likelihood methods (unlike CAPTURE), allowing for model selection and hypothesis testing. Good support available from an active community." (Wearn & Glover-Kapfer, 2017) | White, G. C., & Burnham, K. P. (1999). Program MARK: Survival estimation from populations of marked animals. Bird Study, 46(sup1), S120–S139. https://doi.org/10.1080/00063659909477239 |
| Program - “CAPTURE” | <www.mbr-pwrc.usgs.gov/software/capture.shtml> | "Software for making abundance and density estimates using a limited range of conventional capture-recapture models. Inference is based on the models in White et al. (1978), rather than modern maximum likelihood estimation." (Wearn & Glover-Kapfer, 2017) |  |

````
````{tab-item} References
<font size="1">

Ahumada, J. A., Fegraus, E., Birch, T., Flores, N., Kays, R., O'Brien, T. G., Palmer, J., Schuttler, S., Zhao, J. Y., Jetz, W., Kinnaird, M., Kulkarni, S., Lyet, A., Thau, D., Duong, M., Oliver, R., & Dancer, A. (2019). Wildlife Insights: A Platform to Maximize the Potential of Camera Trap and Other Passive Sensor Wildlife Data for the Planet. *Environmental Conservation*, 47(1), 1-6. <https://doi.org/10.1017/s0376892919000298>

Ahumada, J. A., Silva, C. E. F., Gajapersad, K., Hallam, C., Hurtado, J., Martin, E., McWilliam, A., Mugerwa, B., O'Brien, T., Rovero, F., Sheil, D., Spironello, W. R., Winarni, N., & Andelman, S. J. (2011). Community Structure and Diversity of Tropical Forest Mammals: Data from a Global Camera Trap Network. *Philosophical Transactions: Biological Sciences, 366*(1578), 2703-2711. <https://doi.org/10.1098/rstb.2011.0115>

Alberta Biodiversity Monitoring Institute [ABMI] (2021). *Terrestrial ARU and Remote Camera Trap Protocols:* Edmonton, Alberta. <https://abmi.ca/home/publications/551-600/599>

Alberta Remote Camera Steering Committee (RCSC). 2023. Remote Camera Metadata Standards: Standards for Alberta. Version 2.0. Edmonton, Alberta. <https://cassstevenson.github.io/RCSC-WildCAM_Remote-Camera-Survey-Guidelines-and-Metadata-Standards/2_metadata-standards/2.1_Citation-and-Info.html>

Alonso, R. S., McClintock, B. T., Lyren, L. M., Boydston, E. E., & Crooks, K. R. (2015). Mark-recapture and Mark-resight Methods for Estimating Abundance with Remote Cameras: A Carnivore Case Study. *PLoS One, 10*(3), e0123032. <https://doi.org/10.1371/journal.pone.0123032>

Anile, S., & Devillard, S. (2016). Study Design and Body Mass Influence RAIs from Camera Trap Studies: Evidence from the Felidae. *Animal Conservation, 19*(1), 35--45. <https://doi.org/10.1111/acv.12214>

Apps, P. J., & McNutt, J. W. (2018). How Camera Traps work and how to work them. *African Journal of Ecology, 56*(4), 702--709. <https://doi.org/10.1111/aje.12563>

Arnason, A. N., Schwarz, C. J. & Gerrard, J. M. (1991). Estimating Closed Population Size and Number of Marked Animals from Sighting Data. *Journal of Wildlife Management, 55*(4), 716--730. <https://doi.org/10.2307/3809524>

Augustine, B. C., Royle, J. A., Kelly, M. J., Satter, C. B., Alonso, R. S., Boydston, E. E., & Crooks, K. R. (2018). Spatial Capture--Recapture with Partial Identity: An Application to Camera Traps. *The Annals of Applied Statistics, 12*(1), 67-95. <https://doi.org/10.1214/17AOAS1091>

Augustine, B. C., Royle, J. A., Murphy, S. M. Chandler, R. B., Cox, J. J., & Kelly, M. J. (2019). Spatial Capture--Recapture for Categorically Marked Populations with an Application to Genetic Capture--Recapture. *Ecosphere, 10*(4) e02627-n/a. <https://doi.org/10.1002/ecs2.2627>

Bayne, E., Dennett, J., Dooley, J., Kohler, M., Ball, J., Bidwell, M., Braid, A., Chetelat, J., Dillegeard, E., Farr, D., Fisher, J., Freemark, M., Foster, K., Godwin, C., Hebert, C., Huggard, D., McIssac, D., Narwani, T., Nielsen, S., Pauli, B., Prasad, S., Roberts, D., Slater, S., Song, S., Swanson, S., Thomas, P., Toms, J., Twitchell, C., White, S., Wyatt,& F., Mundy, L. (2021). *Oil Sands Monitoring Program: A Before-After Dose- Response Terrestrial Biological Monitoring Framework for the Oil Sands*. (OSM Technical Report Series No. 7). <https://open.alberta.ca/publications/9781460151341>

Becker, M., Huggard, D. J., Dickie, M., Warbington, C., Schieck, J., Herdman, E., Serrouya, R., & Boutin, S. (2022). Applying and Testing a Novel Method to Estimate Animal Density from Motion-Triggered Cameras. *Ecosphere, 13*(4), 1-14. <https://doi.org/10.1002/ecs2.4005>

Beery, S., Morris, D., & Yang, S. (2019). Efficient Pipeline for Camera Trap Image Review. *Microsoft AI for Earth*. <https://doi.org/10.48550/arXiv.1907.06772>

Bessone, M., Kühl, H. S., Hohmann, G., Herbinger, I., N'Goran, K. P., Asanzi, P., Da Costa, P. B., Dérozier, V., Fotsing, E. D. B., Beka, B. I., Iyomi, M. D., Iyatshi, I. B., Kafando, P., Kambere, M. A., Moundzoho, D. B., Wanzalire, M. L. K., Fruth, B., & Michalski, F. (2020). Drawn out of the Shadows: Surveying Secretive Forest Species with Camera Trap Distance Sampling. *Journal of Applied Ecology, 57*(5), 963--974. <https://doi.org/10.1111/1365-2664.13602>

Bischof, R., Dupont, P., Milleret, C., ChipperfIeld, J., & Royle, J.A. (2020). Consequences of Ignoring Group Association in Spatial Capture-Recapture. *Wildlife Biology, 2020*(1). <https://doi.org/10.2981/wlb.00649>
</font>\
````

````{tab-item} Glossary
**\*Access Method**
:   The method used to reach the camera location (e.g., on "Foot," "ATV," "Helicopter," etc.).

**\*Adult**
:   Animals that are old enough to breed; reproductively mature.

**\*Age Class**
:   The age classification of one or more individuals (if the classification is the same) being categorized (e.g., "Adult," "Juvenile," "Subadult," "Subadult - Young of Year," "Subadult - Yearling", or "Unknown").

**\*Analyst**
:   The first and last names of the individual who provided the observation data point (species identification and associated information). If there are multiple analysts for an observation, enter the primary analyst.

**\*Animal ID**
:   A unique ID for an animal that can be uniquely identified (e.g., marked in some way). More than one unique individual can be identified in an image; each individual should be entered as a unique row. If Animal IDs were not collected, leave blank.

**Audible lure**
:   Sounds imitating noises of prey or conspecifics that draw animals closer by eliciting curiosity (Schlexer, 2008).

**Bait**
:   A food item (or other substance) that is placed to attract animals via the sense of taste and olfactory cues (Schlexer, 2008).

**\*Bait/Lure Type**
:   The type of bait or lure used at a camera location. Leave blank if not applicable.

**\*Batteries Replaced**
:   Whether the camera's batteries were replaced.

**\*Behaviour**
:   The behaviour of an individual or multiple individuals being categorized (e.g., "Standing," "Drinking," "Vigilant," etc.).

**\*Camera Active On Arrival**
:   Whether a camera was functional upon arrival.

**\*Camera Active On Departure**
:   Whether a camera was functional upon departure.

**Camera angle**
:   The degree at which the camera is pointed toward the FOV Target Feature relative to the horizontal ground surface (with respect to slope, if applicable).

**\*Camera Attachment**
:   The method/tools used to attach the camera (e.g., attached to a tree with a bungee cord; reported as codes such as "Tree + Bungee/Strap").

**\*Camera Damaged**
:   Whether the camera was damaged or malfunctioning; if there is any damage to the device (physical or mechanical), the Crew should describe the damage in the Service/Retrieval Comments.

**Camera days per camera location**
:   The number of days each camera was active and functioning during the period it was deployed (e.g., 24-hour periods or the difference in days between the Deployment Start Date Time and the Deployment End Date Time if there were no interruptions).

**\*Camera Direction (degrees)**
:   The cardinal direction that a camera faces. Ideally, cameras should face north (N; i.e. "0" degrees), or south (S; i.e. "180" degrees) if north is not possible. The Camera Direction should be chosen to ensure the field of view (FOV) is of the original FOV target feature.

**\*Camera Height (m)**
:   The height from the ground (below snow) to the bottom of the lens (recorded in metres to the nearest 0.05 m).

**\*Camera ID**
:   A unique alphanumeric ID for the camera that distinguishes it from other cameras of the same make or model.

**Camera location**
:   The location where a single camera was placed (recorded as "Camera Location Name").

**\*Camera Location Characteristic(s)**
:   Record any significant features around the camera at the time of the visit. This may include for example, manmade or natural linear features (e.g., trails), habitat types (e.g., wetlands), wildlife structure (e.g., beaver dam). Camera Location Characteristics differ from FOV Target Features in that Camera Location Characteristics could include those not in the camera's Field of View.

**\*Camera Location Comments**
:   Comments describing additional details about a camera location.

**\*Camera Location Name**
:   A unique alphanumeric identifier for the location where a single camera was placed (e.g., "BH1," "BH2").

**\*Camera Make**
:   The make (i.e., the manufacturer; e.g., "Reconyx" or "Bushnell') of a particular camera.

**\*Camera Model**
:   The model number or name (e.g., "PC900" or "Trophy Cam HD") of a particular camera.

**\*Camera Serial Number**
:   The serial number of a particular camera, which is usually found inside the camera cover (e.g., "P900FF04152022").

**Camera spacing**
:   The distance between cameras (i.e., also referred to as "inter-trap distance"). This will be influenced by the chosen sampling design, the survey objectives, the target species and data analysis.

**Capture-recapture (CR) model / Capture-mark-recapture (CMR) model (Karanth, 1995; Karanth & Nichols, 1998)**
:   A method of estimating the abundance or density of marked populations using the number of animals detected and the likelihood animals will be detected (detection probability). CR (Karanth, 1995; Karanth & Nichols, 1998) can be used to estimate vital rates where all newly detected unmarked animals become marked and are distinguishable in future (Efford, 2022). Spatially explicit capture-recapture (SECR; Borchers & Efford, 2008; Efford, 2004; Royle & Young, 2008) models have largely replaced CR and CMR models and provide more accurate density estimates (Blanc et al., 2013, Obbard et al., 2010, Sollmann et al., 2011).

**\*Card Status (% Full)**
:   The remaining storage capacity on an SD card; collected during a camera service or retrieval.

**Categorical partial identity model (mods_catspim (Augustine et al., 2019; Sun et al., 2022)**
:   A method used to estimate the density of partially marked populations in which the "spatial locations of where partial identity samples are captured to probabilistically resolve their complete identities" (Augustine et al., 2018, 2019). catSPIM models use partial identity traits (e.g., sex class, antler points) to help infer individual identities (Augustine et al., 2019; Sun et al., 2022). catSPIM is an extension of the SC model (Chandler & Royle, 2013).

**Clustered design**
:   Multiple cameras are deployed at a sample station (Figure 3d). A clustered design can be used within a systematic or stratified approach (i.e., systematic clustered design or as a clustered random design [Wearn & Glover-Kapfer, 2017]).

**Convenience design**
:   Camera locations or sample stations are chosen based on logistic considerations (e.g., remoteness, access constraints, and costs).

**Crew**
:   The first and last names of the individuals who collected data for a deployment or a service/retrieval.

**Cumulative detection probability**
:   The probability of detecting a species at least once during the entire survey (Steenweg et al., 2019).

**Density**
:   The number of individuals per unit area.

**Deployment**
:   A unique placement of a camera in space and time (recorded as "Deployment Name"). There may be multiple deployments for one camera location. Deployments are often considered as the time between visits (i.e., deployment to service, service to service, and service to retrieval). Any change to camera location, sampling period, camera equipment (e.g., Trigger Sensitivity setting, becomes non-functioning), and/or conditions (e.g., not baited then baited later; camera SD card replaced) should be documented as a unique deployment.

**\*Deployment Area Photo Numbers**
:   The image numbers for the deployment area photos (if collected, e.g., "DSC100"). These are optionally documented on a Camera Deployment Field Datasheet for each set of camera deployment area photos. Leave blank if not applicable.

**Deployment area photos**
:   Photos of the area around the camera location, collected as a permanent, visual record of the FOV Target Features, Camera Location Characteristics, environmental conditions (e.g., vegetation, ecosite, weather) or other variables of interest. The recommendation includes collecting four photos taken from the centre of the target detection zone (Figure 5), facing each of the four cardinal directions. The documentation of the collection of these photos is recorded as "Deployment Area Photos Taken" (Yes/No).

**\*Deployment Area Photos Taken**
:   Whether deployment area photos were taken (yes/no; optional). The recommendation includes collecting four photos taken from the centre of the target detection zone (Figure 5), facing each of the four cardinal directions.

**\*Deployment Comments**
:   Comments describing additional details about the deployment.

**\*Deployment Crew**
:   The first and last names of the individuals who collected data during the deployment visit.

**Deployment End Date Time (DD-MMM-YYYY HH:MM:SS)**
:   The date and time that the data was retrieved for a specific deployment (e.g., 27-JUL-2019 23:00). The Deployment End Date Time may not coincide with when the last image or video was collected (i.e., the Image Set End Date Time). Recording this field allows users to account for deployments where no images were captured and to confirm the last date and time that the camera was active.

**\*Deployment Image Count**
:   The total number of images collected during the deployment, including false fires (i.e., empty images with no species) and those triggered by a time-lapse setting.

**Deployment metadata**
:   Metadata that is collected each time a camera is deployed. Each deployment event should have its own Camera Deployment Field Datasheet. The relevant metadata fields that should be collected differ when a camera is deployed vs. serviced or retrieved.

:   Refer to Appendix A - Table A5 and Camera Deployment Field Datasheet.

**\*Deployment Name**
:   A unique alphanumeric identifier for a unique camera deployed during a specific survey period (ideally recorded as: “Camera Location Name”_“Deployment Start Date” (or …_”Deployment End Date”) (e.g., “BH1_17-JUL-2018" or “BH1_17-JUL-2018_21-JAN-2019”). Alternative naming conventions may be used, but the goal should be to minimize duplicate Image Names.

**\*Deployment Start Date Time (DD-MMM-YYYY HH:MM:SS)**
:   The date and time that a camera was placed for a specific deployment (e.g., 17-JUL-2018 10:34:22). The Deployment Start Date Time may not coincide with when the first image or video was collected (i.e., the Image Set Start Date Time). Recording this field allows users to account for deployments where no images were captured and to confirm the first date and time a camera was active.

**Deployment visit**
:   When a crew has gone to a location to deploy a remote camera.

**Detection "event"**
:   A group of images or video clips that are considered independent from other images or video clips based on a certain time threshold (or “inter-detection interval”). For example, 30 minutes (O’Brien et al., 2003; Gerber et al., 2010; Kitamura et al., 2010; Samejima et al., 2012) or 1 hour (e.g., Tobler et al., 2008; Rovero & Marshall, 2009).

**Detection distance**
:   "The maximum distance that a sensor can detect a target" (Wearn and Glover-Kapfer, 2017).

**Detection probability (aka detectability)**
:   The probability (likelihood) that an individual of the population of interest is included in the count at time or location i.

**Detection rate**
:   The frequency of independent detections within a specified time period.

**Detection zone**
:   The area (conical in shape) in which a remote camera can detect the heat signature and motion of an object (Rovero & Zimmermann, 2016) (Figure 5).

**Distance sampling (DS) model (Howe et al., 2017)**
:   A method to estimate abundance by using distances at which animals are detected (from survey lines or points) to model abundance as a function of decreasing detection probability with animal distance from the camera (using a decay function) (Cappelle et al., 2021; Howe et al., 2017).

**\*Easting Camera Location**
:   The easting UTM coordinate of the camera location (e.g., "337875"). Record using the NAD83 datum. Leave blank if recording the Longitude instead.

**Effective detection distance**
:   The distance from a camera that would give the same number of detections if all animals up to that distance are perfectly detected, and no animals that are farther away are detected; Buckland, 1987, Becker et al., 2022).

**\*Event Type**
:   Whether detections were reported as an individual image captured by the camera (“Image”), a “Sequence,” or “Tag.”

**False trigger**
:   Blank images (no wildlife or human present). These images commonly occur when a camera is triggered by vegetation blowing in the wind.

**Field of View (FOV)**
:   The extent of a scene that is visible in an image (Figure 5); a large FOV is obtained by "zooming out" from a scene, whilst "zooming in" will result in a smaller FOV (Wearn & Glover-Kapfer, 2017).

**Flash output**
:   The camera setting that provides the level of intensity of the flash (if enabled).

**\*FOV Target Feature**
:   A specific man-made or natural feature at which the camera is aimed to maximize the detection of wildlife species or to measure the use of that feature. Leave blank if not applicable.

**\*FOV Target Feature Distance (m)**
:   The distance (in metres) from the camera to the FOV Target Feature (recorded to the nearest 0.5 m). Leave blank if not applicable.

**\*GPS Unit Accuracy (m)**
:   The margin of error of the GPS unit used to record spatial information (e.g., "5" [m]), such as the coordinates of the camera location. On most GPS units (e.g., "Garmin") this information is provided on the unit’s satellite information page. 

**\*Human Transport Mode/Activity**
:   The activity performed, or mode of transportation used, by a human observed (e.g., hiker, skier, all terrain vehicle etc.). Leave blank if not applicable.

**Hurdle model (Mullahy, 1986)**
:   A regression model used in the setting of excess zeros (zero-inflation) and overdispersion (Mullahy, 1986). Hurdle models (aka "zero-altered" models) differ from zero-inflation models in that they are two-part models, and the zero and non-zero counts are modelling separately (thus, they are only adequate when the counting process cannot generate a zero value) (Blasco-Moreno et al., 2019). [relative abundance indices]

**Image**
:   An individual image captured by a camera, which may be part of a multi-image sequence (recorded as "Image Name").

**Image classification**
:   The process of assigning class labels to an image according to the wildlife species, other entities (e.g., human, vehicle), or conditions within the image. Image classification can be performed manually or automatically by an artificial intelligence (AI) algorithm. Image classification is sometimes used interchangeably with "image tagging."

**Image classification confidence**
:   The likelihood of an image containing an object of a certain class (Fennell et al., 2022).

**\*Image Flash Output**
:   The Image Flash Output setting determines the level of intensity of the flash (if enabled). Record the Image Flash Output as reported in the image Exif data (e.g., "Flash Did Not Fire", "Auto"). Leave blank not applicable and "Unknown" if not known.

**\*Image Infrared Illuminator**
:   The infrared illuminator setting can be enabled, if applicable to the camera make/model, to obtain greater visibility at night by producing infrared light. Record the Image Infrared Illuminator as reported in the image Exif data (e.g., "On" or "Off"). Record “Unknown” if not known.

**Image Name**
:   A unique alphanumeric file name for the image. It is important to include (at a minimum) the camera location, date, time, and image number when generating an Image Name to avoid duplicate file names (e.g., "BH1_17-JUL-2018_22-JUL-2018 10:34:22_IMG_100").

**Image processing**
:   The series of operations that are taken to extract information from images. In the case of remote camera data, it can include loading the images into a processing platform, extracting information from the image metadata (e.g., the date and time the image was taken), running an artificial intelligence (AI) algorithm to identify empty images, classifying animals or other entities within the image.

**\*Image Sequence**
:   The order of the image in a rapid-fire sequence as reported in the image Exif data (text; e.g., "1 of 1" or "1 of 3"). Leave blank if not applicable.

**\*Image Set End Date Time (DD-MMM-YYYY HH:MM:SS)**
:   The date and time of the last image or video collected during a specific deployment (e.g., "17-JUL-2018 12:00:02"). The Image Set End Date Time may not coincide with the deployment end date time. Recording this field allows users to account for deployments that were conducted but for which no data was found and to confirm the last date and time a camera was active (if functioning) if no images or videos were captured prior to Service/Retrieval (especially valuable if users did not collect Time-lapse images or if the camera malfunctioned).

**\*Image Set Start Date Time (DD-MMM-YYYY HH:MM:SS)**
:   The date and time of the first image or video collected during a specific deployment (e.g., “17-JUL-2018 12:00:02”). The Image Set Start Date Time may not coincide with the Deployment Start Date Time. Recording this field allows users to confirm the first date and time a camera was active (reliable if Time-lapse images were collected; especially valuable if the user scheduled a start delay).

**Image tagging**
:   The process of classifying an image according to the wildlife species, other entities (e.g., human, vehicle), or conditions within the image. Image tagging may follow image classification to further classify characteristics of the individuals (e.g., age class, sex class, or behaviour) or entities within the image.

**\*Image Trigger Mode**
:   The type of trigger mode used to capture the image as reported in the image Exif data (e.g., "Time Lapse", "Motion Detection," "CodeLoc Not Entered," "External Sensor"). Record "Unknown" if not known.

**\*Image/Sequence Comments**
:   Comments describing additional details about the image/sequence.

**\*Image/Sequence Date Time (DD-MMM-YYYY HH:MM:SS)**
:   The date and time of an image or sequence. Depending on the Event Type, Image/Sequence Date Time may be reported for an individual image or the first image of a unique sequence. Record as “DD-MMM-YYYY HH:MM:SS” (e.g., 22-JUL-2018 11:02:02).

**Imperfect detection**
:   Species are often detected "imperfectly," meaning that they are not always detected when they are present (e.g., due to cover of vegetation, cryptic nature or small size) (MacKenzie et al., 2004).

**Independent detections**
:   Detections that are deemed to be independent based on a user-defined threshold (e.g., 30 minutes).

**\*Individual Count**
:   The number of unique individuals being categorized. This may be recorded as the total number of individuals, or according to Age Class and/or Sex Class.

**Infrared illuminator**
:   The camera setting that can be enabled (if applicable to the camera make and camera model) to obtain greater visibility at night by producing infrared light.

**Instantaneous sampling (IS) (Moeller et al., 2018)**
:   A method used to estimate abundance or density from time-lapse images from randomly deployed cameras; the number of unique individuals (the count) is needed (Moeller et al., 2018).

**Intensity of use (Keim et al., 2019)**
:   "The expected number of use events of a specific resource unit during a unit of time… [which characterizes] how frequently a particular resource unit is used" (Keim et al., 2019). The intensity of use differs from the probability of use (which characterizes "the probability of at least one use event of that resource unit during a unit of time"; Keim et al., 2019).

**Inter-detection interval**
:   A user-defined threshold used to define a single "detection event" (i.e., independent "events") for group of images or video clips (e.g., 30 minutes or 1 hour). The threshold should be recorded in the Survey Design Description.

**Inventory**
:   Rapid assessment surveys to determine what species are present in a given area at a given point in time; there is no attempt made to quantify aspects of communities or populations (Wearn & Glover-Kapfer, 2017).

**\*Juvenile**
:   Animals in their first summer, with clearly juvenile features (e.g., spots); mammals older than neonates but that still require parental care.

**Kernel density estimator**
:   The probability of "utilization" (Jennrich & Turner, 1969); describes the relative probability of use (Powell & Mitchell, 2012).

**\*Key ID**:   The unique ID for the specific key or set of keys used to lock/secure the camera to the post, tree, etc.

**\*Latitude Camera Location**
:   The latitude of the camera location in decimal degrees to five decimal places (e.g., "53.78136"). Leave blank if recording Northing instead.

**\*Longitude Camera Location**
:   The longitude of the camera location in decimal degrees to five decimal places (e.g., "-113.46067"). Leave blank if recording Easting instead.

**Lure**
:   Any substance that draws animals closer; lures include scent (olfactory) lure, visual lure and audible lure (Schlexer, 2008).

**Marked individuals / populations / species**
:   Individuals, populations, or species (varies with modelling approach and context) that can be identified using natural or artificial markings (e.g., coat patterns, scars, tags, collars).

**Mark-resight (MR) model (Arnason et al., 1991; McClintock et al., 2009)**
:   A method used to estimate the abundance of partially marked populations using the number of marked individuals, the number of unmarked individuals, and the detection probability from marked animals (Wearn & Glover-Kapfer, 2017). MR is similar to capture-recapture (CR; Karanth, 1995; Karanth & Nichols, 1998) models, except only a portion of animals are individually identified.

**Metadata**
:   Data that provides information about other data (e.g., the number of images on an SD card).

**Model assumption**
:   Explicitly stated (or implicitly premised) conventions, choices and other specifications (e.g., about the data, wildlife ecology/behaviour, the relationships between variables, etc.) on which a particular modelling approach is based that allows the model to provide valid inference.

**Modelling approach**
:   The method used to analyze the camera data, which should depend on the state variable, e.g., occupancy models [MacKenzie et al., 2002], spatially explicit capture recapture (SECR) for density estimation [Chandler and Royle, 2013], etc. and the target species.

**\*Motion Image Interval (seconds)**
:   The time (in seconds) between images within a multi-image sequence that occur due to motion, heat, or activation of external detector devices. The Motion Image Interval is pre-set in the camera’s settings by the user, but the time at which the camera collects images because of this setting is influenced by the presence of movement or heat. For example, if the camera was set to take 3 images per event at a Motion Image Interval of 3 seconds when the camera detects motion or heat, the first image will be collected (e.g., at 09:00:00), the second image will be collected 3 seconds later (09:00:03), and the third will be collected 3 seconds after that (09:00:06). This setting differs from the Quiet Period in that the delay occurs between images contained within a multi-image sequence, rather than between multi-image sequences (as in quiet period). If a Motion Image Interval was not set, enter "0" seconds (i.e., instantaneous).

**Negative binomial (NB) regression (Mullahy, 1986)**
:   A regression model used for count data with overdispersion but without zero-inflation. [relative abundance indices]

**N-mixture models**
:   A class of models for estimating absolute abundance using replicated counts of animals from several different sites; site-specific counts are treated as independent random variables to estimate the number of animals available for capture at each site; detection is imperfect (Royle 2004). N-mixture models are a type of site-structured model (i.e., that "treat each camera as though it samples... [a] distinct population within a larger meta-population" [Clarke et al., 2023]).

**\*Northing Camera Location**
:   The northing UTM coordinate of the camera location (e.g., "5962006"). Record using the NAD83 datum. Leave blank if recording the Latitude instead.

**\*# Of Images**
:   The number of images on an SD card.

**Occupancy**
:   The probability a site is occupied by the species.

**Occupancy model (MacKenzie et al., 2002)**
:   A modelling approach used to account for imperfect detection by first evaluating the detection probability of a species via detection histories (i.e., present or absent) to determine the probability of the true presence or absence of a species at a site (MacKenzie et al., 2002).

**Overdispersion**
:   A variance significantly larger than the mean (Bliss & Fisher, 1953); greater variability in a set of data than predicted by the error structure of the model (Harrison et al., 2018); excess variability can be caused by zero inflation, non-independence of counts, or both (Zuur et al., 2009).

**Paired design**
:   A form of clustered design when two cameras that are placed closely together to increase detection probability ("paired cameras") or to evaluate certain conditions ("paired sites", e.g., on- or off trails). Paired placements can help to account for other variability that might occur (i.e., variation in habitat quality).

**Partially marked individuals / populations / species**
:   Individuals, populations, or species (varies with modelling approach and context) that have a suite of partially identifying traits (e.g., antler points, sex class, age class). For populations/species, those in which a proportion of individuals carry marks or in which individuals themselves are partially marked.

**\*Photos Per Trigger**
:   The camera setting that describes the number of photos taken each time the camera is triggered.

**Poisson regression**
:   A regression model for count data used when data are not overdispersed or zero-inflated (Lambert, 1992). [relative abundance indices]

**Project**
:   A scientific study, inventory or monitoring program that has a certain objective, defined methods, and a defined boundary in space and time (recorded as "Project Name").

**\*Project Coordinator**
:   The first and last name of the primary contact for the project.

**\*Project Coordinator Email**
:   The email address of the Project Coordinator.

**\*Project Description**
:   A description of the project objective(s) and general methods.

**\*Project Name**
:   A unique alphanumeric identifier for each project (e.g., "UofA_WildEdmonton-Urban-Wildlife-Monitoring_2018").

**Pseudoreplication**
:   When observations are not statistically independent (spatially or temporally) but are treated as if they are independent.

**Purpose of Visit**
:   The reason for visiting the camera location (i.e. to deploy the camera ["Deployment"], retrieve the camera ["Retrieve"] or to change batteries/SD card or replace the camera ["Service"]).

**\*Quiet Period (seconds)**
:   The user-defined camera setting which provides the time (in seconds) between shutter "triggers" if the camera was programmed to pause between firing initially and firing a second time. If a Quiet Period was not set, enter "0."
Also known as "time lag" (depending on the Camera Make and Camera Model; Palmer et al., 2018). The Quiet Period differs from the Motion Image Interval in that the delay occurs between multi-image sequences rather than between the images contained within multi-image sequences (as in the Motion Image Interval).

**Random (or "simple random") design**
:   Randomized Camera Locations (or sample stations) across the area of interest, sometimes with a predetermined minimum distance between Camera Locations (or sample stations).

**Random encounter and staying time (REST) model (Nakashima et al., 2018)**
:   A recent modification of the REM (Nakashima et al., 2018) that substitutes staying time (i.e., the cumulative time in the cameras' detection zone) for movement speed (staying time and movement speed are inversely proportional) (Cappelle et al., 2021).

**Random encounter model (REM) (Rowcliffe et al., 2008, 2013)**
:   A method used to estimate the density of unmarked populations; uses the rate of independent captures, an estimate of movement rate, average group size, and the area sampled by the remote camera.

**Recovery time**
:   The time necessary for the camera to prepare to capture the next photo after the previous one has been recorded (Trolliet et al., 2014).

**Registration area**
:   The area in which an animal entering has at least some probability of being captured on the image

**Relative abundance indices**
:   An index of relative abundance. When observational data is converted to a detection rate (i.e., the frequency [count] of independent detections of a species within a distinct time period). An index can be a count of animals or any sign that is expected to vary with population size (Caughley, 1977; O'Brien, 2011).

**\*Remaining Battery (%)**
:   The remaining battery power (%) of batteries within a camera.

**Royle-Nichols model (Royle & Nichols, 2003; MacKenzie et al., 2006)**
:   A method used to estimate population abundance or density, which assumes that individuals are counted only once per sampling occasion (Royle, 2004), but that does not require all individuals to be marked. Royle-Nichols models are a type of site-structured model (i.e., that "treat each camera as though it samples... [a] distinct population within a larger meta-population" [Clarke et al., 2023]).

**Sample station**
:   A grouping of two or more non-independent camera locations, such as when cameras are clustered or paired (recorded as "Sample Station Name").

**\*Sample Station Name**
:   A sequential alphanumeric identifier for each camera location within a grouping of two more non-independent camera locations when cameras are deployed in clusters, pairs or arrays (e.g., “SS1” in “SS1_BH1”, “SS1_BH2”, “SS1_BH3” etc.). Leave blank if not applicable.

**Scent lure**
:   Any material that draws animals closer via their sense of smell (Schlexer, 2008).

**\*SD Card ID**
:   The ID label on an SD card (e.g., "CMU-100").

**\*SD Card Replaced**
:   Whether the SD card was replaced.

**\*Security**
:   The equipment used to secure the camera (e.g., "Security box," "Bracket," "Bracket + Screws," or "None").

**Sequence**
:   A user-defined group of images or video clips considered as a single “detection event“ (recorded as "Sequence Name"); often users choose a certain time threshold (or “inter-detection interval“) to define independent “events“; e.g., 30 minutes or 1 hour. The threshold should be recorded in the Survey Design Description).

**\*Sequence Name**
:   A unique alphanumeric for a multi-image sequence. The Sequence Name should ideally consist of the Deployment Name and the names of the first and last images and videos in the sequence (separated by "_") (i.e., "Deployment Name"_"IMG_#[name of first image in sequence]"_"IMG_#[name of last image in sequence] (e.g., "BH1_22-JUL-2018 IMG_001-IMG_005").

**Service/Retrieval**
:   When a crew has gone to a location to service or retrieve a remote camera.

**\*Service/Retrieval Comments**
:   Comments describing additional details about the service/retrieval.

**\*Service/Retrieval Crew**
:   The first and last names of the individuals who collected data during the service/retrieval visit.

**Service/Retrieval metadata**
:   Metadata that should be collected each time a camera location is visited to service or retrieve a camera, including data on any change to the camera location, sampling period, and/or setting type (e.g., not baited and then baited later). The relevant metadata fields that should be collected differ when a camera is deployed vs. serviced or retrieved.
Refer to Appendix - Table A5 and the Camera Service/Retrieval Field Datasheet.

**Service/Retrieval visit**
:   When a crew has gone to a location to service or retrieve a remote camera.

**\*Sex Class**
:   The sex classification of an individual or multiple individuals (if the classification is the same) being categorized (e.g., "Male," "Female," or "Unknown").

**Space-to-event (STE) model (Moeller et al., 2018)**
:   A method used to estimate abundance or density that accounts for variable detection probability through the use of time-lapse images and is unaffected by animal movement rates (collapses sampling intervals to an instant in time, and thus estimates are unaffected by animal movement rates) (Moeller et al., 2018).

**Spatial autocorrelation**
:   The tendency for locations that are closer together to be more similar.

**Spatial count (SC) model / Unmarked spatial capture-recapture (Chandler & Royle, 2013)**
:   A method used to estimate the density of unmarked populations; similar to SECR (Borchers & Efford, 2008; Efford, 2004; Royle & Young, 2008; Royle et al., 2009); however, SC models account for individuals' unknown identities using the spatial pattern of detections (Chandler & Royle, 2013; Sun et al., 2022). SC uses trap-specific counts to estimate the location and number of activity centres to estimate density.

**Spatial mark-resight (SMR) (Chandler & Royle, 2013; Sollmann et al., 2013a, 2013b)**
:   A method used to estimate the density of "partially marked populations by combining... [detection] histories of marked [individuals] and counts of unmarked [individuals]" (Doran-Myers, 2018) over several occasions (Sollman et al., 2013a; Rich et al., 2014; Whittington et al., 2018). SMR models can be implemented using different statistical frameworks, including Bayesian estimation (Royle and Young, 2008; Morin et al., 2022).

**Spatial partial identity model (2-flank SPIM) (Augustine et al., 2018)**
:   A method used to estimate the density of partially marked populations in which the “spatial locations of where partial identity samples are captured to probabilistically resolve their complete identities” (Augustine et al., 2018). Paired sampling design is commonly used to capture both the right and left flanks of an animal to resolve individual identities (Augustine et al., 2018). 2-flank SPIM is an extension of the SCR model (Borchers & Efford, 2008; Efford, 2004; Royle & Young, 2008; Royle et al., 2009).

**Spatially explicit capture-recapture (SECR) / Spatial capture-recapture (SCR) (Borchers & Efford, 2008; Efford, 2004; Royle & Young, 2008; Royle et al., 2009)**
:   The SECR (or SCR) method is used to estimate the density of marked populations; an extension of traditional capture-recapture (CR; Karanth, 1995; Karanth & Nichols, 1998) models (Karanth, 1995; Karanth & Nichols, 1998) that explicitly accounts for camera location and animal movement (Burgar et al., 2018). SECR models use spatially referenced individual capture histories to infer where animals' home range centres are, assuming that detection probability decreases with increasing distance between cameras and home range centres (Clarke et al., 2023). SECR models can be implemented using different statistical frameworks, including Bayesian estimation (Royle and Young, 2008; Morin et al., 2022).

**Species**
:   The capitalized common name of the species being categorized (“tagged”).

**\*Stake Distance (m)**
:   The distance from the camera to a stake (in metres to the nearest 0.05 m). Leave blank if not applicable.

**State variable**
:   A formal measure that summarizes the state of a community or population at a particular time (Wearn & Glover-Kapfer, 2017), e.g., species richness or population abundance.

**Stratified design**
:   The area of interest is divided into smaller strata (e.g., habitat type, disturbance levels), and cameras are placed within each stratum (e.g., 15%, 35% and 50% of sites within high, medium, and low disturbance strata).

**Stratified random design**
:   The area of interest is divided into smaller strata (e.g., habitat type, disturbance levels), and then a proportional random sample of sites is selected within each stratum (e.g., 15%, 35% and 50% of sites within high, medium and low disturbance strata).

**Study area**
:   A unique research, inventory or monitoring area (spatial boundary) within a project (there may be multiple study areas within a single project) (recorded as "Study Area Name").

**Study Area Description**
:   A description for each unique research or monitoring area including its location, the habitat type(s), land use(s) and habitat disturbances (where applicable).

**\*Study Area Name**
:   A unique alphanumeric identifier for each study area (e.g.,"OILSANDS_REF1," "OILSANDS_REF2"). If only one area was surveyed, the Project Name and Study Area Name should be the same.

**\*Subadult**
:   Animals older than a "Juvenile" but not yet an "[Adult](#adult)"; a "Subadult" may be further classified into "Young of the Year" or "Yearling."

**\*Subadult - Yearling**
:   Animals approximately one year old; has lived through one winter season; between "Young of Year" and "[Adult](#adult)."

**\*Subadult - Young of Year**
:   Animals less than one year old; born in the previous year's spring, but has not yet lived through a winter season; between "Juvenile" and "Yearling."

**Survey**
:   A unique deployment period (temporal extent) within a project (recorded as "Survey Name").

**\*Survey Design**
:   The spatial arrangement of remote cameras within the study area.

**\*Survey Design Description**
:   A description of any additional details about the Survey Design.

**\*Survey Name**
:   A unique alphanumeric identifier for each survey period (e.g., "FORTMC_001").

**\*Survey Objectives**
:   The specific objectives of each survey within a project. Survey objectives should be specific, measurable, achievable, relevant, and time-bound (i.e., SMART). Objectives may include include the Target Species, the state variables, proposed modelling approach(es) and the variables of interest (e.g., occupancy, density). If a project has only one survey or multiple surveys with identical methods and locations, the project and Survey Objectives may be the same. Otherwise, the differences between each unique survey should be documented carefully.

**Systematic design**
:   Camera locations occur in a regular pattern (e.g., a grid pattern) across the study area.

**Systematic random design**
:   Camera locations are selected using a two-stage approach. Firstly, girds are selected systematically (to occur within a regular pattern) across the study area. The location of the camera within each grid is then selected randomly.

**\*Tag**
:   When individuals or groups of individuals are categorized within images, regardless of whether the information applies to all of the individuals in the image.

**\*Target Species**
:   The capitalized common name(s) of the species that the survey was designed to detect.

**Targeted design**
:   Camera locations or sample stations are placed in areas that are known or suspected to have higher activity levels (e.g., game trails, mineral licks).

**Test image**
:   An image taken from a camera after it has been set up to provide a permanent record of the visit metadata (e.g., Sample Station Name, Camera Location Name, Deployment Name, Crew, and Deployment Start Date Time [DD-MMM-YYYY HH:MM:SS]).


:   Taking a test image can be useful to compare the information from the image to that of which was collected on the Camera Service/Retrieval Field Datasheet after retrieval and can help in reducing recording errors.

**\*Test Image Taken**
:   Whether a test image (i.e., an image taken from a camera after it has been set up to provide a permanent record of the visit metadata) was taken. Arm the camera, from ~5 m in front, walk towards the camera while holding the Test Image Sheet (see next page).

**Time in front of the camera (TIFC) (Huggard, 2018; Warbington & Boyce, 2020; tested in Becker et al., 2022)**
:   A method used to estimate density that treats camera image data as quadrat samples (Becker et al., 2022).

**Time-lapse image**
:   Images that are taken at regular intervals (e.g., hourly or daily, on the hour). It is critical to take a minimum of one time-lapse image per day at a consistent time (e.g., 12:00 pm [noon]) to create a record of camera functionality and local environmental conditions (e.g., snow cover, plant growth, etc.). Time-lapse images may always be useful for modelling approaches that require estimation of the "viewshed" ("viewshed density estimators" such as REM or time-to-event (TTE) models; see Moeller et al., [2018] for advantages and disadvantages).

**Time-to-event (TTE) model (Moeller et al., 2018)**
:   A method used to estimate abundance or density from the detection rate while accounting for animal movement rates (Moeller et al., 2018). The TTE model assumes perfect detection (though there is a model extension to account for imperfect detection that requires further testing).

**Total number of camera days**
:   The number of days that all cameras were active during the survey.

**Trigger "event"**
:   An activation of the camera detector(s) that initiates the capture of a single or multiple images, or the recording of video.

**\*Trigger Mode(s)**
:   The camera setting(s) that determine how the camera will trigger: by motion ("Motion Image"), at set intervals ("Time-lapse image"), and/or by video ("Video"; possible with newer camera models, such as Reconyx HP2X).

**\*Trigger Sensitivity**
:   The camera setting responsible for how sensitive a camera is to activation (to "triggering") via the infrared and/or heat detectors (if applicable, e.g., Reconyx HyperFire cameras have a choice between "Low," "Low/Med," "Med," "Med/High," "High," "Very high" and "Unknown"). 

**Trigger speed**
:   The time delay necessary for the camera to shoot a photo once an animal has interrupted the infrared beam within the camera's detection zone (Trolliet et al., 2014). Trigger speed differs from Motion Image Interval (a camera setting specified by the user) in that the trigger speed is inherent to the Camera Make and Camera Model (e.g., two different cameras, models both with a Motion Image Interval set to "no delay," may not be able to capture images at the same speed).

**Unmarked individuals / populations / species**
:   Individuals, populations, or species (varies with modelling approach and context) that cannot be identified using natural or artificial markings (e.g., coat patterns, scars, tags, collars). Unmarked population models rely on supplementary data (e.g., animal movement speed) and/or assumptions as a surrogate for individual identification; that is, to distinguish between multiple detections of the same individual from detections of multiple individuals when individuals do not have unique features (Gilbert et al., 2020; Morin et al., 2022).

**User label**
:   A label (up to 16 characters) that can be programmed in the camera’s settings, and that will be visible in the data band of all photos and videos taken by the camera (Reconyx, 2018). It is recommended that users program the Sample Station Name/Camera Location Name as the user label, which serves as a means to confirm which Sample Station Name/Camera Location Name is associated with the images/videos.

**\*UTM Zone Camera Location**
:   The coordinate system that divides geographic areas into north-south zones. In Alberta the UTM zones are either 11, 12, or TTM. Enter all other UTM zones in the Camera Location Comments field (e.g., zones 7-10 for British Columbia), or use Latitude and Longitude instead of UTM coordinates.

**\*Video Length (seconds)**
:   If applicable, describes the camera setting that specifies the minimum video duration (in seconds) that the camera will record when triggered. Leave blank if not applicable.

**Viewshed**
:   The area visible to the camera as determined by its lens angle (in degrees) and trigger distance (Moeller et al., 2023).

**Viewshed density estimators**
:   Methods used to estimate the abundance of unmarked populations from observations of animals that relate animal observations to the space directly sampled by each camera’s viewshed (Moeller et al., 2023); they result in viewshed density estimates that can be extrapolated to abundance within broader sampling frames (Gilbert et al., 2020; Moeller et al., 2023).

**Visit**
:   When a crew has gone to a location to deploy, service, or retrieve a remote camera.

**\*Visit Comments**
:   Comments describing additional details about the deployment and/or service/retrieval visits.

**Visit metadata**
:   Metadata that should be collected each time a camera location is visited to deploy, service or retrieve a camera. Other relevant metadata fields that should be collected differ when a camera is deployed vs. serviced or retrieved.


:   Refer to Appendix A - Table A5, Camera Deployment Field Datasheet, and Camera Service/Retrieval Field Datasheet.

**Visual lure**
:   Any material that draws animals closer via their sense of sight (Schlexer, 2008).

**Walktest**
:   A test performed to ensure the camera height, tilt, etc., adequately captures the desired detection zone. The user will 1) activate the walktest mode, 2) attach the camera at the desired height / angle, 3) walk in front of the camera to a specified distance (i.e., the "Walktest Distance," e.g., 5 m), and 4) wave their hand in front of the camera (usually at ground level and a chosen height [i.e., the "Walktest Height," e.g., 0.8 m]) to determine if the camera is activating (a light on the camera will flash).

**\*Walktest Complete**
:   Whether a walktest was performed to ensure the camera height, tilt, etc., adequately captures the desired detection zone. The user will 1) activate the walktest mode, 2) attach the camera at the desired height / angle, 3) walk in front of the camera to a specified distance (i.e., the "Walktest Distance," e.g., 5 m), and 4) wave their hand in front of the camera (usually at ground level and a chosen height [i.e., the "Walktest Height," e.g., 0.8 m]) to determine if the camera is activating (a light on the camera will flash).

**\*Walktest Distance (m)**
:   The horizontal distance (recorded in metres to the nearest 0.05 m) from the camera at which the crew performs the walktest. Leave blank if not applicable.

**\*Walktest Height (m)**
:   The vertical distance (recorded in metres to the nearest 0.05 m) from the camera at which the crew performs the walktest. Leave blank if not applicable.

**Zero-inflated negative binomial (ZINB) regression (McCullagh & Nelder, 1989)**
:   A regression model used in the setting of excess zeros (zero-inflation) and overdispersion. This approach is a two-part model, where the zero-inflation is modelled separately from the counts and assumes that the count (abundance) is "conditional" on the zero-inflation model (occurrence) model. [relative abundance indices]

**Zero-inflated Poisson (ZIP) regression (Lambert, 1992)**
:   A regression model for count data that both follows the Poisson distribution and contains excess zeros (Lambert, 1992). ZIP models are only appropriate for data for which the overdispersion is not solely due to zero-inflation. [relative abundance indices]

**Zero-inflation**
:   An excess of zeros that is "so large that those expected in standard distributions (e.g., normal, Poisson, binomial, negative binomial and beta)" (Heilbron, 1994) violate the assumptions of such distributions (Martin et al., 2005). Excess zeroes can be a result of ecological effects ("true" zeros) or due to sampling or observer error ("false zeros") (Martin et al., 2005). Excess zeroes contribute to overdispersion, but they don't necessarily account for all excess variability (Blasco-Moreno et al., 2019).
</p>

````
`````

``````