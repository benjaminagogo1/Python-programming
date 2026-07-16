contacts = []

exit_program = False
running = True
while running:


    print("Contact-Book".upper().center(24, "="))
    try:
        chosen_option = int(input("Choose an option.\n\n1. Add contact\n2. View contact\n3. Exit\n"))
    except ValueError:
        print("Please, enter only 1, 2, or 3.\n")
        continue
    if chosen_option == 1:
        contact_name = input("Enter the contact name\n")
        try:
            contact_phone = int(input("Enter the contact phone\n"))
        except ValueError:
            print("Only digits")
            continue
    elif chosen_option == 3:
        running = False
        break
    else:
        print("Please enter only the digit: 1, 2, or 3\n")
        continue
    contact = {
        "name": contact_name,
        "phone": contact_phone,
    }

    contacts.append(contact)
    print("added successfully.")
    print()
    
    while True:
        add_choice = input("Do you want to add another contact?\n1. Yes\n2. No\n")
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