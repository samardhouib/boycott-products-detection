from data_preprocessing import data_preprocessing
from data_generation import data_generation
from model_creation import create_model
from model_compiling import model_compiling
from train_model import train_model
from model_prediction import model_prediction

if _name_ == "_main_":
    initial_path = '/kaggle/input/aaaaaaaa/pfa'

    # Data Preprocessing
    data_preprocessing(initial_path)

    # Data Generation
    generators = data_generation()

    # Create Model
    input_shape = (299, 299, 3)  # Exemple de forme d'entrée
    num_classes = 14  # Exemple de nombre de classes
    model = create_model(input_shape, num_classes)

    # Model Compiling
    model_compiling(model)

    # Train 
    train_model(model, generators["train_generator"], generators["val_generator"])

    # Model Prediction
    model_prediction(generators["train_generator"], generators["val_generator"])

