def print_all(contacts: dict) -> None:
    for key in contacts:
        print(f"Nom: {key} - email: {contacts[key]}")

contacts =  { "rom": "rom@hello", "jer": "jer@apo"}
print_all(contacts)
