import os
import csv
import random
import msvcrt

# Demande le chemin du dossier à traiter
folder_path = input("Entrez le chemin du dossier à traiter : ")

# Vérifie que le dossier existe
if not os.path.exists(folder_path):
    print("Le dossier spécifié n'existe pas")
    msvcrt.getch()
    exit()

# Obtient la liste de tous les fichiers .mp3 dans le dossier spécifié
mp3_files = [f for f in os.listdir(folder_path) if f.endswith('.mp3')]

# Vérifie qu'il y a des fichiers mp3 dans le dossier
if not mp3_files:
    print("Le dossier ne contient aucun fichier MP3")
    msvcrt.getch()
    exit()

# Initialise un dictionnaire pour stocker les alias déjà utilisés
used_aliases = {}

# Initialise une liste pour stocker les informations sur chaque fichier traité
files_info = []

# Parcourt la liste des fichiers mp3
for mp3_file in mp3_files:
    # Génère un alias unique pour ce fichier
    alias = None
    while not alias or alias in used_aliases:
        alias = ''.join(random.choice('abcdefghijkmnpqrstuvwxyz23456789') for _ in range(3))
    used_aliases[alias] = mp3_file
    
    # Stocke les informations sur le fichier dans la liste files_info
    files_info.append([mp3_file, alias])
    
    # Renomme le fichier avec son alias
    old_path = os.path.join(folder_path, mp3_file)
    new_path = os.path.join(folder_path, f"{alias}.mp3")
    os.rename(old_path, new_path)

# Exporte les informations sur les fichiers dans un fichier CSV
csv_path = os.path.join(folder_path, "fichiers.csv")
with open(csv_path, mode='w', newline='') as csv_file:
    writer = csv.writer(csv_file, delimiter=',')
    writer.writerows(files_info)

# Affiche un message de confirmation
print(f"Traitement terminé, {len(mp3_files)} fichiers renommés")

# Attend une action clavier pour fermer le programme
print("Appuyez sur une touche pour quitter...")
msvcrt.getch()
