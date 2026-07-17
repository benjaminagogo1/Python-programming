import json

def load_contacts():
    try:
        with open("contact.json", "r") as load_contacts:
            content = load_contacts.read()
            if content.strip() == "":
                print("File content is empty")
                return []
            contacts_saved = json.loads(content)
            return contacts_saved
    except FileNotFoundError:
        return []
    except JSONDecodeError:
        print("Error: contact.json contains inavlid JSON.")
        return []