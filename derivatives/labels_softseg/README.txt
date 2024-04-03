The derivatives labels_softseg include soft segmentations (_softseg) of the spinal cord. Softsegs were generated artificially by averaging binary segmentations of multiple contrasts using [process_data.sh](https://github.com/sct-pipeline/contrast-agnostic-softseg-spinalcord/blob/v2.2/processing_spine_generic/process_data.sh).

Main processing steps include:

- Spinal cord segmentation on 6 contrasts (T1w, T2w, T2star, flip-1_mt-on_MTS, flip-2_mt-off and rec-average_dwi)
- Aligning the images with T2w
- Averaging of the segmentations according to each FOV
- Bringing back the segmentations to the original space

All problematic registrations or if a contrast was missing were excluded and the pipeline was run again so the softsegs only include good registrations.
Excluded subjects are listed here: [exclude.yml](https://github.com/sct-pipeline/contrast-agnostic-softseg-spinalcord/blob/v2.2/exclude.yml)
