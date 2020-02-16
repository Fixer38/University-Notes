def print_mail(contacts: dict, name: str) -> None:
    if name in contacts:
        print(contacts[name])
    else:
        print("Le nom n'est pas dans le dictionnaire")

contacts =  { "rom": "rom@hello", "jer": "jer@apo"}
print_mail(contacts, "rom")
