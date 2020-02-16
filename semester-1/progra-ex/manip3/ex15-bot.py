import random
import sys
import time

def print_choices():
    print("""
1. Affiche une blague
2. Devinez un nombre
3. Décompte de secondes
4. Quitter le programme""")

def get_user_choice():
    user_choice = int(input("Quel est votre choix: "))
    return user_choice

def print_joke():
    joke1 = "toto et une blague 1"
    joke2 = "toto et une blague 2"
    joke3 = "toto et une blague 3"
    joke_number = random.randint(1,3)

    if joke_number == 1:
        print(joke1)
    elif joke_number == 2:
        print(joke2)
    else:
        print(joke3)

def random_number():
    random_number = random.randint(1, 10)
    user_input = int(input("Entrez un nombre entre 1 et 10: "))

    while user_input != random_number:
        user_input = int(input("Raté, réessayez: "))

    print("Bravo! Le nombre caché était donc: {}".format(random_number))

def timeslip(sec: int):
    for x in range(sec, 0, -1):
        print(x)
        time.sleep(1)

print_choices()
user_choice = get_user_choice()

while user_choice != 4:
    if user_choice == 1:
        print_joke()
    elif user_choice == 2:
        random_number()
    elif user_choice == 3:
        sec = int(input("Rentrez un nombre de secondes: "))
        timeslip(sec)
    else:
        print("Ce choix n'est pas valide")
    print_choices()
    user_choice = get_user_choice()
