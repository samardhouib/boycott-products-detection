def main():
    initial_path = '/kaggle/input/aaaaaaaa/pfa'
    data_preprocessing(initial_path)
    generators = data_generation()
    model = model_compiling()
    train_model(model, generators["train_generator"], generators["val_generator"])
    model_prediction(model, generators["val_generator"])

if __name__ == "__main__":
    main()
