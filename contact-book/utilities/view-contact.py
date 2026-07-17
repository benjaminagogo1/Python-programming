def view_contacts():
    elif chosen_option == 2:
        if not contacts:
            print("No contact found.")
            print()
            continue
        for contact in contacts:
            print(contact)
        text = json.dumps(contacts, indent=2)
        print(text)
