from tensorflow.keras.optimizers import Adam

def model_compiling():
    input_shape = (299, 299, 3)
    num_classes = 14

    model = create_model(input_shape, num_classes)
    model.compile(optimizer=Adam(learning_rate=0.002), loss='categorical_crossentropy', metrics=['accuracy'])
    model.summary()
    return model
