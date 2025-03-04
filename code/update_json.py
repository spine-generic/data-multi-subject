import os
import json
import argparse


def get_parser():
    parser = argparse.ArgumentParser(
        description="Adds spatial reference information to json sidecars." )
    parser.add_argument('-d', 
                        required=True, help='Directory to process JSON files in')
    parser.add_argument('-r', 
                        default='0.8x0.8x0.8', 
                        help='Resampling factor to add to SpatialReference')

    return parser


def create_json_file(nii_gz_files, resampling_factor):
    """Creates a JSON file listing all .nii.gz files and includes the resampling factor.

    Args:
        nii_gz_files (list): A list of paths to .nii.gz files.
    """
    data = {
        #"SpatialReference": {
        #     "Orientation": "RPI",
         #    "Resampling": resampling_factor,
        # },
        "GeneratedBy":[
        {
            "Name": "sct_dmri_moco",
            "Version": "SCT v6.1",
            #"Author": "Paul Bautin",
            #"Date": "2020-07-30 11:57:54",
            "Description": "Mean image across directions after motion correction"
        }]
    }
    for file in nii_gz_files:
        output_path = file.replace('.nii.gz', '.json')
        with open(output_path, 'w', encoding='utf-8') as file:
            json.dump(data, file, indent=4)


def add_spatial_reference(file_path, resampling_factor):
    """Adds the SpatialReference field to a JSON file.

    Args:
        file_path (str): The path to the JSON file.
    """
    with open(file_path, 'r+', encoding='utf-8') as file:
        # Load the existing data
        data = json.load(file)

        # Add the "SpatialReference" field
        data["SpatialReference"] = {
           "Resampling": resampling_factor,
            "Reorientation": "RPI",
            "Other": "root-mean square across 4th dimension (if it exists)"
        }

        # Reset file pointer to the beginning and truncate the file
        file.seek(0)
        file.truncate()

        # Write the modified data back to the file
        json.dump(data, file, indent=4)


def find_nii_gz_files(directory):
    """Finds all .nii.gz files in a directory and its subdirectories.

    Args:
        directory (str): The root directory to start the search from.

    Returns:
        list: A list of paths to the .nii.gz files found.
    """
    nii_gz_files = []
    for root, _, files in os.walk(directory):
        for file in files:
            if ('rec-average_dwi.nii.gz' in file):
                nii_gz_files.append(os.path.join(root, file))
    
    return nii_gz_files


def process_directory(directory, resampling_factor):
    """Recursively processes directories to find and update JSON files.

    Args:
        directory (str): The root directory to start the search from.
    """
    for root, _, files in os.walk(directory):
        for file in files:
            if ('T2w' in file) and ('.json' in file):
                file_path = os.path.join(root, file)
                add_spatial_reference(file_path, resampling_factor)
                print(f"Updated {file_path}")

def main():
    parser = get_parser()
    args = parser.parse_args()
    #process_directory(args.d, args.r)
    nii_gz_files = find_nii_gz_files(args.d)
    create_json_file(nii_gz_files, args.r)

if __name__ == "__main__":
    main()