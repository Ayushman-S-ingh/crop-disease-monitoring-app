import os
import random
import shutil

# Paths
BASE_DIR = "ml_model/dataset"
SOURCE_DIR = os.path.join(BASE_DIR, "PlantVillage")
TRAIN_DIR = os.path.join(BASE_DIR, "train")
VAL_DIR = os.path.join(BASE_DIR, "validation")

SPLIT_RATIO = 0.8  # 80% train, 20% validation


def create_dir(path):
    if not os.path.exists(path):
        os.makedirs(path)


def split_dataset():
    print("Starting dataset split...")

    for class_name in os.listdir(SOURCE_DIR):
        class_path = os.path.join(SOURCE_DIR, class_name)

        if not os.path.isdir(class_path):
            continue

        images = os.listdir(class_path)
        random.shuffle(images)

        split_index = int(len(images) * SPLIT_RATIO)

        train_images = images[:split_index]
        val_images = images[split_index:]

        # Create class folders
        create_dir(os.path.join(TRAIN_DIR, class_name))
        create_dir(os.path.join(VAL_DIR, class_name))

        # Copy training images
        for img in train_images:
            src = os.path.join(class_path, img)
            dst = os.path.join(TRAIN_DIR, class_name, img)
            shutil.copy2(src, dst)

        # Copy validation images
        for img in val_images:
            src = os.path.join(class_path, img)
            dst = os.path.join(VAL_DIR, class_name, img)
            shutil.copy2(src, dst)

        print(f"{class_name}: {len(train_images)} train | {len(val_images)} validation")

    print("Dataset split completed.")


if __name__ == "__main__":
    split_dataset()
