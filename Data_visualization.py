import os
import cv2
import matplotlib.pyplot as plt
from collections import Counter
import numpy as np
def plot_hist_repartition_classe(data_path):
    # Classes à prédire
    boycott_classes = ['Cherry Coke', 'Fanta', 'Minute Maid', 'Nestea', 'Sprite', 'Aquarius', 'Coca Cola']

    # Dictionnaires pour stocker le nombre d'images par classe
    class_counts = {'Boycott': 0, 'NonBoycott': 0}

    # Parcourir tous les sous-dossiers dans le répertoire data_path
    for root, dirs, _ in os.walk(data_path):
        for subdir in dirs:
            # Ignorer le sous-dossier 'non_boycott'
            if subdir.lower() == 'non boycott':
                continue

            # Obtenir le chemin complet du sous-dossier
            subdir_path = os.path.join(root, subdir)

            # Obtenir le label de la classe (1 ou 0)
            class_label = 1 if subdir in boycott_classes else 0

            # Compter le nombre d'images dans le sous-dossier
            num_files = len(os.listdir(subdir_path))

            # Mettre à jour le dictionnaire correspondant à la classe
            if class_label == 1:
                class_counts['Boycott'] += num_files
            else:
                class_counts['NonBoycott'] += num_files
    class_counts['NonBoycott'] //= 2
    # Créer le tracé à barres pour visualiser la répartition des classes 1 et 0
    plt.figure(figsize=(6, 6))
    plt.bar(list(class_counts.keys()), list(class_counts.values()), color=['blue', 'orange'])
    plt.xlabel('Classes')
    plt.ylabel('Nombre d\'images')
    plt.title('Répartition des Boycott et NonBoycott dans le jeu de données')
    plt.tight_layout()

    # Afficher le tracé
    plt.show()

def plot_nombre_img_par_classe_(data_path):
    # Classes à considérer pour diviser par deux le nombre d'images
    valid_classes = ['Cherry Coke', 'Fanta', 'Minute Maid', 'Nestea', 'Sprite', 'Aquarius', 'Coca Cola']

    # Dictionnaire pour stocker le nombre d'images par label
    label_counts = Counter()

    # Parcourir tous les fichiers dans le répertoire data_path
    for root, dirs, files in os.walk(data_path):
        for file in files:
            # Obtenir le label à partir du nom du dossier parent
            label = os.path.basename(root)

            # Vérifier si le label appartient à la liste spécifiée
            if label in valid_classes:
                # Incrémenter le compteur pour ce label
                label_counts[label] += 1
            else:
                # Diviser par deux le nombre d'images pour les autres classes
                label_counts[label] += 0.5

    # Extraire les labels et les comptes
    labels = list(label_counts.keys())
    counts = list(label_counts.values())

    # Créer le tracé à barres
    plt.figure(figsize=(10, 6))
    bars = plt.bar(labels, counts, color='skyblue')
    plt.xlabel('Labels')
    plt.ylabel("Nombre d'images")
    plt.title("Nombre d'images pour chaque label")
    plt.xticks(rotation=45)
    plt.tight_layout()

    # Ajouter le nombre d'images sur chaque barre
    for bar, count in zip(bars, counts):
        plt.text(bar.get_x() + bar.get_width() / 2, bar.get_height() - 0.5, str(int(count)), ha='center', color='black',
                 fontsize=10)

    # Afficher le tracé
    plt.show()

def plot_pie_nombre_image_nette(data_path):
    # Initialiser les compteurs pour les images nettes et floues
    sharp_images_count = 0
    blurry_images_count = 0

    # Parcourir tous les fichiers dans le répertoire data_path
    for root, dirs, files in os.walk(data_path):
        for file in files:
            # Chemin complet de l'image
            image_path = os.path.join(root, file)

            # Lire l'image en niveaux de gris
            image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)

            # Appliquer un filtre de Canny pour détecter les contours
            edges = cv2.Canny(image, 100, 200)

            # Calculer la surface totale des contours détectés
            total_edge_area = np.sum(edges != 0)

            # Calculer la taille de l'image
            image_size = image.shape[0] * image.shape[1]

            # Calculer le pourcentage de la surface des contours par rapport à la taille de l'image
            edge_area_ratio = total_edge_area / image_size

            # Définir un seuil pour déterminer si l'image est nette ou floue
            threshold = 0.01

            # Mettre à jour les compteurs en fonction du résultat
            if edge_area_ratio > threshold:
                sharp_images_count += 1
            else:
                blurry_images_count += 1

    # Créer un diagramme circulaire pour visualiser les résultats
    labels = ['Nettes', 'Floues']
    sizes = [sharp_images_count, blurry_images_count]
    colors = ['green', 'red']
    explode = (0.1, 0)  # "Exploser" la première tranche (images nettes)

    plt.figure(figsize=(8, 8))
    plt.pie(sizes, explode=explode, labels=labels, colors=colors, autopct='%1.1f%%', shadow=True, startangle=140)
    plt.title('Qualité des images')
    plt.axis('equal')  # Ajuster l'aspect pour être un cercle

    # Afficher le diagramme circulaire
    plt.show()







