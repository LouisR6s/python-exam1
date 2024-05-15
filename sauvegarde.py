import os
import shutil
import json
from datetime import datetime

def load_config(config_path):
    try:
        with open(config_path, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        print(f"Le fichier de configuration {config_path} n'existe pas.")
        return None
    except json.JSONDecodeError:
        print(f"Le fichier de configuration {config_path} n'est pas un fichier JSON valide.")
        return None

def backup_path(src_path, dest_dir):
    if not os.path.exists(src_path):
        print(f"Le chemin {src_path} n'existe pas.")
        return
    
    try:
        if os.path.isfile(src_path):
            shutil.copy2(src_path, dest_dir)
            print(f"Fichier {src_path} sauvegardé dans {dest_dir}.")
        elif os.path.isdir(src_path):
            dest_path = os.path.join(dest_dir, os.path.basename(src_path))
            if os.path.exists(dest_path):
                dest_path += f"_{datetime.now().strftime('%Y%m%d%H%M%S')}"
            shutil.copytree(src_path, dest_path)
            print(f"Répertoire {src_path} sauvegardé dans {dest_dir}.")
    except PermissionError:
        print(f"Permission refusée pour accéder à {src_path}.")
    except Exception as e:
        print(f"Erreur lors de la sauvegarde de {src_path}: {e}")
