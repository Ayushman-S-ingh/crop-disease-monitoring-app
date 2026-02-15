import os
import tensorflow as tf
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from tensorflow.keras.applications import MobileNetV2
from tensorflow.keras import layers, models
from tensorflow.keras.callbacks import (
    EarlyStopping,
    ModelCheckpoint,
    ReduceLROnPlateau,
    CSVLogger,
)

# ========================
# Configuration
# ========================

BASE_DIR = "ml_model/dataset"
TRAIN_DIR = os.path.join(BASE_DIR, "train")
VAL_DIR = os.path.join(BASE_DIR, "validation")

SAVE_DIR = "ml_model/saved_model"
MODEL_PATH = os.path.join(SAVE_DIR, "plant_disease_model.keras")
LOG_PATH = "ml_model/training_log.csv"

IMG_SIZE = (224, 224)
BATCH_SIZE = 32
EPOCHS = 8

os.makedirs(SAVE_DIR, exist_ok=True)

print("\nInitializing data generators...")

# ========================
# Data Generators
# ========================

train_datagen = ImageDataGenerator(
    rescale=1.0 / 255,
    rotation_range=20,
    zoom_range=0.2,
    horizontal_flip=True
)

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

num_classes = train_generator.num_classes
print(f"Number of classes: {num_classes}")

# ========================
# Transfer Learning Model
# ========================

print("\nLoading MobileNetV2 base model...")

base_model = MobileNetV2(
    weights="imagenet",
    include_top=False,
    input_shape=(224, 224, 3)
)

base_model.trainable = False  # Freeze base layers

model = models.Sequential([
    base_model,
    layers.GlobalAveragePooling2D(),
    layers.Dense(128, activation="relu"),
    layers.Dropout(0.5),
    layers.Dense(num_classes, activation="softmax")
])

model.compile(
    optimizer=tf.keras.optimizers.Adam(learning_rate=0.001),
    loss="categorical_crossentropy",
    metrics=["accuracy"]
)

model.summary()

# ========================
# Callbacks
# ========================

callbacks = [
    EarlyStopping(
        monitor="val_loss",
        patience=3,
        restore_best_weights=True
    ),
    ModelCheckpoint(
        MODEL_PATH,
        monitor="val_accuracy",
        save_best_only=True,
        verbose=1
    ),
    ReduceLROnPlateau(
        monitor="val_loss",
        factor=0.2,
        patience=2,
        verbose=1
    ),
    CSVLogger(LOG_PATH)
]

# ========================
# Training
# ========================

print("\nStarting training...")

history = model.fit(
    train_generator,
    validation_data=val_generator,
    epochs=EPOCHS,
    callbacks=callbacks,
    steps_per_epoch=len(train_generator),
    validation_steps=len(val_generator)
)


# ========================
# Evaluation
# ========================

print("\nEvaluating model...")

val_loss, val_accuracy = model.evaluate(val_generator)

print(f"\nFinal Validation Accuracy: {val_accuracy * 100:.2f}%")

# ========================
# Verify Model Loading
# ========================

print("\nVerifying saved model...")

loaded_model = tf.keras.models.load_model(MODEL_PATH)
print("Model loaded successfully.")
