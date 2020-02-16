nb_batiments = int(input("Nombre de bâtiments à construire: "))
ressources_neccessaires = int(input("Nombre de ressources nécessaires: "))
ressources_disponibles = int(input("Nombre de ressources disponibles: "))

nb_batiment_valide = nb_batiments  <=15 and nb_batiments > 1
ressources_insuffisantes = ressources_neccessaires < ressources_disponibles
peut_construire = nb_batiment_valide == ressources_insuffisantes

print(peut_construire)
