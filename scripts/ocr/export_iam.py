from datasets import load_dataset
from pathlib import Path
import pandas as pd

print("Loading IAM...")
dataset = load_dataset("Teklia/IAM-line")

output_dir = Path("/Volumes/Hardik/OCR_Dataset/IAM")
image_dir = output_dir / "images"
image_dir.mkdir(parents=True, exist_ok=True)

rows = []

for split in dataset:
    print(f"\nProcessing {split}: {len(dataset[split])} images")

    for i, sample in enumerate(dataset[split]):
        image_path = image_dir / f"{split}_{i:05d}.png"

        sample["image"].save(image_path)

        rows.append({
            "image": f"images/{split}_{i:05d}.png",
            "text": sample["text"],
            "split": split
        })

        if (i + 1) % 250 == 0:
            print(f"  {i + 1}/{len(dataset[split])}")

df = pd.DataFrame(rows)
df.to_csv(output_dir / "annotations.csv", index=False)

print("\n==============================")
print("IAM EXPORT COMPLETE")
print("==============================")
print(f"Images exported: {len(rows)}")
print(f"Location: {output_dir}")
