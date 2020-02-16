def update_contact(contacts: dict, name: str, mail: str) -> None:
    contacts[name] = mail
    print(contacts)

contacts =  { "rom": "rom@hello", "jer": "jer@apo"}
update_contact(contacts, "rom", "romain@hello")
