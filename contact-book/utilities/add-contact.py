def add_contact():
    if chosen_option == 1:
        contact_name = input("Enter the contact name\n")
        if contact_name.strip() == "":
            print("Invalid input: Contact name cannot be empty.\n")
            continue
        contact_phone = input("Enter the contact phone\n")
        if contact_phone.isdigit() == False:
            print("Phone number must contain only digit.")
            print()
            continue
        contact = {
            "Contact-Name": contact_name,
            "Contact-Phone": contact_phone,
        }
        contacts.append(contact)