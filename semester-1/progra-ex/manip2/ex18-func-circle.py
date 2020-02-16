from math import pi

rayon = int(input("Entrez le rayon d'un cercle: "))
global circonference

def calcul_circonference():
    circonference = pi * (rayon * 2)
    print(f"circonference du cercle: {circonference}")

calcul_circonference()
