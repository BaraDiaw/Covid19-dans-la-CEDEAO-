# -*- coding: utf-8 -*-
"""
Created on Fri Mar 20 02:17:34 2020

@author: T!t@n BD
"""

#import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

#Récupération du tableau
tab5 = pd.read_excel("exo5.xlsx")
dtfr5 = pd.DataFrame(tab5)


"""
#Création du dataframe
tab5 = {"Numéro de l'individu":["1", "2", "3", "4", "5"],
        "X" : [3, 2, 1, 4, 5],
        "Y" : [6, 4, 5, 9, 11]
        }
data = pd.DataFrame(tab5)"""

print(dtfr5)
#print(data.describe())


print("\n La moyenne de X est : ", dtfr5["X"].mean())#moyenne de X
print("\n La moyenne de Y est : ", dtfr5["Y"].mean())#moyenne de Y
print("\n La variance de X est : ", dtfr5["X"].var())#variance de X
print("\n La variance de Y est : ", dtfr5["Y"].var())#variance de Y

#covariance et interpétations
covariance = dtfr5.X.cov(dtfr5.Y)
print("\n La cavariance entre X et Y est : ", covariance)
if covariance > 0 :
    print("\n CONCLUSION : X et y évoluent dans le même sens.")
elif covariance < 0:
    print("\n CONCLUSION : X et y évoluent dans le sens contraire.")

#coeff de corrélation et interpétations
correlation = dtfr5.X.corr(dtfr5.Y)
print("\n Le coefficient de corrélation de X et de Y est : ", correlation)
if correlation == 1 :
    print("\n CONCLUSION : Il existe une relation affine entre X et Y.")
elif correlation > 0.8 :
    print("\n CONCLUSION : X et Y sont fortement corrélés.")

#Graphique
plt.scatter(x = dtfr5["X"], y = dtfr5["Y"], color = "blue")
plt.title("Degré de dépendance linéaire entre X et Y", color = "blue", size = 14)
plt.xlabel("Durée en mois (X)", color = "orange", size = 12)
plt.ylabel("Nombre de kilos perdus (Y)", color = "orange", size = 12)
plt.show()
        

