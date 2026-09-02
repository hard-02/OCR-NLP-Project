# OCR-NLP Project

An end-to-end NLP project for document OCR, long-document summarization, and multilingual translation.

## Project Pipeline

Document / PDF
      ↓
     OCR
      ↓
Extracted Text
      ↓
Text Preprocessing
      ↓
Long-Document Summarization
      ↓
Hindi / Marathi Translation

## Project Components

### OCR

The OCR component uses:

- SROIE
- FUNSD
- CORD
- IAM
- Mozhi (Hindi + Marathi)

The final OCR dataset contains **14,541 unique images** after duplicate-image filtering.

The final dataset manifests are located in:

data/manifests/

- final_train.csv
- final_validation.csv
- final_test.csv
- master_annotations.csv
- dataset_audit.csv

The actual OCR images are not stored in this repository.

### ArXiv Summarization

The summarization component uses the ArXiv summarization dataset.

Current experiments include:

- Dataset exploration
- TextRank baseline
- Transformer baseline
- LED (Longformer Encoder-Decoder) baseline

The large ArXiv datasets are kept outside the Git repository.

## Repository Structure

OCR-NLP-Project/

├── data/
│   └── manifests/
├── docs/
├── models/
├── notebooks/
│   ├── arxiv/
│   └── ocr/
├── outputs/
├── scripts/
│   └── ocr/
├── .gitignore
├── README.md
└── requirements.txt

## Notebooks

### ArXiv

- 01_dataset_exploration.ipynb
- 02_baseline_textrank.ipynb
- 03_transformer_baseline.ipynb
- 04_led_baseline.ipynb

### OCR

- 01_dataset_audit.ipynb

## OCR Dataset Scripts

Located in scripts/ocr/:

- audit_dataset.py
- build_master_manifest.py
- export_cord.py
- export_funsd.py
- export_iam.py
- export_mozhi.py

## Models

Large model weights and checkpoints are intentionally excluded from Git.

The locally stored LED model is approximately 3.4 GB and is not included in this repository.

## Data and Large Files

The following are intentionally kept outside GitHub:

- OCR image datasets
- ArXiv datasets
- Hugging Face caches
- Model weights
- Training checkpoints
- Generated outputs

The repository contains the code, notebooks, manifests, and documentation needed to reproduce the project workflow.

## Current Status

### Completed

- [x] ArXiv dataset preparation
- [x] ArXiv dataset exploration
- [x] TextRank baseline
- [x] Transformer baseline
- [x] LED baseline
- [x] OCR dataset collection
- [x] OCR dataset auditing
- [x] Duplicate-image detection
- [x] OCR train/validation/test manifests
- [x] Cross-split duplicate leakage check

### Planned

- [ ] OCR model training
- [ ] OCR evaluation
- [ ] Long-document summarization training/evaluation
- [ ] Hindi/Marathi translation
- [ ] End-to-end document processing pipeline
- [ ] Final system evaluation

## Reproducibility

The repository contains the code, notebooks, manifests, and documentation needed to reproduce the project workflow.

Large datasets, model weights, caches, and generated artifacts are intentionally kept outside Git.