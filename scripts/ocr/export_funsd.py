from datasets import load_dataset
from pathlib import Path
import pandas as pd
import json

print("Loading FUNSD...")

dataset = load_dataset("nielsr/funsd")

output_dir = Path("/Volumes/Hardik/OCR_Dataset/FUNSD")
image_dir = output_dir / "images"

image_dir.mkdir(parents=True, exist_ok=True)

rows = []

for split in dataset:
    print(f"\nProcessing {split}: {len(dataset[split])} images")

    for i, sample in enumerate(dataset[split]):

        image_path = image_dir / f"{split}_{i:03d}.png"

        sample["image"].save(image_path)

        # Preserve the complete annotations
        rows.append({
            "image": f"images/{split}_{i:03d}.png",
            "id": sample["id"],
            "words": json.dumps(sample["words"], ensure_ascii=False),
            "bboxes": json.dumps(sample["bboxes"]),
            "ner_tags": json.dumps(sample["ner_tags"]),
            "split": split
        })

        if (i + 1) % 25 == 0:
            print(f"  {i + 1}/{len(dataset[split])}")

df = pd.DataFrame(rows)

df.to_csv(
    output_dir / "annotations.csv",
    index=False
)

print("\n==============================")
print("FUNSD EXPORT COMPLETE")
print("==============================")
print(f"Images exported: {len(rows)}")
print(f"Location: {output_dir}")
