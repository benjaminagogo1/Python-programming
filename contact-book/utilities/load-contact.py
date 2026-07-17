import json

def load_contact():
    try:
        with open("contact.json", "r") as load_contacts:
            content = load_contacts.read()
            if content.strip() == "":
                print("File content is empty")
                return []
            contacts_saved = json.load_contacts(content)
            return contacts_saved
    except FileNotFoundError:
        return []
    except JSONDecodeError:
        print("Error: contact.json contain inavlid JSON.")
        return []