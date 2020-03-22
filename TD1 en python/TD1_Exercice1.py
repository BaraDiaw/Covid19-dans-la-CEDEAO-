# -*- coding: utf-8 -*-
"""
Created on Fri Mar 20 01:03:10 2020

@author: T!t@n BD
"""

import numpy as np
import matplotlib.pyplot as plt
#import pandas as pd

#print("\n PREMIERE METHODE")
#Données
faces = ["1", "2", "3", "4", "5", "6"]
resultats = [1, 8, 4, 3, 4, 0]

#Calcul de la médiane
print("\n 1°) La médiane de la série est : ", np.median(resultats))

#Graphique en barres
plt.bar(faces, resultats, color = "blue", width = 0.5)
plt.xlabel("Faces du dé", size = 12, color = "orange")
plt.ylabel("Nombre d'apparution des faces", size = 12, color = "orange")
plt.title("Titre: Diagramme en barres ", color = "lime", size = 12)
plt.show()

#Graphique en bâtons
plt.bar(faces, resultats, color = "orange", width = 0.05)
plt.xlabel("Faces du dé", size = 12, color = "blue")
plt.ylabel("Nombre d'apparution des faces", size = 12, color = "blue")
plt.title("Titre: Diagramme en bâtons ", color = "lime", size = 12)
plt.show()

#Interprétation
print("\n 2°) Après observation, le mode de la série est : 2 ")

"""
#Deuxième méthode
print("\n DEUXIEME METHODE")
#Récupération du tableau au format excel
tab = pd.read_excel("exo1.xlsx")
#Affichage du tableau
print(tab)
#Calcul de la médiane
print("La médiane de la série est : ",tab.median())"""