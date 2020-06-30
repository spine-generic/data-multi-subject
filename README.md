# Spinal Cord MRI Public Database

## Context

For many years, spinal cord MRI has been a nightmare for most neuro-imagers, mostly due to the technical difficulties related to the requirement for high resolution and the presence of motion and susceptibility artifacts. Thankfully though, researchers have been developing methods to overcome these challenges, including more sensitive coil arrays and advanced pulse sequences to mitigate motion and susceptibility artifacts, allowing researchers to acquire high quality spinal cord data with strong potential for becoming relevant biomarkers. The downside of these improvements however, is that it can be overwhelming for researchers with insufficient expertise in MR physics to choose the sequence and parameters adapted to their needs. To address this issue, an initiative has recently been launched by Dr. Cohen-Adad at the [4th Spinal Cord MRI workshop](http://www.spinalcordmri.org/2017/04/28/workshop.html), whose goal was to bring together all spinal cord imaging experts and come up with a consensus acquisition protocol. What remains to be done is finalize this protocol and evaluate its reproducibility across different vendors to provide researchers with normative values and variability indices, allowing them to conduct power analyses before engaging into SC studies.

## Goal

The main objectives of this proposal are:
1. Optimize the current state-of-the art protocol,
2. Quantify the intra/inter-site and intra/inter-vendor variability of relevant qMRI metrics across the three main vendors (GE, Philips, Siemens) and
3. Disseminate these protocols/SOPs and publish a white paper.

## Protocol

The recommended protocol uses product sequences. However, some old software might not have all up-to-date product sequences, and there could exist research sequences which are equivalent. When applicable, this information will be mentioned in the present document. To harmonize the naming of sequences we followed the BIDS recommendation, i.e.:

* T1w: IR-FSPGR/BRAVO (GE), 3D TFE (Philips), MPRAGE (Siemens)
* T2w: CUBE (GE), VISTA (Philips), SPACE (Siemens)
* DWI: FOCUS (GE), Zoom Diffusion (Philips), ep2d_diff ZOOMit (Siemens)
* GRE-MT1: SPGR (GE), FFE (Philips), GRE (Siemens)
* GRE-MT0: SPGR (GE), FFE (Philips), GRE (Siemens)
* GRE-T1w: SPGR (GE), FFE (Philips), GRE (Siemens)
* GRE-ME: MERGE (GE), mFFE (Philips), GRE (Siemens)

N.B. All importable files are already available for the three vendors (not just the pdf), and if cross-compatibility is broken between models, each file should be there (e.g., VB: .edx vs. VD/VE: .exar for Siemens). Parameters should not be manually copied, to avoid human mistakes. If you cannot import the protocol from the already-available files, please let me know.

## Data

Two open access multi-site datasets acquired with the proposed protocol are available:

* Single-subject, male, healthy, 38 y.o., scanned at multiple sites.
* Multi-subjects, 20-40 y.o., balanced male/female. Subjects are different across sites.

## Ethical consideration and licensing

Each contributor has any necessary ethics / permissions to share the data publicly.
The dataset does not include any identifiable personal health information (including names, zip codes, dates of birth, acquisition dates, facial features on structural scans etc.).
Each contributor agrees that the dataset will become publicly available under an MIT license.

## Would you like to contribute?

If you would like to participate in this repository database, please contact [Julien Cohen-Adad](https://www.neuro.polymtl.ca/people/julien_cohenadad).

## Processing scripts

We provide a processing pipeline to analyze the dataset. For more information, please go to the [Github page](https://github.com/sct-pipeline/spine-generic#analysis-pipeline) of the project.

## Maintaining this repository

This section is for internal use and describes the procedure for creating new
releases of the database and making sure it is synced with the local server at
NeuroPoly Lab.

To push changes:
- Make sure local repository is synced with the latest version online.
- Modify/Add/Delete files in the local repository.
- Update file CHANGES
- Upload to openneuro
- At this stage, the status is "draft". Examine the log to assess that only the
files that were supposed to change (or added) have indeed changed. Archive the log
file.
- Once validated, create a snapshot.
- Update local repository to latest version online.
