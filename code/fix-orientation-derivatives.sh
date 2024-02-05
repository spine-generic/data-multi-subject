#!/bin/bash
#
# Fixes orientation of derivatives labels
#
# Usage:
#   ./process_data.sh <SUBJECT>
#
#
# Authors: Sandrine Bédard
# The following global variables are retrieved from the caller sct_run_batch
# but could be overwritten by uncommenting the lines below:
# PATH_DATA_PROCESSED="~/data_processed"
# PATH_RESULTS="~/results"
# PATH_LOG="~/log"
# PATH_QC="~/qc"

# Uncomment for full verbose
set -x

# Immediately exit if error
set -e -o pipefail
trap "echo Caught Keyboard Interrupt within script. Exiting now.; exit" INT

# Retrieve input params
SUBJECT=$1
# get starting time:
start=`date +%s`

# SCRIPT STARTS HERE
# ==============================================================================
# Display useful info for the log, such as SCT version, RAM and CPU cores available
sct_check_dependencies -short

# Go to folder where data will be copied and processed
cd $PATH_DATA_PROCESSED

# Copy source images
rsync -avzh $PATH_DATA/$SUBJECT .

# Go to anat folder where all structural data are located
cd ${SUBJECT}/anat/

file_t2="${SUBJECT}_T2w"


orient_native=`sct_image -i ${file_t2}.nii.gz -getorient | cut -f18 -d' '`
orient_native=${orient_native:9:5}
echo "Native orientation: $orient_native"



# Copy CSF seg
file_t2_csf="${file_t2}_label-CSF_seg"
rsync -avzh $PATH_DATA/derivatives/labels/${SUBJECT}/anat/${file_t2_csf}.nii.gz ${file_t2_csf}_or.nii.gz
# Set to CSF seg to native orientation
sct_image -i ${file_t2_csf}_or.nii.gz -setorient $orient_native -o ${file_t2_csf}_reorient.nii.gz


# Resample no native resolution:

sct_resample -i ${file_t2_csf}_reorient.nii.gz -ref ${file_t2}.nii.gz -x linear -o ${file_t2_csf}_reorient_r.nii.gz
sct_maths -i ${file_t2_csf}_reorient_r.nii.gz -bin 0.5 -o ${file_t2_csf}_reorient_r_bin.nii.gz

# Create QC report
sct_qc -i ${file_t2}.nii.gz -s ${file_t2_csf}_reorient_r_bin.nii.gz -p sct_deepseg_sc -qc ${PATH_QC} -qc-subject ${SUBJECT}

# Create derivatives:
mkdir -p $PATH_DATA_PROCESSED/derivatives/labels/${SUBJECT}/anat/
rsync -avzh ${file_t2_csf}_reorient_r_bin.nii.gz $PATH_DATA_PROCESSED/derivatives/labels/${SUBJECT}/anat/${file_t2_csf}.nii.gz


# Verify presence of output files and write log file if error
# ------------------------------------------------------------------------------
FILES_TO_CHECK=(
  "$PATH_DATA_PROCESSED/derivatives/labels/${SUBJECT}/anat/${file_t2_csf}.nii.gz"
)
pwd
for file in ${FILES_TO_CHECK[@]}; do
  if [[ ! -e $file ]]; then
    echo "${SUBJECT}/anat/${file} does not exist" >> $PATH_LOG/_error_check_output_files.log
  fi
done

# Display useful info for the log
end=`date +%s`
runtime=$((end-start))
echo
echo "~~~"
echo "SCT version: `sct_version`"
echo "Ran on:      `uname -nsr`"
echo "Duration:    $(($runtime / 3600))hrs $((($runtime / 60) % 60))min $(($runtime % 60))sec"
echo "~~~"
