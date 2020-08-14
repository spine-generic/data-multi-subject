# Contributing to data-multi-subject

To submit changes -- new images and/or manual ground truths (e.g., spinal cord segmentations, disc labels, etc.) -- please fork this repository and submit a pull request.
The process is a little bit unusual because of the existence of `git-annex` and Amazon S3 in the mix:

## If you are a member of the lab

1. Fork this repository.
2. Add your fork as a remote:
```
# in your local copy, assuming you already followed the download instructions in README.md
git add yourusername git@github.com:yourusername/data-multi-subject.git
git annex sync yourusername
```
3. Start a branch:
```
git checkout -b your-changes
```
4. Make your changes. Use the usual git commands (`git add -u`, `git add [filename]`, `git rm [filename]`, etc) to apply them.
5. Commit them as usual to git:
```
git commit
```
6. Contact [@jcohenadad](https://github.com/jcohenadad) to get Amazon S3 credentials to the cloud storage used for the NifTi files.
```
export AWS_ACCESS_KEY_ID="..." AWS_SECRET_ACCESS_KEY="..."
```
7. Publish:
```
git annex sync --content amazon
git annex sync yourusername
```
8. Go to https://github.com/yourusername/data-multi-subject and click the Pull Request button.

## If you are an external contributor.

We haven't yet worked out the best way to support this. See: https://github.com/spine-generic/data-multi-subject/issues/3


# Troubleshooting `git-annex`

## For users

#### "a cosmetic problem affecting git status"

Sometimes the `git-annex` filter will glitch. It will give you a warning in these cases, and a suggested solution. It does prevent git from doing most of its operations correctly however, despite `git-annex` calling it "cosmetic".

To fix:

```
git status | sed -n 's/modified://p' | xargs git update-index -q --refresh
```

This doesn't touch file contents, so it should be safe to run anytime.


## For dataset administrators

#### Resetting git-annex

git-annex writes to a lot of places: the `git-annex` branch, .git/annex (including several sqlite databases?), .git/config, and .git/info/attributes. To get rid of it without getting rid of the complete repo, you can use

```
git annex uninit
```

#### Resetting an S3 bucket

To fully delete a S3 bucket, use `aws` (`pip install awscli`). Give it your credentials and run:

```
aws s3 rm s3://$BUCKET --recursive
aws s3api delete-bucket --bucket $BUCKET --region ca-central-1
```

But this is a complete wipe. If you just need to reset it so you can rerun `git annex initremote`, it is enough to do:

```
aws s3 rm s3://data-multi-subject---spine-generic---neuropoly/annex-uuid
```

Hopefully, erasing all the data won't be something we need to do that often, but there it is if we need to.
