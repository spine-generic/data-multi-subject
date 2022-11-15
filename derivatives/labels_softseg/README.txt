The derivatives labels_softseg include soft segmentations (_softseg) of the spinal cord. Softsegs were generated artificially by averaging binary segmentations of multiple contrasts using [process_data.sh](https://github.com/sct-pipeline/contrast-agnostic-softseg-spinalcord/blob/v1.1/process_data.sh).

Main processing steps include:

- Spinal cord segmentation on 6 contrasts
- Aligning the images with T2w
- Averaging of the segmentations according to each FOV
- Bringing back the segmentations to the original space

All problematic registrations were excluded and the pipeline was run again so the softsegs only include good registrations.
7 subjects were excluded:
    - sub-brnoUhb02
    - sub-brnoUhb03
    - sub-brnoUhb07
    - sub-brnoUhb08
    - sub-mountSinai03
    - sub-oxfordFmrib01
    - sub-ucdavis07
