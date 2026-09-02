# Data

This directory contains dataset manifests used by the project.

## OCR Dataset

The OCR datasets are stored outside this repository because of their size and dataset redistribution/licensing considerations.

The OCR datasets used in this project are:

- SROIE
- FUNSD
- CORD
- IAM
- Mozhi (Hindi + Marathi)

The final OCR dataset contains:

- 14,541 unique images
- 9,808 training samples
- 1,373 validation samples
- 3,360 test samples

## Manifests

The `manifests/` directory contains:

- `master_annotations.csv` — master OCR dataset metadata
- `final_train.csv` — training split
- `final_validation.csv` — validation split
- `final_test.csv` — test split
- `dataset_audit.csv` — dataset audit results

The manifests contain references and metadata for the external OCR images.

## ArXiv Dataset

The ArXiv datasets are also stored outside this repository.

Large datasets are intentionally excluded from GitHub.

## Reproducing the Dataset

To reproduce the OCR dataset manifests, use the scripts in:

`scripts/ocr/`

The original datasets must be obtained separately and placed in the appropriate local directories.