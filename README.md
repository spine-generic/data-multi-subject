# Spine Generic Public Database (Multi-Subject)
[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.4299140.svg)](https://doi.org/10.5281/zenodo.4299140)
[![BIDS Validator](https://github.com/spine-generic/data-multi-subject/workflows/BIDS%20Validator/badge.svg)](https://github.com/spine-generic/data-multi-subject/actions?query=workflow%3A%22BIDS+Validator%22)

## About this dataset

This dataset was acquired using the [spine-generic protocol](http://spinalcordmri.org/protocols)
on multiple subjects, multiple sites and multiple MRI vendors and models. The list of subjects
is available in [participants.tsv](./participants.tsv).

This dataset follows the [BIDS](https://bids.neuroimaging.io/) convention.
The contributors have the necessary ethics & permissions to share the data publicly.

The dataset does not include any identifiable personal health information, including names,
zip codes, dates of birth, facial features on structural scans.

The entire dataset is about **10GB**.

## Download

We are using a tool to manage large datasets called `git-annex`. To download this dataset, you need to have `git` installed, and also [install `git-annex`](https://github.com/neuropoly/data-management/blob/master/git-annex.md#installation)

> ⚠️  Make sure you have at least **version 8** by running:
>
> ```
> $ git annex version | head -n 1
> git-annex version: 8.20200330
> ```


Then this will download the dataset:

```
git clone https://github.com/spine-generic/data-multi-subject && \
cd data-multi-subject && \
git annex init && \
git annex get .
```

You may **substitute** `git annex get` with more specific commands if you are only interested in certain subjects. For example:

```
git annex get sub-nwu01/ sub-nwu03/ sub-nwu04/ sub-oxfordFmrib04/ sub-tokyoSkyra*/
```

See more at [the official documentation](https://git-annex.branchable.com/walkthrough/) and take note of our [in-lab troubleshooting](https://github.com/neuropoly/data-management/blob/master/git-annex.md).

## Analysis

The instructions to process this dataset are available in the [spine-generic documentation](https://spine-generic.readthedocs.io/en/latest/analysis-pipeline.html).

## Contributing

If you wish to contribute to this dataset please see [the wiki](https://github.com/spine-generic/spine-generic/wiki/git-annex). Thank you for your contribution 🎉 
