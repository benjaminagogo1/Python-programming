import json

contacts = []

exit_program = False
running = True
while running:


    print("Contact-Book".upper().center(24, "="))
    try:
        chosen_option = int(input("Choose an option.\n\n1. Add contact\n2. View contacts\n3. Edit contacts\n4. Delete contact\n5. Exit\n"))
        
    except ValueError:
        print("Please, enter only 1, 2, or 3.\n")
        continue
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
        print()

        while True:
            add_choice = input("Add another contact?\n1. Yes\n2. No\n")
            try:
                add_choice = int(add_choice)
            except ValueError:
                print("Invalid input: Please enter only digit.\n")
                continue
            if add_choice == 1:
                break
            elif add_choice == 2:
                exit_program = True
                break
            else:
                print("Please enter 1 or 2.\n")
        if exit_program:
            break

    elif chosen_option == 2:
        if not contacts:
            print("No contact found.")
            print()
            continue
        for contact in contacts:
            print(contact)
        text = json.dumps(contacts, indent=2)
        print(text)
    elif chosen_option == 3:
        found = False
        serial = 1
        if not contacts:
            print("No contact found")
            print()
            continue
        print("all contacts".upper().center(31, "="))
        for edit_contact in contacts:
            print(f"{serial}. {edit_contact['Contact-Name']} - {edit_contact['Contact-Phone']}")
            serial += 1
            print()

        contact_number_selected = input("Choose the contact number to edit.\n")

        contact_number_selected = int(contact_number_selected)

        user_index = contact_number_selected - 1
        if user_index < 0 or user_index > len(contacts):
            print("Invalid input: Choose the correct number of the contact you want to edit.")
            continue
        selected_contact = contacts[user_index]
        item = int(input("what do you want to edit?\n1. Contact Name\n2. Phone Number\n"))

        if item == 1:
            new_contact_name = input("Enter the new contact name\n")
            selected_contact["Contact-Name"] = new_contact_name
        if item == 2:
            new_contact_phone = input("Enter the new phone number\n")
            if not new_contact_phone.isdigit():
                print("Invalid input: Only digits are allowed.")
                continue
            selected_contact["Contact-Phone"] = new_contact_phone
    elif chosen_option == 5:
        running = False
        break
    else:
        print("Please enter only the digit: 1, 2, 3, 4 or 5.\n")
        continue