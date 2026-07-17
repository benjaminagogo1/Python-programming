from utilities.save_contact import save_contact

def add_contact(contacts):
    contact_name = input("Enter the contact name\n")
    if contact_name.strip() == "":
        print("Invalid input: Contact name cannot be empty.\n")
        return
    contact_phone = input("Enter the contact phone\n")
    if contact_phone.isdigit() == False:
        print("Phone number must contain only digit.")
        print()
        return
    contact = {
        "Contact-Name": contact_name,
        "Contact-Phone": contact_phone,
    }
    contacts.append(contact)
    save_contact(contacts)
    print()
    print(f"\033[32m{contact['Contact-Name']} added successfully!\033[0m")
    print()