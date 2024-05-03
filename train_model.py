from tensorflow.keras.callbacks
import ((ReduceLROnPlateau, ModelCheckpoint))

def train_model(model, train_generator, val_generator):
    epochs = 200
    batch_size = 32

    train_steps_per_epoch = train_generator.samples // batch_size
    val_steps_per_epoch = val_generator.samples // batch_size

    reduce_lr = ReduceLROnPlateau(monitor='val_loss', factor=0.2, patience=5, min_lr=1e-9)

    checkpoint_path = 'best_model.keras'

    checkpoint = ModelCheckpoint(checkpoint_path,
                                 monitor='val_loss',
                                 verbose=1,
                                 save_best_only=True,
                                 mode='min')

    history = model.fit(train_generator,
                        steps_per_epoch=train_steps_per_epoch,
                        epochs=epochs,
                        validation_data=val_generator,
                        validation_steps=val_steps_per_epoch,
                        callbacks=[reduce_lr, checkpoint])