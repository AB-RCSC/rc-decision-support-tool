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
(glossary3)=
# Glossary2

<!-- https://mystmd.org/guide/glossaries-and-terms -->

Bold indicates a metadata field in either the [AB Metadata Standards](https://ab-rcsc.github.io/RCSC-WildCAM_Remote-Camera-Survey-Guidelines-and-Metadata-Standards/2_metadata-standards/2_0.1_Citation-and-Info.html) (RCSC, 2024) or [Remote Camera Survey Guidelines](https://ab-rcsc.github.io/RCSC-WildCAM_Remote-Camera-Survey-Guidelines-and-Metadata-Standards/1_survey-guidelines/1_0.1_Citation-and-Info.html) (RCSC et al., 2024).<br>
An asterisk (*) indicates the field is optional and not required by the AB Metadata Standards (RCSC, 2024) and B.C. Metadata Standards (RISC, 2019).

```{glossary}
[**Access Method*]{#access_method}
  The method used to reach the camera location (e.g., on "Foot," "ATV," "Helicopter," etc.).

[*Adult*]{#age_class_adult}
  Animals that are old enough to breed; reproductively mature.

[*Age Class*]{#age_class}
  The age classification of individual(s) being categorized (e.g., "Adult," "Juvenile," "Subadult," "Subadult - Young of Year," "Subadult - Yearling", or "Unknown").

[*Analyst*]{#analyst}
  The first and last names of the individual who provided the observation data point (species identification and associated information). If there are multiple analysts for an observation, enter the primary analyst.

[**Animal ID*]{#animal_id}
  A unique ID for an animal that can be uniquely identified (e.g., marked in some way). If multiple unique individuals are identified, enter an Animal ID for each as a unique row. Leave blank if not applicable.

[Audible lure]{#baitlure_audible_lure}
  Sounds imitating noises of prey or conspecifics that draw animals closer by eliciting curiosity (Schlexer, 2008).

[Bait]{#baitlure_bait}
  A food item (or other substance) that is placed to attract animals via the sense of taste and olfactory cues (Schlexer, 2008).

[*Bait/Lure Type*]{#baitlure_bait_lure_type}
  The type of bait or lure used at a camera location. Record "None” if a Bait/Lure Type was not used and "Unknown" if not known. If "Other,” describe in the Deployment Comments.

[**Batteries Replaced*]{#batteries_replaced}
  Whether the camera's batteries were replaced.

[**Behaviour*]{#behaviour}
  The behaviour of the individual(s) being categorized (e.g., "Standing," "Drinking," "Vigilant," etc.).

[**Camera Active On Arrival*]{#camera_active_on_arrival}
  Whether a camera was functional upon arrival.

[**Camera Active On Departure*]{#camera_active_on_departure}
  Whether a camera was functional upon departure.

[Camera angle]{#camera_angle}
  The degree at which the camera is pointed toward the FOV Target Feature relative to the horizontal ground surface (with respect to slope, if applicable).

[**Camera Attachment*]{#camera_attachment}
  The method/tools used to attach the camera (e.g., attached to a tree with a bungee cord; reported as codes such as "Tree + Bungee/Strap"). If "Other,” describe in the Camera Location Comments.

[**Camera Damaged*]{#camera_damaged}
  Whether the camera was damaged or malfunctioning; if there is any damage to the device (physical or mechanical), the crew should describe the damage in the Service/Retrieval Comments.

[Camera days per camera location]{#camera_days_per_camera_location}
  The number of days each camera was active and functioning during the period it was deployed (e.g., 24-hour periods or the difference in days between the Deployment Start Date Time and the Deployment End Date Time if there were no interruptions).

[**Camera Direction (degrees)*]{#camera_direction}
  The cardinal direction that a camera faces. Ideally, cameras should face north (N; i.e. "0" degrees), or south (S; i.e. "180" degrees) if north is not possible. The Camera Direction should be chosen to ensure the field of view (FOV) is of the original FOV target feature.

[*Camera Height (m)*]{#camera_height}
  The height from the ground (below snow) to the bottom of the lens (metres; to the nearest 0.05 m).

[*Camera ID*]{#camera_id}
  A unique alphanumeric ID for the camera that distinguishes it from other cameras of the same make or model.

[Camera location]{#camera_location}
  The location where a single camera was placed (recorded as "Camera Location Name").

[**Camera Location Characteristic(s)*]{#camera_location_characteristics}
  Any significant features around the camera at the time of the visit. This may include for example, manmade or natural linear features (e.g., trails), habitat types (e.g., wetlands), wildlife structure (e.g., beaver dam). If "Other,” describe in the Camera Location Comments.<br><br>  Camera Location Characteristics differ from FOV Target Features in that Camera Location Characteristics could include those not in the camera's Field of View. If "Other,” describe in the Camera Location Comments.

[**Camera Location Comments*]{#camera_location_comments}
  Comments describing additional details about a camera location.

[*Camera Location Name*]{#camera_location_name}
  A unique alphanumeric identifier for the location where a single camera was placed (e.g., "bh1," "bh2").

[*Camera Make*]{#camera_make}
  The make of a particular camera (i.e., the manufacturer, e.g., "Reconyx" or "Bushnell”).

[*Camera Model*]{#camera_model}
  The model number or name of a particular camera (e.g., "PC900" or "Trophy Cam HD").

[*Camera Serial Number*]{#camera_serial_number}
  The serial number of a particular camera, which is usually found inside the camera cover (e.g., "P900FF04152022").

[Camera spacing]{#camera_spacing}
  The distance between cameras (i.e., also referred to as "inter-trap distance"). This will be influenced by the chosen sampling design, the Survey Objectives, the Target Species and data analysis.

[Capture-recapture (CR) model / Capture-mark-recapture (CMR) model (Karanth, 1995; Karanth & Nichols, 1998)]{#mods_cr_cmr}
  A method of estimating the abundance or density of marked populations using the number of animals detected and the likelihood animals will be detected (detection probability). CR (Karanth, 1995; Karanth & Nichols, 1998) can be used to estimate vital rates where all newly detected unmarked animals become marked and are distinguishable in future (Efford, 2022). Spatially explicit capture-recapture (SECR; Borchers & Efford, 2008; Efford, 2004; Royle & Young, 2008) models have largely replaced CR and CMR models and provide more accurate density estimates (Blanc et al., 2013, Obbard et al., 2010, Sollmann et al., 2011).

[Categorical partial identity model (catSPIM) (Augustine et al., 2019; Sun et al., 2022)]{#mods_catspim}
  A method used to estimate the density of partially marked populations in which the "spatial locations of where partial identity samples are captured to probabilistically resolve their complete identities" (Augustine et al., 2018, 2019). catSPIM models use partial identity traits (e.g., sex class, antler points) to help infer individual identities (Augustine et al., 2019; Sun et al., 2022). catSPIM is an extension of the SC model (Chandler & Royle, 2013).

[Clustered design]{#sampledesign_clustered}
  Multiple cameras are deployed at a sample station (Figure 3d). A clustered design can be used within a systematic or stratified approach (i.e., systematic clustered design or as a clustered random design \[Wearn & Glover-Kapfer, 2017\]).

[Convenience design]{#sampledesign_convenience}
  Camera locations or sample stations are chosen based on logistic considerations (e.g., remoteness, access constraints, and/or costs).

[Crew]{#crew}
  The first and last names of all the individuals who collected data during the deployment visit ("Deployment Crew") and service/retrieval visit ("Service/Retrieval Crew").

[Cumulative detection probability]{#cumulative_det_probability}
  The probability of detecting a species at least once during the entire survey (Steenweg et al., 2019).

[Density]{#density}
  The number of individuals per unit area.

[Deployment]{#deployment}
  A unique placement of a camera in space and time (recorded as "Deployment Name"). There may be multiple deployments for one camera location. Deployments are often considered as the time between visits (i.e., deployment to service, service to service, and service to retrieval). Any change to camera location, sampling period, camera equipment (e.g., Trigger Sensitivity setting, becomes non-functioning), and/or conditions (e.g., not baited then baited later; camera SD card replaced) should be documented as a unique deployment.

[**Deployment Area Photo Numbers*]{#deployment_area_photo_numbers}
  The image numbers for the deployment area photos (if collected, e.g., "DSC100"). These are optionally documented on a Camera Deployment Field Datasheet for each set of camera deployment area photos. Leave blank if not applicable.

[Deployment area photos]{#deployment_area_photos}
  Photos of the area around the camera location, collected as a permanent, visual record of the FOV Target Features, Camera Location Characteristics, environmental conditions (e.g., vegetation, ecosite, weather) or other variables of interest. The recommendation includes collecting four photos taken from the centre of the target detection zone (Figure 5), facing each of the four cardinal directions. The documentation of the collection of these photos is recorded as "Deployment Area Photos Taken" (Y/N).

[**Deployment Area Photos Taken*]{#deployment_area_photos_taken}
  Whether deployment area photos were taken (yes/no; optional). The recommendation includes collecting four photos taken from the centre of the target detection zone (Figure 5), facing each of the four cardinal directions.

[**Deployment Comments*]{#deployment_comments}
  Comments describing additional details about the deployment.

[*Deployment Crew*]{#deployment_crew}
  The first and last names of the individuals who collected data during the deployment visit.

[*Deployment End Date Time (DD-MMM-YYYY HH\:MM\:SS)*]{#deployment_end_date_time}
  The date and time that the data was retrieved for a specific deployment (e.g., 27-Jan-2019 23\:00\:00). The Deployment End Date Time may not coincide with when the last image or video was collected (i.e., the Image Set End Date Time). Recording this field allows users to account for deployments where no images were captured and to confirm the last date and time that the camera was active.

[**Deployment Image Count*]{#deployment_image_count}
  The total number of images collected during the deployment, including false triggers (i.e., empty images with no wildlife or human present species) and those triggered by a time-lapse setting (if applicable).

[Deployment metadata]{#deployment_metadata}
  Metadata that is collected each time a camera is deployed. Each deployment event should have its own Camera Deployment Field Datasheet. The relevant metadata fields that should be collected differ when a camera is deployed vs. serviced or retrieved.<br><br>Refer to Appendix A - Table A5 and Camera Deployment Field Datasheet.

[*Deployment Name*]{#deployment_name}
  A unique alphanumeric identifier for a unique camera deployed during a specific survey period (ideally recorded as "Camera Location Name,"_",Deployment Start Date” (or …*"Deployment End Date") (e.g., "bh1_17-Jul-2018" or "bh1_17-Jul-2018_21-Jan-2019”).<br><br>  Alternative naming conventions may be used, but the goal should be to minimize duplicate Image Names.

[*Deployment Start Date Time (DD-MMM-YYYY HH\:MM\:SS)*]{#deployment_start_date_time}
  The date and time that a camera was placed for a specific deployment (e.g., 17-Jan-2018 10\:34\:22).<br><br>The Deployment Start Date Time may not coincide with when the first image or video was collected (i.e., the Image Set Start Date Time). Recording this field allows users to account for deployments where no images were captured and to confirm the first date and time a camera was active.

[Deployment visit]{#deployment_visit}
  When a crew has gone to a location to deploy a remote camera.

[Detection "event”]{#detection_event}
  A group of images or video clips that are considered independent from other images or video clips based on a certain time threshold (or "inter-detection interval”). For example, 30 minutes (O’Brien et al., 2003; Gerber et al., 2010; Kitamura et al., 2010; Samejima et al., 2012) or 1 hour (e.g., Tobler et al., 2008; Rovero & Marshall, 2009).

[Detection distance]{#detection_distance}
  The maximum distance that a sensor can detect a target (Wearn and Glover-Kapfer, 2017).

[Detection probability (aka detectability)]{#detection_probability}
  The probability (likelihood) that an individual of the population of interest is included in the count at time or location *i*.

[Detection rate]{#detection_rate}
  The frequency of independent detections within a specified time period.

[Detection zone]{#detection_zone}
  The area (conical in shape) in which a remote camera can detect the heat signature and motion of an object (Rovero & Zimmermann, 2016) (Figure 5).

[Distance sampling (DS) model (Howe et al., 2017)]{#mods_distance_sampling}
  A method to estimate abundance by using distances at which animals are detected (from survey lines or points) to model abundance as a function of decreasing detection probability with animal distance from the camera (using a decay function) (Cappelle et al., 2021; Howe et al., 2017).

[*Easting Camera Location*]{#easting_camera_location}
  The easting UTM coordinate of the camera location (e.g., "337875"). Record using the NAD83 datum. Leave blank if recording the Longitude instead.

[Effective detection distance]{#effective_detection_distance}
  The distance from a camera that would give the same number of detections if all animals up to that distance are perfectly detected, and no animals that are farther away are detected; Buckland, 1987, Becker et al., 2022).

[*Event Type*]{#event_type}
  Whether detections were reported as an individual image captured by the camera ("Image”), a "Sequence,” or "Tag.”

[False trigger]{#false_trigger}
  Blank images (no wildlife or human present). These images commonly occur when a camera is triggered by vegetation blowing in the wind.

[Field of View (FOV)]{#field_of_view}
  The extent of a scene that is visible in an image (Figure 5); a large FOV is obtained by "zooming out" from a scene, whilst "zooming in" will result in a smaller FOV (Wearn & Glover-Kapfer, 2017).

[Flash output]{#settings_flash_output}
  The camera setting that provides the level of intensity of the flash (if enabled).

[*FOV Target Feature*]{#fov_target}
  A specific man-made or natural feature at which the camera is aimed to maximize the detection of wildlife species or to measure the use of that feature. Record "None” if a FOV Target Feature was not used and "Unknown" if not known. If "Other,” describe in the Camera Location Comments.

[**FOV Target Feature Distance (m)*]{#fov_target_distance}
  The distance from the camera to the FOV Target Feature (in metres; to the nearest 0.5 m). Leave blank if not applicable.

[*GPS Unit Accuracy (m)*]{#gps_unit_accuracy}
  The margin of error of the GPS unit used to record spatial information (e.g., "5" \[m\]), such as the coordinates of the camera location. On most GPS units (e.g., "Garmin") this information is provided on the unit’s satellite information page.

[**Human Transport Mode/Activity*]{#human_transport_mode_activity}
  The activity performed or mode of transportation used by a human observed (e.g., hiker, skier, off-highway vehicle, etc.). This categorical field should be populated when data on humans (in addition to wildlife) are collected. Leave blank if not applicable and record "Unknown" if not known.

[Hurdle model (Mullahy, 1986; Heilbron 1994)]{#mods_hurdle}
  A regression model used in the setting of excess zeros (zero-inflation) and overdispersion (Mullahy, 1986). Hurdle models (aka "zero-altered" models) differ from zero-inflation models in that they are two-part models, and the zero and non-zero counts are modelling separately (thus, they are only adequate when the counting process cannot generate a zero value) (Blasco-Moreno et al., 2019). \[relative abundance indices\]

[Image]{#image}
  An individual image captured by a camera, which may be part of a multi-image sequence (recorded as "Image Name").

[Image classification]{#image_classification}
  The process of assigning class labels to an image according to the wildlife species, other entities (e.g., human, vehicle), or conditions within the image. Image classification can be performed manually or automatically by an artificial intelligence (AI) algorithm. Image classification is sometimes used interchangeably with "image tagging."

[Image classification confidence]{#image_classification_confidence}
  The likelihood of an image containing an object of a certain class (Fennell et al., 2022).

[**Image Flash Output*]{#image_flash_output}
  The Image Flash Output is an image metadata field indicating the level of intensity of the flash \[if enabled/applicable\]). Record as reported in the image Exif data (e.g., "Flash Did Not Fire", "Auto"). This field is in text format; record "Unknown" if not known; leave blank if not applicable.

[**Image Infrared Illuminator*]{#image_infrared_illuminator}
  The Image Infrared Illuminator is an image metadata field indicating whether the infrared illuminator setting was enabled (if applicable; to obtain greater visibility at night by producing infrared light). Record as reported in the image Exif data (e.g., "On" or "Off"). This field is categorical; leave blank if not applicable and record "Unknown" if not known.

[*Image Name*]{#image_name}
  A unique alphanumeric identifier for the image. It is important to include (at a minimum) the camera location, date, time, and image number when generating an Image Name to avoid duplicate file names (e.g., "bh1_17-Jul-2018_P900FF04152022_22-Jul-2018 10\:34\:22_img_100" or "bh1_17-Jul-2018_22-Jul-2018_10:34:22_img_100").

[Image processing]{#image_processing}
  The series of operations that are taken to extract information from images. In the case of remote camera data, it can include loading the images into a processing platform, extracting information from the image metadata (e.g., the date and time the image was taken), running an artificial intelligence (AI) algorithm to identify empty images, classifying animals or other entities within the image.

[Image Sequence]{#image_sequence}
  The order of the image in a rapid-fire sequence as reported in the image Exif data (text; e.g., "1 of 1" or "1 of 3"). Leave blank if not applicable.

[*Image Set End Date Time (DD-MMM-YYYY HH\:MM\:SS)*]{#image_set_end_date_time}
  The date and time of the last image or video collected during a specific deployment (e.g., "17-Jan-2018 22\:10\:05").<br><br> The Image Set End Date Time may not coincide with the deployment end date time. Recording this field allows users to account for deployments that were conducted but for which no data was found and to confirm the last date and time a camera was active (if functioning) if no images or videos were captured prior to Service/Retrieval (especially valuable if users did not collect Time-lapse images or if the camera malfunctioned).

[*Image Set Start Date Time (DD-MMM-YYYY HH\:MM\:SS)*]{#image_set_start_date_time}
  The date and time of the first image or video collected during a specific deployment (e.g., "17-Jan-2018 12\:00\:02”).<br><br>The Image Set Start Date Time may not coincide with the Deployment Start Date Time. Recording this field allows users to confirm the first date and time a camera was active (reliable if Time-lapse images were collected; especially valuable if the user scheduled a start delay).

[Image tagging]{#image_tagging}
  The process of classifying an image according to the wildlife species, other entities (e.g., human, vehicle), or conditions within the image. Image tagging may follow image classification to further classify characteristics of the individuals (e.g., age class, sex class, or behaviour) or entities within the image.

[**Image Trigger Mode*]{#image_trigger_mode}
  The type of trigger mode used to capture the image as reported in the image Exif data (e.g., "Time Lapse", "Motion Detection," "CodeLoc Not Entered," "External Sensor"). Record "Unknown" if not known.

[**Image/Sequence Comments*]{#image_sequence_comments}
  Comments describing additional details about the image/sequence.

[*Image/Sequence Date Time (DD-MMM-YYYY HH\:MM\:SS)*]{#image_sequence_date_time}
  The date and time of an image, or the image chosen to represent the sequence, recorded as "DD-MMM-YYYY HH\:MM\:SS" (e.g., 22-Jul-2018 11:02:02).<br><br>Sequence date/time information may be reported for a "representative image" of a sequence (i.e., the image with the most information). For example, if three images were included in a sequence, but the Sex Class could only be discerned in the second image \[all else remaining equal\], the second image would be the best representative image of the sequence.<br><br>The Image/Sequence Date Time differs from the Image Set Start Date Time which refers to the first image or video collected during a deployment.

[Imperfect detection]{#imperfect_detection}
  Species are often detected "imperfectly," meaning that they are not always detected when they are present (e.g., due to cover of vegetation, cryptic nature or small size) (MacKenzie et al., 2004).

[Independent detections]{#independent_detections}
  Detections that are deemed to be independent based on a user-defined threshold (e.g., 30 minutes).

[*Individual Count*]{#individual_count}
  The number of unique individuals being categorized. Depending on the Event Type, this may be recorded as the total number of individuals, or according to Age Class and/or Sex Class.

[Infrared illuminator]{#settings_infrared_illum}
  The camera setting that can be enabled (if applicable to the camera make and camera model) to obtain greater visibility at night by producing infrared light. This field is categorical; leave blank if not applicable and record "Unknown" if not known.

[Instantaneous sampling (IS) (Moeller et al., 2018)]{#mods_instantaneous_sampling}
  A method used to estimate abundance or density from time-lapse images from randomly deployed cameras; the number of unique individuals (the count) is needed (Moeller et al., 2018).

[Intensity of use (Keim et al., 2019)]{#intensity_of_use}
  The expected number of use events of a specific resource unit during a unit of time… \[which characterizes\] how frequently a particular resource unit is used (Keim et al., 2019). The intensity of use differs from the probability of use (which characterizes "the probability of at least one use event of that resource unit during a unit of time"; Keim et al., 2019).

[Inter-detection interval]{#inter_detection_interval}
  A user-defined threshold used to define a single "detection event" (i.e., independent "events") for group of images or video clips (e.g., 30 minutes or 1 hour). The threshold should be recorded in the Survey Design Description.

[Inventory]{#mods_inventory}
  Rapid assessment surveys to determine what species are present in a given area at a given point in time; there is no attempt made to quantify aspects of communities or populations (Wearn & Glover-Kapfer, 2017).

[*Juvenile*]{#age_class_juvenile}
  Animals in their first summer, with clearly juvenile features (e.g., spots); mammals older than neonates but that still require parental care.

[Kernel density estimator]{#kernel_density_estimator}
  The probability of "utilization" (Jennrich & Turner, 1969); describes the relative probability of use (Powell & Mitchell, 2012).

[**Key ID*]{#key_id}
  The unique ID for the specific key or set of keys used to lock/secure the camera to the post, tree, etc.

[*Latitude Camera Location*]{#latitude_camera_location}
  The latitude of the camera location in decimal degrees to five decimal places (e.g., "53.78136"). Leave blank if recording Northing instead.

[*Longitude Camera Location*]{#longitude_camera_location}
  The longitude of the camera location in decimal degrees to five decimal places (e.g., "-113.46067"). Leave blank if recording Easting instead.

[Lure]{#baitlure_lure}
  Any substance that draws animals closer; lures include scent (olfactory) lure, visual lure and audible lure (Schlexer, 2008).

[Marked individuals / populations / species]{#typeid_marked}
  Individuals, populations, or species (varies with modelling approach and context) that can be identified using natural or artificial markings (e.g., coat patterns, scars, tags, collars).

[Mark-resight (MR) model (Arnason et al., 1991; McClintock et al., 2009)]{#mods_mr}
  A method used to estimate the abundance of partially marked populations using the number of marked individuals, the number of unmarked individuals, and the detection probability from marked animals (Wearn & Glover-Kapfer, 2017). MR is similar to capture-recapture (CR; Karanth, 1995; Karanth & Nichols, 1998) models, except only a portion of animals are individually identified.

[Metadata]{#metadata}
  Data that provides information about other data (e.g., the number of images on an SD card).

[Model assumption]{#mods_modelling_assumption}
  Explicitly stated (or implicitly premised) conventions, choices and other specifications (e.g., about the data, wildlife ecology/behaviour, the relationships between variables, etc.) on which a particular modelling approach is based that allows the model to provide valid inference.

[Modelling approach]{#mods_modelling_approach}
  The method used to analyze the camera data, which should depend on the state variable, e.g., occupancy models \[MacKenzie et al., 2002\], spatially explicit capture recapture (SECR) for density estimation \[Chandler and Royle, 2013\], etc. and the Target Species.

[*Motion Image Interval (seconds)*]{#settings_motion_image_interval}
  The time (in seconds) between images within a multi-image sequence that occur due to motion, heat, or activation of external detector devices. The Motion Image Interval is pre-set in the camera’s settings by the user, but the time at which the camera collects images because of this setting is influenced by the presence of movement or heat. For example, if the camera was set to take 3 images per event at a Motion Image Interval of 3 seconds when the camera detects motion or heat, the first image will be collected (e.g., at 09\:00\:00), the second image will be collected 3 seconds later (09:00:03), and the third will be collected 3 seconds after that (09\:00\:06).<br><br>This setting differs from the Quiet Period in that the delay occurs between images contained within a multi-image sequence, rather than between multi-image sequences (as in Quiet Period). If a Motion Image Interval was not set, enter "0" seconds (i.e., instantaneous).

[Negative binomial (NB) regression (Mullahy, 1986)]{#mods_negative_binomial}
  A regression model used for count data with overdispersion but without zero-inflation. \[relative abundance indices\]

[N-mixture models]{#mods_n_mixture}
  A class of models for estimating absolute abundance using replicated counts of animals from several different sites; site-specific counts are treated as independent random variables to estimate the number of animals available for capture at each site; detection is imperfect (Royle 2004). N-mixture models are a type of site-structured model (i.e., that "treat each camera as though it samples... \[a\] distinct population within a larger meta-population" \[Clarke et al., 2023\]).

[*Northing Camera Location*]{#northing_camera_location}
  The northing UTM coordinate of the camera location (e.g., "5962006"). Record using the NAD83 datum. Leave blank if recording the Latitude instead.

[Occupancy]{#occupancy}
  The probability a site is occupied by the species.

[Occupancy model (MacKenzie et al., 2002)]{#mods_occupancy}
  A modelling approach used to account for imperfect detection by first evaluating the detection probability of a species via detection histories (i.e., present or absent) to determine the probability of the true presence or absence of a species at a site (MacKenzie et al., 2002).

[Overdispersion]{#mods_overdispersion}
  A variance significantly larger than the mean (Bliss & Fisher, 1953); greater variability in a set of data than predicted by the error structure of the model (Harrison et al., 2018); excess variability can be caused by zero inflation, non-independence of counts, or both (Zuur et al., 2009).

[Paired design]{#sampledesign_paired}
  A form of "clustered design” where two cameras that are placed closely together to increase detection probability ("paired cameras"), to evaluate certain conditions ("paired sites", e.g., on- or off trails), etc. Paired placements can help to account for other variability that might occur (i.e., variation in habitat quality). For some objectives, pairs of cameras might be considered subsamples within another sampling design (e.g., simple random, stratified random, systematic).

[Partially marked individuals / populations / species]{#typeid_partially_marked}
  Individuals, populations, or species (varies with modelling approach and context) that have a suite of partially identifying traits (e.g., antler points, sex class, age class). For populations/species, those in which a proportion of individuals carry marks or in which individuals themselves are partially marked.

[*Photos Per Trigger*]{#settings_photos_per_trigger}
  The camera setting that describes the number of photos taken each time the camera is triggered.

[Poisson regression]{#mods_poisson}
  A regression model for count data used when data are not overdispersed or zero-inflated (Lambert, 1992). \[relative abundance indices\]

[Project]{#project}
  A scientific study, inventory or monitoring program that has a certain objective, defined methods, and a defined boundary in space and time (recorded as "Project Name").

[*Project Coordinator*]{#project_coordinator}
  The first and last name of the primary contact for the project.

[*Project Coordinator Email*]{#project_coordinator_email}
  The email address of the Project Coordinator.

[*Project Description*]{#project_description}
  A description of the project objective(s) and general methods.

[*Project Name*]{#project_name}
  A unique alphanumeric identifier for each project. Ideally, the Project Name should include an abbreviation for the organization, a brief project name, and the year the project began (e.g., "uofa_oilsands_2018").

[Pseudoreplication]{#pseudoreplication}
  When observations are not statistically independent (spatially or temporally) but are treated as if they are independent.

[*Purpose of Visit*]{#purpose_of_visit}
  The reason for visiting the camera location (i.e. to deploy the camera \["Deployment"\], retrieve the camera \["Retrieve"\] or to change batteries/SD card or replace the camera \["Service"\]).

[*Quiet Period (seconds)*]{#settings_quiet_period}
  The user-defined camera setting which provides the time (in seconds) between shutter "triggers" if the camera was programmed to pause between firing initially and firing a second time. If a Quiet Period was not set, enter "0."<br><br>Also known as "time lag" (depending on the Camera Make and Camera Model; Palmer et al., 2018). The Quiet Period differs from the Motion Image Interval in that the delay occurs between multi-image sequences rather than between the images contained within multi-image sequences (as in the Motion Image Interval).

[Random (or "simple random”) design]{#sampledesign_random}
  Cameras occur at randomized camera locations (or sample stations) across the area of interest, sometimes with a predetermined minimum distance between camera locations (or sample stations).

[Random encounter and staying time (REST) model (Nakashima et al., 2018)]{#mods_rest}
  A recent modification of the REM (Nakashima et al., 2018) that substitutes staying time (i.e., the cumulative time in the cameras' detection zone) for movement speed (staying time and movement speed are inversely proportional) (Cappelle et al., 2021).

[Random encounter model (REM) (Rowcliffe et al., 2008, 2013)]{#mods_rem}
  A method used to estimate the density of unmarked populations; uses the rate of independent captures, an estimate of movement rate, average group size, and the area sampled by the remote camera.

[Recovery time]{#recovery_time}
  The time necessary for the camera to prepare to capture the next photo after the previous one has been recorded (Trolliet et al., 2014).

[Registration area]{#fov_registration_area}
  The area in which an animal entering has at least some probability of being captured on the image.

[Relative abundance indices]{#mods_relative_abundance}
  An index of relative abundance. When observational data is converted to a detection rate (i.e., the frequency \[count\] of independent detections of a species within a distinct time period). An index can be a count of animals or any sign that is expected to vary with population size (Caughley, 1977; O'Brien, 2011).

[**Remaining Battery (%)*]{#remaining_battery_percent}
  The remaining battery power (%) of batteries within a camera.

[Royle-Nichols model (Royle & Nichols, 2003; MacKenzie et al., 2006)]{#mods_royle_nichols}
  A method used to estimate population abundance or density, which assumes that individuals are counted only once per sampling occasion (Royle, 2004), but that does not require all individuals to be marked. Royle-Nichols models are a type of site-structured model (i.e., that "treat each camera as though it samples... \[a\] distinct population within a larger meta-population" \[Clarke et al., 2023\]).

[Sample station]{#sample_station}
  A grouping of two or more non-independent camera locations, such as when cameras are clustered or paired (recorded as "Sample Station Name").

[*Sample Station Name*]{#sample_station_name}
  A sequential alphanumeric identifier for each grouping of two more non-independent camera locations (when cameras are deployed in clusters, pairs, or arrays; e.g., "ss1” in "ss1_bh1”, "ss1_bh2”, "ss1_bh3” etc.). Leave blank if not applicable.

[Scent lure]{#baitlure_scent_lure}
  Any material that draws animals closer via their sense of smell (Schlexer, 2008).

[**SD Card ID*]{#sd_card_id}
  The ID label on an SD card (e.g., "cmu_100").

[**SD Card Replaced*]{#sd_card_replaced}
  Whether the SD card was replaced.

[**SD Card Status (% Full)*]{#sd_card_status}
  The remaining storage capacity on an SD card; collected during a camera service or retrieval.

[**Security*]{#security}
  The equipment used to secure the camera (e.g., "Security box," "Bracket," "Bracket + Screws," or "None").

[Sequence]{#sequence}
  A user-defined group of images or video clips considered as a single "detection event" (recorded as "Sequence Name"); often users choose a certain time threshold (or "inter-detection interval") to define independent "events"; e.g., 30 minutes or 1 hour. The threshold should be recorded in the Survey Design Description).

[*Sequence Name*]{#sequence_name}
  A unique alphanumeric identifier for a multi-image sequence. The Sequence Name should ideally consist of the Deployment Name and the names of the first and last images and videos in the sequence (separated by "\_") (i.e., "Deployment Name",\_",img\_#\[name of first image in sequence\],"\_",img\_#\[name of last image in sequence\] (e.g., "bh1_22-Jul-2018_img_001-img_005"). Leave blank if not applicable.

[Service/Retrieval]{#service_retrieval}
  When a crew has gone to a location to service or retrieve a remote camera.

[**Service/Retrieval Comments*]{#service_retrieval_comments}
  Comments describing additional details about the service/retrieval.

[*Service/Retrieval Crew*]{#service_retrieval_crew}
  The first and last names of the individuals who collected data during the service/retrieval visit.

[Service/retrieval metadata]{#service_retrieval_metadata}
  Metadata that should be collected each time a camera location is visited to service or retrieve a camera, including data on any change to the camera location, sampling period, and/or setting type (e.g., not baited and then baited later). The relevant metadata fields that should be collected differ when a camera is deployed vs. serviced or retrieved.<br><br>Refer to Appendix - Table A5 and the Camera Service/Retrieval Field Datasheet.

[Service/Retrieval visit]{#service_retrieval_visit}
  When a crew has gone to a location to service or retrieve a remote camera.

[*Sex Class*]{#sex_class}
  The sex classification of individual(s) being categorized (e.g., "Male," "Female," or "Unknown").

[Space-to-event (STE) model (Moeller et al., 2018)]{#mods_ste}
  A method used to estimate abundance or density that accounts for variable detection probability through the use of time-lapse images and is unaffected by animal movement rates (collapses sampling intervals to an instant in time, and thus estimates are unaffected by animal movement rates) (Moeller et al., 2018).

[Spatial autocorrelation]{#spatial_autocorrelation}
  The tendency for locations that are closer together to be more similar.

[Spatial count (SC) model / Unmarked spatial capture-recapture (Chandler & Royle, 2013)]{#mods_sc}
  A method used to estimate the density of unmarked populations; similar to SECR (Borchers & Efford, 2008; Efford, 2004; Royle & Young, 2008; Royle et al., 2009); however, SC models account for individuals' unknown identities using the spatial pattern of detections (Chandler & Royle, 2013; Sun et al., 2022). SC uses trap-specific counts to estimate the location and number of activity centres to estimate density.

[Spatial mark-resight (SMR) (Chandler & Royle, 2013; Sollmann et al., 2013a, 2013b)]{#mods_smr}
  A method used to estimate the density of "partially marked populations by combining... \[detection\] histories of marked \[individuals\] and counts of unmarked \[individuals\]" (Doran-Myers, 2018) over several occasions (Sollman et al., 2013a; Rich et al., 2014; Whittington et al., 2018). SMR models can be implemented using different statistical frameworks, including Bayesian estimation (Royle and Young, 2008; Morin et al., 2022).

[Spatial partial identity model (2-flank SPIM) (Augustine et al., 2018)]{#mods_2flankspim}
  A method used to estimate the density of partially marked populations in which the "spatial locations of where partial identity samples are captured to probabilistically resolve their complete identities” (Augustine et al., 2018). Paired sampling design is commonly used to capture both the right and left flanks of an animal to resolve individual identities (Augustine et al., 2018). 2-flank SPIM is an extension of the SCR model (Borchers & Efford, 2008; Efford, 2004; Royle & Young, 2008; Royle et al., 2009).

[Spatially explicit capture-recapture (SECR) / Spatial capture-recapture (SCR) (Borchers & Efford, 2008; Efford, 2004; Royle & Young, 2008; Royle et al., 2009)]{#mods_scr_secr}
  The SECR (or SCR) method is used to estimate the density of marked populations; an extension of traditional capture-recapture (CR; Karanth, 1995; Karanth & Nichols, 1998) models (Karanth, 1995; Karanth & Nichols, 1998) that explicitly accounts for camera location and animal movement (Burgar et al., 2018). SECR models use spatially referenced individual capture histories to infer where animals' home range centres are, assuming that detection probability decreases with increasing distance between cameras and home range centres (Clarke et al., 2023). SECR models can be implemented using different statistical frameworks, including Bayesian estimation (Royle and Young, 2008; Morin et al., 2022).

[*Species*]{#species}
  The capitalized common name of the species being categorized ("tagged”).

[**Stake Distance (m)*]{#stake_distance}
  The distance from the camera to a stake (in metres to the nearest 0.05 m). Leave blank if not applicable.

[State variable]{#state_variable}
  A formal measure that summarizes the state of a community or population at a particular time (Wearn & Glover-Kapfer, 2017), e.g., species richness or population abundance.

[Stratified design]{#sampledesign_stratified}
  The area of interest is divided into smaller strata (e.g., habitat type, disturbance levels), and cameras are placed within each stratum (e.g., 15%, 35% and 50% of sites within high, medium, and low disturbance strata).

[Stratified random design]{#sampledesign_stratified_random}
  The area of interest is divided into smaller strata (e.g., habitat type, disturbance levels), and then a proportional random sample of sites is selected within each stratum (e.g., 15%, 35% and 50% of sites within high, medium and low disturbance strata).

[Study area]{#study_area}
  A unique research, inventory or monitoring area (spatial boundary) within a project (there may be multiple study areas within a single project) (recorded as "Study Area Name").

[*Study Area Description*]{#study_area_description}
  A description for each unique research or monitoring area including its location, the habitat type(s), land use(s) and habitat disturbances (where applicable).

[*Study Area Name*]{#study_area_name}
  A unique alphanumeric identifier for each study area (e.g.,"oilsands_ref1”). If only one area was surveyed, the Project Name and Study Area Name should be the same.

[*Subadult*]{#age_class_subadult}
  Animals older than a "Juvenile" but not yet an "Adult"; a "Subadult" may be further classified into "Young of the Year" or "Yearling."

[*Subadult - Yearling*]{#age_class_subadult_yearling}
  Animals approximately one year old; has lived through one winter season; between "Young of Year" and "Adult."

[*Subadult - Young of Year*]{#age_class_subadult_youngofyear}
  Animals less than one year old; born in the previous year's spring, but has not yet lived through a winter season; between "Juvenile" and "Yearling."

[Survey]{#survey}
  A unique deployment period (temporal extent) within a project (recorded as "Survey Name").

[*Survey Design*]{#survey_design}
  The spatial arrangement of remote cameras within the study area for an individual survey. If "Hierarchical (multiple)\*”, include additional details in the Survey Design Description.<br><br>Note that we refer to different configurations of cameras more generally as study design and sampling design; however, the term "Survey Design" refers to study design as it applies to an individual survey. There may be multiple Survey Designs for surveys within a project; if this occurs, the Survey Design should be reported separately for each survey.

[**Survey Design Description*]{#survey_design_description}
  A description of any additional details about the Survey Design.

[*Survey Name*]{#survey_name}
  A unique alphanumeric identifier for each survey period (e.g., "fortmc_001").

[*Survey Objectives*]{#survey_objectives}
  The specific objectives of each survey within a project, including the Target Species, the state variables (e.g., occupancy, density), and proposed modelling approach(es). Survey Objectives should be specific, measurable, achievable, relevant, and time-bound (i.e., SMART).

[Systematic design]{#sampledesign_systematic}
  Camera locations occur in a regular pattern (e.g., a grid pattern) across the study area.

[Systematic random design]{#sampledesign_systematic_random}
  Camera locations are selected using a two-stage approach. Firstly, girds are selected systematically (to occur within a regular pattern) across the study area. The location of the camera within each grid is then selected randomly.

[*Tag*]{#tag}
  When individuals, or groups of individuals, are categorized within an image, regardless of whether the information applies to all of the individuals in the image. A single tag is applied to categorize one or more individuals with the same combination of characteristics (e.g., Adult Males displaying the same Behaviour). Conversely, multiple tags are applied when individuals in an image differ in their characteristics (e.g., an Adult and a Juvenile, all else remaining equal, are tagged separately). This could also occur for Age Class, Behaviour, Human Transport Mode/Activity, etc. Since multiple tags can occur for a single image, there may be multiple data rows for the same image (if the Event Type is at the "Tag" level).

[*Target Species*]{#target_species}
  The common name(s) of the species that the survey was designed to detect.

[Targeted design]{#sampledesign_targeted}
  Camera locations or sample stations are placed in areas that are known or suspected to have higher activity levels (e.g., game trails, mineral licks).

[Test image]{#test_image}
  An image taken from a camera after it has been set up to provide a permanent record of the visit metadata (e.g., Sample Station Name, Camera Location Name, Deployment Name, Crew, and Deployment Start Date Time \[DD-MMM-YYYY HH\:MM\:SS\]).<br><br>Taking a test image can be useful to compare the information from the image to that of which was collected on the Camera Service/Retrieval Field Datasheet after retrieval and can help in reducing recording errors.

[**Test Image Taken*]{#test_image_taken}
  Whether a test image (i.e., an image taken from a camera after it has been set up to provide a permanent record of the visit metadata) was taken. Arm the camera, from \~5 m in front, walk towards the camera while holding the Test Image Sheet.

[Time in front of the camera (TIFC) (Huggard, 2018; Warbington & Boyce, 2020; tested in Becker et al., 2022)]{#mods_tifc}
  A method used to estimate density that treats camera image data as quadrat samples (Becker et al., 2022).

[Time-lapse image]{#timelapse_image}
  Images that are taken at regular intervals (e.g., hourly or daily, on the hour). It is critical to take a minimum of one time-lapse image per day at a consistent time (e.g., 12:00 pm \[noon\]) to create a record of camera functionality and local environmental conditions (e.g., snow cover, plant growth, etc.). Time-lapse images may always be useful for modelling approaches that require estimation of the "viewshed" ("viewshed density estimators" such as REM or time-to-event (TTE) models; see Moeller et al., \[2018\] for advantages and disadvantages).

[Time-to-event (TTE) model (Moeller et al., 2018)]{#mods_tte}
  A method used to estimate abundance or density from the detection rate while accounting for animal movement rates (Moeller et al., 2018). The TTE model assumes perfect detection (though there is a model extension to account for imperfect detection that requires further testing).

[Total number of camera days]{#total_number_of_camera_days}
  The number of days that all cameras were active during the survey.

[Trigger "event”(trigger_event}
  An activation of the camera detector(s) that initiates the capture of a single or multiple images, or the recording of video.

[*Trigger Mode(s)* (camera settings)]{#settings_trigger_modes}
  The camera setting(s) that determine how the camera will triggerby motion ("Motion Image"), at set intervals ("Time-lapse image"), and/or by video ("Video"; possible with newer camera models, such as Reconyx HP2X).

[*Trigger Sensitivity*]{#settings_trigger_sensitivity}
  The camera setting responsible for how sensitive a camera is to activation (to "triggering") via the infrared and/or heat detectors (if applicable, e.g., Reconyx HyperFire cameras have a choice between "Low," "Low/Med," "Med," "Med/High," "High," "Very high" and "Unknown").

[Trigger speed]{#trigger_speed}
  The time delay necessary for the camera to shoot a photo once an animal has interrupted the infrared beam within the camera's detection zone (Trolliet et al., 2014). Trigger speed differs from Motion Image Interval (a camera setting specified by the user) in that the trigger speed is inherent to the Camera Make and Camera Model (e.g., two different cameras, models both with a Motion Image Interval set to "no delay," may not be able to capture images at the same speed).

[Unmarked individuals / populations / species]{#typeid_unmarked}
  Individuals, populations, or species (varies with modelling approach and context) that cannot be identified using natural or artificial markings (e.g., coat patterns, scars, tags, collars). Unmarked population models rely on supplementary data (e.g., animal movement speed) and/or assumptions as a surrogate for individual identification; that is, to distinguish between multiple detections of the same individual from detections of multiple individuals when individuals do not have unique features (Gilbert et al., 2020; Morin et al., 2022).

[User label]{#settings_userlabel}
  A label (up to 16 characters) that can be programmed in the camera’s settings, and that will be visible in the data band of all photos and videos taken by the camera (Reconyx, 2018). It is recommended that users program the Sample Station Name/Camera Location Name as the user label, which serves as a means to confirm which Sample Station Name/Camera Location Name is associated with the images/videos.

[*UTM Zone Camera Location*]{#utm_zone_camera_location}
  The number corresponding to the Universal Transverse Mercator (UTM) grid zone where the camera was placed (e.g., "12”). UTM is a coordinate system that divides the earth into grid zones that are identified with a number (representing a width of latitude) and letter (representing the hemisphere).<br><br>In Alberta the UTM zones are either 11, 12, or TTM. Enter all other UTM zones in the Camera Location Comments field (e.g., zones 7-10 for British Columbia), or use Latitude and Longitude instead of UTM coordinates.

[**Video Length (seconds)*]{#settings_video_length}
  If applicable, describes the camera setting that specifies the minimum video duration (in seconds) that the camera will record when triggered. Leave blank if not applicable.

[Viewshed]{#fov_viewshed}
  The area visible to the camera as determined by its lens angle (in degrees) and trigger distance (Moeller et al., 2023).

[Viewshed density estimators]{#fov_viewshed_density_estimators}
  Methods used to estimate the abundance of unmarked populations from observations of animals that relate animal observations to the space directly sampled by each camera’s viewshed (Moeller et al., 2023); they result in viewshed density estimates that can be extrapolated to abundance within broader sampling frames (Gilbert et al., 2020; Moeller et al., 2023).

[Visit]{#visit}
  When a crew has gone to a location to deploy, service, or retrieve a remote camera.

[**Visit Comments*]{#visit_comments}
  Comments describing additional details about the deployment and/or service/retrieval visits.

[Visit metadata]{#visit_metadata}
  Metadata that should be collected each time a camera location is visited to deploy, service or retrieve a camera. Other relevant metadata fields that should be collected differ when a camera is deployed vs. serviced or retrieved. <br/>Refer to Appendix A - Table A5, Camera Deployment Field Datasheet, and Camera Service/Retrieval Field Datasheet.

[Visual lure]{#baitlure_visual_lure}
  Any material that draws animals closer via their sense of sight (Schlexer, 2008).

[Walktest]{#walktest}
  A test performed to ensure the camera height, tilt, etc., adequately captures the desired detection zone. The user will 1) activate the walktest mode, 2) attach the camera at the desired height / angle, 3) walk in front of the camera to a specified distance (i.e., the "Walktest Distance," e.g., 5 m), and 4) wave their hand in front of the camera (usually at ground level and a chosen height \[i.e., the "Walktest Height," e.g., 0.8 m\]) to determine if the camera is activating (a light on the camera will flash).

[**Walktest Complete*]{#walktest_complete}
  Whether a walktest was performed to ensure the camera height, tilt, etc., adequately captures the desired detection zone. The user will 1) activate the walktest mode, 2) attach the camera at the desired height / angle, 3) walk in front of the camera to a specified distance (i.e., the "Walktest Distance," e.g., 5 m), and 4) wave their hand in front of the camera (usually at ground level and a chosen height \[i.e., the "Walktest Height," e.g., 0.8 m\]) to determine if the camera is activating (a light on the camera will flash).

[*Walktest Distance (m)*]{#walktest_distance}
  The horizontal distance from the camera at which the crew performs the walktest (metres; to the nearest 0.05 m). Leave blank if not applicable.

[*Walktest Height (m)*]{#walktest_height}
  The vertical distance from the camera at which the crew performs the walktest (metres; to the nearest 0.05 m). Leave blank if not applicable.

[Zero-inflated negative binomial (ZINB) regression (McCullagh & Nelder, 1989)]{#mods_zinb}
  A regression model used in the setting of excess zeros (zero-inflation) and overdispersion. This approach is a two-part model, where the zero-inflation is modelled separately from the counts and assumes that the count (abundance) is "conditional" on the zero-inflation model (occurrence) model. \[relative abundance indices\]

[Zero-inflated Poisson (ZIP) regression (Lambert, 1992)]{#mods_zip}
  A regression model for count data that both follows the Poisson distribution and contains excess zeros (Lambert, 1992). ZIP models are only appropriate for data for which the overdispersion is not solely due to zero-inflation. \[relative abundance indices\]

[Zero-inflation]{#mods_zero_inflation}
  An excess of zeros that is "so large that those expected in standard distributions (e.g., normal, Poisson, binomial, negative binomial and beta)" (Heilbron, 1994) violate the assumptions of such distributions (Martin et al., 2005). Excess zeroes can be a result of ecological effects ("true" zeros) or due to sampling or observer error ("false zeros") (Martin et al., 2005). Excess zeroes contribute to overdispersion, but they don't necessarily account for all excess variability (Blasco-Moreno et al., 2019).
```