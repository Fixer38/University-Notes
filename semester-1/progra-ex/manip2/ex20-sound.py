sound = 50

command = input("Entrez +, - ou x: ")

def up_sound():
    global sound
    sound += 1


def down_sound():
    global sound
    sound -= 1


while command != "x":

    if command == "+":
        up_sound()

    elif command == "-":
        down_sound()

    else:
        print("Commande non valide")

    print(sound)
    command = input("Entrez +, - ou x: ")

print("Fin du programme")

