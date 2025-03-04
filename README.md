# Spine Generic Public Database (Multi-Subject)
[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.4299140.svg)](https://doi.org/10.5281/zenodo.4299140)
[![BIDS Validator](https://github.com/spine-generic/data-multi-subject/workflows/BIDS%20Validator/badge.svg)](https://github.com/spine-generic/data-multi-subject/actions?query=workflow%3A%22Dataset+Validator%22)

## About this dataset

This dataset was acquired using the [spine-generic protocol](http://spinalcordmri.org/protocols)
on multiple subjects, multiple sites and multiple MRI vendors and models. The list of subjects
is available in [participants.tsv](./participants.tsv).

This dataset follows the [BIDS](https://bids.neuroimaging.io/) convention.
The contributors have the necessary ethics & permissions to share the data publicly.

The dataset does not include any identifiable personal health information, including names,
zip codes, dates of birth, facial features on structural scans.

The entire dataset is about **26GB**.

## Download

We are using a tool to manage large datasets called `git-annex`. To download this dataset, you need to have `git` installed, and also [install `git-annex`](https://github.com/neuropoly/data-management/blob/master/git-annex.md#installation)

> ⚠️  Make sure you have at least **version 8** by running:
>
> ```
> git annex version | head -n 1
> # the answer should show something like: git-annex version: 8.20200330
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

If you with to update an already-cloned repository, run:

```
git pull && git annex get .
```

See more at [the official documentation](https://git-annex.branchable.com/walkthrough/) and take note of our [in-lab troubleshooting](https://github.com/neuropoly/data-management/blob/master/git-annex.md).

## Working from a forked repository

> ⚠️ For advanced users only. Normally the instructions under [Download](#Download) should be enough.

If you have forked this repository on Github (so that you have a copy `your-user-name/data-multi-subject` of `spine-generic/data-multi-subject`), you will need to take a few extra synchronization steps to get the latest data with `git annex get`. Otherwise, you may get an error message like:
```
get some-file-name.nii.gz (not available)
  No other repository is known to contain the file.

  (Note that these git remotes have annex-ignore set: origin)
failed
```

1. In your local clone of `your-user-name/data-multi-subject`, make sure that `spine-generic/data-multi-subject` is also configured as a remote:
   ```
   git remote -v
   # the answer should show both your-user-name/data-multi-subject.git (probably named "origin")
   # and spine-generic/data-multi-subject (probably named "upstream")
   ```

   If `spine-generic/data-multi-subject` is missing, you can add it with:
   ```
   git remote add upstream https://github.com/spine-generic/data-multi-subject.git
   git config remote.upstream.annex-readonly true
   ```

2. Then, to update your local clone, make sure to fetch the `git-annex` branch from `spine-generic/data-multi-subject` before running `git annex get`:
   ```
   git fetch upstream +refs/heads/git-annex:refs/remotes/upstream/git-annex
   git pull && git annex get .
   ```

## Analysis

The instructions to process this dataset are available in the [spine-generic documentation](https://spine-generic.readthedocs.io/en/latest/analysis-pipeline.html).

## Help

If you have problems downloading the dataset, please post an [issue](https://github.com/spine-generic/data-multi-subject/issues). Document your steps as much as possible and copy/paste the content of your Terminal.

## Contributing

If you wish to contribute to this dataset please see [the wiki](https://github.com/spine-generic/spine-generic/wiki/git-annex). Thank you for your contribution 🎉 
