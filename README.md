# Spine Generic Public Database (Multi-Subject)

## About this dataset

This dataset was acquired using the [spine-generic protocol](http://spinalcordmri.org/protocols)
on multiple subjects, multiple sites and multiple MRI vendors and models. The list of subjects
is available in [participants.tsv](./participants.tsv).

This dataset follows the [BIDS](https://bids.neuroimaging.io/) convention.
The contributors have the necessary ethics & permissions to share the data publicly.

The dataset does not include any identifiable personal health information, including names,
zip codes, dates of birth, facial features on structural scans.

The processing pipeline to analyze this dataset is available in the [spine-generic repository](https://github.com/sct-pipeline/spine-generic).

## Download

To download the latest version of this dataset, you have two options:

### Download zip package (recommended)

If you are only planning on using the dataset for processing, you can download the latest version as a zip package:

~~~
curl -o spinegeneric.zip -L https://github.com/spine-generic/data-multi-subject/archive/master.zip
unzip spinegeneric.zip
~~~

### Clone the repository (slower)

If you are planning on contributing to this repository (e.g. uploading manual segmentations/labels), you need to clone this repository:
~~~
git clone https://github.com/spine-generic/data-multi-subject.git
~~~

## Analysis

The instructions to process this dataset are available in the [spine-generic documentation](https://spine-generic.readthedocs.io/en/latest/documentation.html#analysis-pipeline).

## Contributing

If you wish to contribute to this dataset by adding new images and/or manual ground truths (e.g., spinal cord segmentations, disc labels, etc.), please fork this repository and submit a pull request. Thank you for your contribution 🎉 
