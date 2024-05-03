import os
import shutil
import random

def data_preprocessing(initial_path):
    directories = ['train', 'val', 'test']
    subdirectories = ['Cherry Coke', 'Fanta', 'Minute Maid', 'Nestea', 'Sprite', 'aquarius', 'boga', 'irnbru',
                      'j20', 'prime', 'rio', 'barrcola', 'rubicon', 'tango']
    props = [0.7, 0.2, 0.1]

    for directory in directories:
        for subdirectory in subdirectories:
            path = os.path.join(initial_path, subdirectory)
            files = os.listdir(path)
            random.shuffle(files)
            total = len(files)
            train_end = int(total * props[0])
            val_end = train_end + int(total * props[1])
            if directory == 'train':
                new_files = files[:train_end]
            elif directory == 'val':
                new_files = files[train_end:val_end]
            else:
                new_files = files[val_end:]
            new_path = os.path.join(directory, subdirectory)
            os.makedirs(new_path, exist_ok=True)
            for file in new_files:
                old_file_path = os.path.join(path, file)
                new_file_path = os.path.join(new_path, file)
                shutil.copy(old_file_path, new_file_path)
