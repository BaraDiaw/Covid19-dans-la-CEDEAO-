# -*- coding: utf-8 -*-
"""
Created on Sat Mar 28 10:15:39 2020

@author: T!t@n ABD
"""

import matplotlib.pyplot as plt
#Diagramme circulaire
pays = [ "Burkina", "Cap Vert", "Gambie", "Ghana", "Niger", "Nigéria",]
dcd = [4, 1, 1, 4, 1, 1 ]
colors = ["red", "blue", "black", "orange", "cyan", "green"]
plt.pie(dcd, labels=pays, colors=colors, shadow=True, startangle=90, autopct = "%1.1f%%")
plt.axis('equal')
plt.title("Pays de la CEDEAO ayant des décés du Covid-19 au 26 Mars 2020")
plt.show()