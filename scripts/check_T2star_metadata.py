import glob
import os
import json
import argparse
import pandas as pd

def get_parser():
    parser = argparse.ArgumentParser(description='Check if AcquisitionDuration, RepetitionTime, VolumeTiming, '
                                                 'SliceTiming are available in the JSON metadata for *_T2star.json ')
    parser.add_argument('--input', help='Path to data-multi-subject')
    parser.add_argument('--output', help='CSV output file.')
    return parser

def fetch_acquisition_duration(fname_json):
    """
    Fetch the value of AcquisitionDuration in the JSON file of the same basename as fname_nifti
    Return: float: Acquisition duration in seconds
    """
    # Open JSON file
    with open(fname_json) as f:
        dict_json = json.load(f)
        if 'AcquisitionDuration' in dict_json:
            return float(dict_json['AcquisitionDuration'])
        else:
            raise ReferenceError

def fetch_slice_timing(fname_json):
    """
    Fetch the value of SliceTiming in the JSON file of the same basename as fname_nifti
    Return: float: SliceTiming in seconds
    """
    # Open JSON file
    with open(fname_json) as f:
        dict_json = json.load(f)
        if 'SliceTiming' in dict_json:
            return (dict_json['SliceTiming'])
        else:
            raise ReferenceError

def fetch_volume_timing(fname_json):
    """
    Fetch the value of VolumeTiming in the JSON file of the same basename as fname_nifti
    Return: float: VolumeTiming in seconds
    """
    # Open JSON file
    with open(fname_json) as f:
        dict_json = json.load(f)
        if 'VolumeTiming' in dict_json:
            return (dict_json['VolumeTiming'])
        else:
            raise ReferenceError

def fetch_repetitiontime(fname_json):
    """
    Fetch the value of RepetitionTime in the JSON file of the same basename as fname_nifti
    Return: float: RepetitionTime in seconds
    """
    # Open JSON file
    with open(fname_json) as f:
        dict_json = json.load(f)
        if 'RepetitionTime' in dict_json:
            return (dict_json['RepetitionTime'])
        else:
            raise ReferenceError

def main(argv=None):
    parser = get_parser()
    args = parser.parse_args(argv)
    os.chdir(args.input)
    rows=[]
    for file in glob.glob("./*/*/*_T2star.json"):
        print(file)
        row = []
        row.append((os.path.split(file)[1]).replace("_T2star.json",""))
        try:
            repetitiontime = fetch_repetitiontime(file)
            row.append(repetitiontime)
        except ReferenceError:
            print("Field 'RepetitionTime' was not found in the JSON sidecar.")
            row.append("N")
        try:
            acq_duration = fetch_acquisition_duration(file)
            row.append(acq_duration)
        except ReferenceError:
            print("Field 'AcquisitionDuration' was not found in the JSON sidecar.")
            row.append("N")
        try:
            rep_timing = fetch_volume_timing(file)
            row.append(rep_timing)
        except ReferenceError:
            print("Field 'VolumeTiming' was not found in the JSON sidecar.")
            row.append("N")
        try:
            slice_timing = fetch_slice_timing(file)
            row.append(slice_timing)
        except ReferenceError:
            print("Field 'SliceTiming' was not found in the JSON sidecar.")
            row.append("N")
        rows.append(row)

    df = pd.DataFrame(rows, columns=["Subject", "RepetitionTime", "AcquisitionDuration", "VolumeTiming", "SliceTiming"])
    df = df.sort_values(by=['Subject'])
    df.to_csv(args.output, index=False)

if __name__ == "__main__":
    main()