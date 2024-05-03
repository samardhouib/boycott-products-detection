import numpy as np
from tensorflow.keras.preprocessing.image import ImageDataGenerator

def data_generation():
    img_height = 299
    img_width = 299
    batch_size = 32

    train_datagen = ImageDataGenerator(
        rescale=1 / 255.,
        rotation_range=40,
        width_shift_range=0.2,
        height_shift_range=0.2,
        shear_range=0.2,
        zoom_range=0.2,
        horizontal_flip=True,
        fill_mode='nearest'
    )

    val_datagen = ImageDataGenerator(rescale=1 / 255.)

    train_generator = train_datagen.flow_from_directory(
        'train',
        target_size=(img_height, img_width),
        batch_size=batch_size,
        class_mode='categorical',
        color_mode='rgb'
    )

    val_generator = val_datagen.flow_from_directory(
        'val',
        target_size=(img_height, img_width),
        batch_size=batch_size,
        class_mode='categorical',
        color_mode='rgb'
    )
    return {"val_generator": val_generator, "train_generator": train_generator}
