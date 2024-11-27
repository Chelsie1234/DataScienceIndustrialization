# Utiliser une image Python de base
FROM python:3.10-slim

# Définir le répertoire de travail dans le conteneur
WORKDIR /app

# Copier le script Python et les autres fichiers nécessaires dans le conteneur
COPY weather-classification-TP.py /app/
COPY requirements.txt /app/

# Créer le répertoire cible pour le modèle
RUN mkdir -p /app/data

# Copier le fichier du modèle dans le bon répertoire
COPY ./data/ResNet152V2-Weather-Classification-03.h5 /app/data/ResNet152V2-Weather-Classification-03.h5


# Installer les packages requis depuis requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Créer les répertoires de montage pour les volumes
RUN mkdir -p /app/data /app/output


# Commande par défaut pour exécuter le script Python
CMD ["python", "weather-classification-TP.py"]
