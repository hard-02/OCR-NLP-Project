from pathlib import Path
from PIL import Image
import pandas as pd

BASE = Path("/Volumes/Hardik/OCR_Dataset")

DATASETS = ["SROIE", "FUNSD", "CORD", "IAM", "Mozhi"]

image_extensions = {".png", ".jpg", ".jpeg", ".webp"}

results = []

print("=" * 60)
print("OCR DATASET AUDIT")
print("=" * 60)

for dataset in DATASETS:

    dataset_dir = BASE / dataset

    if not dataset_dir.exists():
        print(f"\n{dataset}: NOT FOUND")
        continue

    images = [
        p for p in dataset_dir.rglob("*")
        if p.is_file() and p.suffix.lower() in image_extensions
    ]

    print(f"\n{dataset}")
    print("-" * 40)
    print(f"Images: {len(images)}")

    broken = 0
    widths = []
    heights = []

    for i, path in enumerate(images):

        try:
            with Image.open(path) as im:
                im.verify()

            with Image.open(path) as im:
                widths.append(im.width)
                heights.append(im.height)

        except Exception as e:
            broken += 1
            print(f"BROKEN: {path}")

    print(f"Broken: {broken}")

    if widths:
        print(f"Width:  min={min(widths)}, max={max(widths)}")
        print(f"Height: min={min(heights)}, max={max(heights)}")

    results.append({
        "dataset": dataset,
        "images": len(images),
        "broken": broken,
        "min_width": min(widths) if widths else None,
        "max_width": max(widths) if widths else None,
        "min_height": min(heights) if heights else None,
        "max_height": max(heights) if heights else None
    })

df = pd.DataFrame(results)

print("\n" + "=" * 60)
print("SUMMARY")
print("=" * 60)

print(df.to_string(index=False))

df.to_csv(BASE / "dataset_audit.csv", index=False)

print("\nAudit saved to:")
print(BASE / "dataset_audit.csv")
