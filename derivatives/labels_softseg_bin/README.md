The derivatives labels_softseg_bin include binarized soft segmentations (desc-softseg_label-SC_seg) of the spinal cord. Softsegs bin were generated artificially by averaging binary segmentations of multiple contrasts using [process_data.sh](https://github.com/sct-pipeline/contrast-agnostic-softseg-spinalcord/blob/v2.2/processing_spine_generic/process_data.sh) followed by binarization.


All problematic registrations or if a contrast was missing were excluded and the pipeline was run again so the softsegs only include good registrations.
Excluded subjects are listed here: [exclude.yml](https://github.com/sct-pipeline/contrast-agnostic-softseg-spinalcord/blob/v2.2/exclude.yml)
