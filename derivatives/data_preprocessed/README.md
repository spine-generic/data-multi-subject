This folder contains the preprocessed images using [process_data.sh](https://github.com/spine-generic/spine-generic/blob/v2.7/process_data.sh). The preprocessing steps include:

T2w:
    * Resampling to 0.8x0.8x0.8 mm
    * Reorientation to RPI
T1w: 
    * Resampling to 1x1x1 mm
    * Reorientation to RPI
T2star:
    * Reorientation to RPI
    * Root-mean square across 4th dimension (if exists)

MTS (flip-1_mt-on & flip-2_mt-off):
    * Reorientation to RPI

DWI: 
    * Motion correction
    * Avreage across 4th dimension
