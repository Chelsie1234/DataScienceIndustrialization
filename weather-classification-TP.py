#!/usr/bin/env python
# coding: utf-8

# # **Imports**

# Taken from : https://www.kaggle.com/datasets/utkarshsaxenadn/weather-classification-resnet152v2

# In[5]:


# Common
import keras
import numpy as np
import pandas as pd
from glob import glob
from tqdm import tqdm

# Data
from tensorflow.image import resize
from sklearn.model_selection import StratifiedShuffleSplit
from tensorflow.keras.utils import load_img, img_to_array

# Data Viz
import seaborn as sns
import matplotlib.pyplot as plt

# TL Model
from tensorflow.keras.applications import ResNet50, ResNet50V2, InceptionV3, Xception, ResNet152, ResNet152V2

# Model
from keras import Sequential
from keras.layers import Dense, GlobalAvgPool2D, Dropout
from keras.models import load_model

# Callbacks 
from keras.callbacks import EarlyStopping, ModelCheckpoint

# Model Performance
from sklearn.metrics import classification_report

# Model Viz
from tensorflow.keras.utils import plot_model

#datetime
import os
import datetime

# # Data and utilities

# In[6]:


# Cateories
class_names = {0: 'cloudy', 1: 'foggy', 2: 'rainy', 3: 'shine', 4: 'sunrise'}


# In[7]:


def load_image(path):
    '''
    Takes in path of the image and load it
    '''
    img = resize(img_to_array(load_img(path))/255., (256,256))
    return img


# In[8]:


def show_image(image, title=None):
    '''
    Takes in an Image and plot it with Matplotlib
    '''
    plt.imshow(image)
    plt.title(title)
    plt.axis('off')


# In[9]:


def load_data(img_paths):
    X = np.zeros(shape=(len(img_paths), 256,256,3))

    for i, path in tqdm(enumerate(img_paths), desc="Loading"):
        X[i] = load_image(path)
    
    return X


# # Load images

# In[14]:


image_paths = sorted(glob('./data/*.jpg'))
print(f"Total Number of Images : {len(image_paths)}")


# In[15]:


image_paths[:5]


# In[16]:


images = load_data(image_paths)


# # **Data Viz**

# In[17]:


plt.figure(figsize=(10,10))
for i in range(25):
    
    if i > len(images)-1:
        break
    
    image = images[i]

    plt.subplot(5,5,i+1)
    show_image(image, title=f"Image : {i}")
plt.tight_layout()
plt.show()


# # Prediction with pre-trained ResNet152V2 model

# In[22]:


# Load model
model_v3 = load_model('./data/ResNet152V2-Weather-Classification-03.h5')


# In[23]:


# Make Predictions
preds = np.argmax(model_v3.predict(images), axis=-1)


# # Result

# In[24]:


plt.figure(figsize=(15,20))
for i, im in enumerate(images):

    # Make Prediction
    pred = class_names[list(preds)[i]]
    
    # Show Prediction
    plt.subplot(5,5,i+1)
    show_image(im, title=f"Pred : {pred}")
    
    
plt.tight_layout()
plt.show()


# Créer un répertoire de sortie s'il n'existe pas
output_dir = 'output'
os.makedirs(output_dir, exist_ok=True)


# Créer une liste de tuples (image_name, prediction_label)
results = []
for i, image_path in enumerate(image_paths):
    image_name = os.path.basename(image_path)  # Obtenir le nom de l'image sans le chemin complet
    prediction_label = class_names[preds[i]]  # Utiliser le dictionnaire pour obtenir le label
    results.append((image_name, prediction_label))

#Convertir les résultats en DataFrame pandas pour les sauvegarder en CSV
df_results = pd.DataFrame(results, columns=["image_name", "prediction_label"])

# Générer un nom de fichier avec horodatage
timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
output_file = os.path.join(output_dir, f"predictions_{timestamp}.csv")

# Sauvegarder le DataFrame en CSV
df_results.to_csv(output_file, index=False)

print(f"CSV file saved: {output_file}")