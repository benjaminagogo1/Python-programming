from utilities.save_contact import save_contact


def edit_contact(contacts):
    found = False
    serial = 1
    if not contacts:
        print("No contact found")
        print()
        return
    print("all contacts".upper().center(31, "="))
    for edit_contact in contacts:
        print(f"{serial}. {edit_contact['Contact-Name']} - {edit_contact['Contact-Phone']}")
        serial += 1
        print()

    contact_number_selected = input("Choose the contact number to edit.\n")
    if not contact_number_selected.isdigit():
        print("Invalid input: Choose the number of the contact to edit.")
        return
    contact_number_selected = int(contact_number_selected)

    user_index = contact_number_selected - 1
    if user_index < 0 or user_index >= len(contacts):
        print("Invalid input: Choose the correct number of the contact you want to edit.")
        return
    selected_contact = contacts[user_index]
    item = int(input("what do you want to edit?\n1. Contact Name\n2. Phone Number\n"))

    if item == 1:
        new_contact_name = input("Enter the new contact name\n")
        selected_contact["Contact-Name"] = new_contact_name
        save_contact(contacts)
        print(f"\033[32m{selected_contact['Contact-Name']}: edited successfully!\033[0m")
    if item == 2:
        new_contact_phone = input("Enter the new phone number\n")
        if not new_contact_phone.isdigit():
            print("Invalid input: Phone number must contain only digit.")
            return
        selected_contact["Contact-Phone"] = new_contact_phone
        save_contact(contacts)
        print(f"\033[32m{selected_contact['Contact-Phone']}: edited successfully!\033[0m")