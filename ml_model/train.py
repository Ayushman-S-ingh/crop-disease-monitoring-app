import os
import tensorflow as tf
from tensorflow.keras.preprocessing.image import ImageDataGenerator

# Paths
BASE_DIR = "ml_model/dataset"
TRAIN_DIR = os.path.join(BASE_DIR, "train")
VAL_DIR = os.path.join(BASE_DIR, "validation")

IMG_SIZE = (224, 224)
BATCH_SIZE = 32

def main():
    print("Initializing data preprocessing pipeline...")

    # Training Data Generator with Augmentation
    train_datagen = ImageDataGenerator(
        rescale=1.0 / 255,
        rotation_range=20,
        zoom_range=0.2,
        shear_range=0.2,
        horizontal_flip=True,
        fill_mode="nearest"
    )

    # Validation Data Generator (NO augmentation)
    val_datagen = ImageDataGenerator(rescale=1.0 / 255)

    train_generator = train_datagen.flow_from_directory(
        TRAIN_DIR,
        target_size=IMG_SIZE,
        batch_size=BATCH_SIZE,
        class_mode="categorical"
    )

    val_generator = val_datagen.flow_from_directory(
        VAL_DIR,
        target_size=IMG_SIZE,
        batch_size=BATCH_SIZE,
        class_mode="categorical"
    )

    print("\nData preprocessing setup complete.")
    print(f"Found {train_generator.samples} training images.")
    print(f"Found {val_generator.samples} validation images.")
    print(f"Number of classes: {len(train_generator.class_indices)}")

if __name__ == "__main__":
    main()
