# -*- coding: utf-8 -*-
"""
Created on Fri Mar 27 22:22:19 2020

@author: T!t@n ABD
"""
#Premier graphique :Diagramme en barres
import matplotlib.pyplot as plt
import numpy as np
#Données
pays = ["Bénin", "Burkina", "Cap Vert", "Cote d'Ivoire", "Gambie", "Ghana", "Guinée", "Guinée Bissau", "Libéria", "Mali", "Niger", "Nigéria", "Sénégal", "Sierra Leone", "Togo"]
infectes = [6, 146, 4, 80, 3, 68, 4, 2, 3, 2, 7, 51, 99, 0, 23]

graphe = plt.bar(pays, infectes, color = "orange", width = 0.5)
graphe[1].set_color("red")#colorier Burkina en rouge
plt.xlabel("Pays de la CEDEAO", size = 12, color = "blue")
plt.ylabel("Nombre de personnes infectées", size = 12, color = "blue")
plt.title("Nombre de personnes infectées par le Covid-19 dans la CEDEAO au 26 Mars 2020", color = "black", size = 12)
fig = plt.gcf()#Taille de la figure
fig.set_size_inches(17, 6)
plt.show()

#Deuxième graphique
infectes2 = [6, 146, 4, 80, 3, 68, 4, 2, 3, 2, 7, 51, 99, 0, 23]
dcd = [0, 4, 1, 0, 1, 4, 0, 0, 0, 0, 1, 1, 0, 0, 0]
pays2 = ["Bénin", "Burkina", "Cap Vert", "Cote d'Ivoire", "Gambie", "Ghana", "Guinée", "Guinée Bissau", "Libéria", "Mali", "Niger", "Nigéria", "Sénégal", "Sierra Leone", "Togo"]

inf = plt.bar(pays2, infectes2, color = ["lime" for i in infectes2], width = 0.5)
dc = plt.bar(pays2, dcd, color = ["red" for i in dcd], width = 0.5)
fig = plt.gcf()#Taille de la figure
fig.set_size_inches(17, 12)
plt.xlabel("Pays de la CEDEAO", size = 12, color = "blue")
plt.yticks(np.arange(0,150,5))
plt.grid()
plt.ylabel("Nombre de personnes", size = 12, color = "blue")
plt.title("Situation des cas au Covid-19 dans les pays de la CEDEAO  au 26 Mars 2020", color = "black", size = 12)
plt.legend([inf, dc], ["Personnes infectées", "Personnes décédées"])

plt.show()
