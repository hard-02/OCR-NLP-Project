from datasets import load_dataset
from pathlib import Path
import pandas as pd

LANGUAGES = {
    "hindi": "Hindi",
    "marathi": "Marathi"
}

TARGETS = {
    "train": 800,
    "validation": 100,
    "test": 100
}

BASE = Path("/Volumes/Hardik/OCR_Dataset/Mozhi")
BASE.mkdir(parents=True, exist_ok=True)

rows = []

for config, language in LANGUAGES.items():

    print(f"\n{'=' * 50}")
    print(f"Processing {language}")
    print("=" * 50)

    dataset = load_dataset(
        "darknight054/indic-mozhi-ocr",
        config
    )

    image_dir = BASE / config / "images"
    image_dir.mkdir(parents=True, exist_ok=True)

    for split, target in TARGETS.items():

        selected = dataset[split].select(range(target))

        print(f"{split}: {target} images")

        for i, sample in enumerate(selected):

            filename = f"{split}_{i:04d}.png"
            image_path = image_dir / filename

            if not image_path.exists():
                sample["image"].save(image_path)

            rows.append({
                "image": f"{config}/images/{filename}",
                "text": sample["text"],
                "language": language,
                "split": split,
                "id": sample["id"]
            })

            if (i + 1) % 100 == 0:
                print(f"  {i + 1}/{target}")

df = pd.DataFrame(rows)
df.to_csv(BASE / "annotations.csv", index=False)

print("\nDONE")
print(df["language"].value_counts())
print(f"Total: {len(df)}")
