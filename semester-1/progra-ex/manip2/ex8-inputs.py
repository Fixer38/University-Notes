commande = input("Entrez une commande (O, X, F, P)")

if commande == "O":
    nom_fichier = input("Entrez le nom du fichier à ouvrir: ")
    print(f"Ouverture du fichier {nom_fichier}")

elif commande == "X":
    confirm = input("Etes vous sur de vouloir quitter? [y/n]: ")
    if confirm == "y":
        print("Sortie du programme")

elif commande == "F":
    confirm = input("Etes vous sur de vouloir fermer le fichier? [y/n]: ")
    if confirm == "y":
        print("Fermeture du fichier")

elif commande == "P":
    nb_impression = int(input("Entrez le nombre d'impressions à effectuer: "))
    print(f"Les {nb_impression} impressions sont en cours")

else:
    print("commande non valide")

