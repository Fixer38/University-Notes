nb_base8 = "0123567"
bloc = ("Air", "minecraft:air", 0)
descriptions = [("Air", "minecraft:air", 0), ("Stone", "minecraft:stone", 1), ("Grass", "minecraft:grass", 3)]

#bloc_deja_defini = bloc_lu in descriptions

semaine = ["Lundi", "Mardi", "Mercredi", "Jeudi", "Vendredi", "Samedi", "Dimanche"]

for day in semaine:
    if day != "Samedi" and day != "Dimanche":
        print(day[0:2])

import math

noms = ["Bodart", "Pirotte", "Smal", "Valentin"]
moyenne = 0
for name in noms:
    moyenne += len(name)
print((math.floor(moyenne / len(noms))))
