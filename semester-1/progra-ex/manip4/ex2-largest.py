def is_empty(liste: list) -> bool:
    return len(liste) == 0


def print_max(lst: list) -> None:
    if is_empty(lst):
        print("Erreur, la liste est vide")
    else:
        print(f"Le nombre maximum de la liste est: {max(lst)}")

lst = []
lst2 = [1, 2, 3, 2]
print_max(lst)
print_max(lst2)
