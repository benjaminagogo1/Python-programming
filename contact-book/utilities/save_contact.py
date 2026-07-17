import json

def save_contact(contacts):
    text = json.dumps(contacts, indent=4)
    try:
        with open("contact.json", "w") as saveContact:
            saveContact.write(text)
    except OSError:
        print("Error: unable to save contact to contact.json")
        return