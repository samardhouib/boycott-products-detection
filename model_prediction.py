import numpy as np


def model_prediction(train_generator, val_generator):
    predictions = model.predict(val_generator)

    class_indices = train_generator.class_indices
    indices_to_classes = {v: k for k, v in class_indices.items()}
    boycott_classes = ['Cherry Coke', 'Fanta', 'Minute Maid', 'Nestea', 'Sprite', 'aquarius']

    for i, prediction in enumerate(predictions):
        class_index = np.argmax(prediction)
        class_name = indices_to_classes[class_index]
        boycott_status = "boycott" if class_name in boycott_classes else "non boycott"
        print(f"Prediction {i + 1}: Class: {class_name}, Boycott Status: {boycott_status}")