import json
import pandas as pd
import argparse
import os
import glob

def get_parser():
    parser = argparse.ArgumentParser(description='Add AcquisitionDuration in the JSON metadata for *_T2star.json from CSV file')
    parser.add_argument('--input', help='Path to data-multi-subject')
    parser.add_argument('--input-csv', help='Path to CSV file')
    return parser

def main(argv=None):
    parser = get_parser()
    args = parser.parse_args(argv)
    os.chdir(args.input)
    df = pd.read_csv(args.input_csv)
    rows=[]
    for file in glob.glob(os.path.join(args.input,"*/*/*_T2star.json")):
        subject_name = (os.path.split(file)[1].split('_')[0])
        value_AcquisitionDuration = df[df['Subject'].str.contains(subject_name) == True]['AcquisitionDurationManual'].values[0]
        file_json = open(os.path.join(args.input,file))
        data = json.load(file_json)
        data_to_add = {"AcquisitionDuration": value_AcquisitionDuration}
        data.update(data_to_add)
        with open(os.path.join(args.input,file), 'w') as outfile:
            json.dump(data, outfile, indent=4)

if __name__ == "__main__":
    main()