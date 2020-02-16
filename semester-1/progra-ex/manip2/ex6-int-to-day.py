nb1 = int(input("Entrez un nombre entre 1 et 7: "))
days = ["lundi", "mardi", "mercredi", "jeudi", "vendredi", "samedi", "dimanche"]

if nb1 <= 7 and nb1 > 0:
    print(days[nb1-1])

else:
    print("Le nombre doit être entre 1 et 7")
