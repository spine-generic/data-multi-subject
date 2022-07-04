The derivatives labels_softseg include soft segmentations (_softseg) of the spinal cord. Softsegs were generated artificially by averaging binary segmentations of multiple contrasts using [process_data.sh](https://github.com/sct-pipeline/contrast-agnostic-softseg-spinalcord/blob/v1.0/process_data.sh).

Main processing steps include:

- Spinal cord segmentation on 6 contrasts
- Aligning the images with T2w
- Averaging of the segmentations according to each FOV
- Bringing back the segmentations to the original space

All problematic registrations were excluded and the pipeline was run again so the softsegs only include good registrations.

We encountered an edge effect when applying the warping field to bring back the segmentations to their native space which was resolved with padding :
(https://github.com/sct-pipeline/contrast-agnostic-softseg-spinalcord/issues/11)
It was not resolved for 35 softsegs. The problematic slices were manually removed for:
 - sub-amu03_T1w.nii.gz
 - sub-balgrist02_acq-MTon_MTS.nii.gz
 - sub-barcelona02_T2w.nii.gz
 - sub-barcelona02_acq-MTon_MTS.nii.gz
 - sub-brnoCeitec01_T1w.nii.gz
 - sub-brnoCeitec03_T1w.nii.gz
 - sub-brnoCeitec06_T1w.nii.gz
 - sub-dresden02_acq-MTon_MTS.nii.gz
 - sub-fslAchieva06_T1w.nii.gz
 - sub-geneva03_T1w.nii.gz
 - sub-geneva05_T1w.nii.gz
 - sub-hamburg03_T1w.nii.gz
 - sub-juntendo750w02_acq-T1w_MTS.nii.gz
 - sub-juntendo750w02_acq-MTon_MTS.nii.gz
 - sub-mgh02_acq-MTon_MTS.nii.gz
 - sub-milan05_T1w.nii.gz
 - sub-mpicbs06_T1w.nii.gz
 - sub-nottwil02_T1w.nii.gz
 - sub-nottwil04_acq-MTon_MTS.nii.gz
 - sub-oxfordFmrib05_T1w.nii.gz
 - sub-oxfordOhba01_T1w.nii.gz
 - sub-pavia05_T1w.nii.gz
 - sub-sherbrooke07_T1w.nii.gz
 - sub-sherbrooke07_T1w.nii.gz
 - sub-stanford05_acq-MTon_MTS.nii.gz
 - sub-tokyo750w07_T1w.nii.gz
 - sub-ubc02_T1w.nii.gz
 - sub-ubc04_acq-MTon_MTS.nii.gz
 - sub-ucdavis04_T1w.nii.gz
 - sub-ucl03_T1w.nii.gz
 - sub-ucl06_acq-MTon_MTS.nii.gz
 - sub-unf02_T1w.nii.gz
 - sub-vallHebron05_acq-MTon_MTS.nii.gz
 - sub-vallHebron06_T2w.nii.gz
 - sub-vuiisAchieva05_T1w.nii.gz
