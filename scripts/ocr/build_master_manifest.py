import os
import csv
import json
import ast
import hashlib
from collections import defaultdict

ROOT = "/Volumes/Hardik/OCR_Dataset"
OUTPUT = os.path.join(ROOT, "master_annotations.csv")

DATASETS = ["SROIE", "FUNSD", "CORD", "IAM", "Mozhi"]


def sha256_file(path):
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest()


def full_path(rel_path):
    return os.path.join(ROOT, rel_path)


rows = []


# --------------------------------------------------
# SROIE
# --------------------------------------------------
with open(os.path.join(ROOT, "SROIE", "annotations.csv"),
          encoding="utf-8-sig", newline="") as f:

    reader = csv.DictReader(f)

    for r in reader:
        image = os.path.join("SROIE", r["image"])

        rows.append({
            "image": image,
            "dataset": "SROIE",
            "language": "en",
            "split": "unspecified",
            "text": r["text"]
        })


# --------------------------------------------------
# FUNSD
# --------------------------------------------------
with open(os.path.join(ROOT, "FUNSD", "annotations.csv"),
          encoding="utf-8-sig", newline="") as f:

    reader = csv.DictReader(f)

    for r in reader:
        words = ast.literal_eval(r["words"])
        text = " ".join(words)

        image = os.path.join("FUNSD", r["image"])

        rows.append({
            "image": image,
            "dataset": "FUNSD",
            "language": "en",
            "split": r["split"],
            "text": text
        })


# --------------------------------------------------
# CORD
# --------------------------------------------------
with open(os.path.join(ROOT, "CORD", "annotations.csv"),
          encoding="utf-8-sig", newline="") as f:

    reader = csv.DictReader(f)

    for r in reader:
        gt = json.loads(r["ground_truth"])

        words = []

        for line in gt.get("valid_line", []):
            for word in line.get("words", []):
                text = word.get("text", "")
                if text:
                    words.append(text)

        text = " ".join(words)

        image = os.path.join("CORD", r["image"])

        rows.append({
            "image": image,
            "dataset": "CORD",
            "language": "id",
            "split": r["split"],
            "text": text
        })


# --------------------------------------------------
# IAM
# --------------------------------------------------
with open(os.path.join(ROOT, "IAM", "annotations.csv"),
          encoding="utf-8-sig", newline="") as f:

    reader = csv.DictReader(f)

    for r in reader:
        image = os.path.join("IAM", r["image"])

        rows.append({
            "image": image,
            "dataset": "IAM",
            "language": "en",
            "split": r["split"],
            "text": r["text"]
        })


# --------------------------------------------------
# Mozhi
# --------------------------------------------------
with open(os.path.join(ROOT, "Mozhi", "annotations.csv"),
          encoding="utf-8-sig", newline="") as f:

    reader = csv.DictReader(f)

    for r in reader:
        image = os.path.join("Mozhi", r["image"])

        rows.append({
            "image": image,
            "dataset": "Mozhi",
            "language": r["language"],
            "split": r["split"],
            "text": r["text"]
        })


# --------------------------------------------------
# SHA-256 + duplicate detection
# --------------------------------------------------
hash_to_images = defaultdict(list)

for row in rows:
    path = full_path(row["image"])

    if not os.path.isfile(path):
        raise FileNotFoundError(f"Missing image: {path}")

    digest = sha256_file(path)
    row["sha256"] = digest
    hash_to_images[digest].append(row["image"])


# Mark duplicates while keeping ALL original rows
for row in rows:
    duplicates = hash_to_images[row["sha256"]]

    if len(duplicates) > 1:
        row["is_duplicate"] = "true"
        row["duplicate_of"] = min(duplicates)
    else:
        row["is_duplicate"] = "false"
        row["duplicate_of"] = ""


# --------------------------------------------------
# Write manifest
# --------------------------------------------------
fieldnames = [
    "image",
    "dataset",
    "language",
    "split",
    "text",
    "sha256",
    "is_duplicate",
    "duplicate_of"
]

with open(OUTPUT, "w", encoding="utf-8", newline="") as f:
    writer = csv.DictWriter(f, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(rows)


# --------------------------------------------------
# Verification
# --------------------------------------------------
print()
print("=" * 60)
print("MASTER MANIFEST CREATED")
print("=" * 60)

print(f"Total rows: {len(rows)}")

unique_hashes = len(hash_to_images)
duplicate_groups = sum(
    1 for images in hash_to_images.values()
    if len(images) > 1
)

print(f"Unique images: {unique_hashes}")
print(f"Duplicate groups: {duplicate_groups}")

print()
print("Dataset counts:")

counts = defaultdict(int)

for row in rows:
    counts[row["dataset"]] += 1

for dataset in DATASETS:
    print(f"  {dataset:8s}: {counts[dataset]}")

print()
print(f"Saved to:")
print(OUTPUT)
print("=" * 60)
