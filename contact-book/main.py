contacts = []

y = True
while y:



    contact_name = input("Enter the contact name\n")

    try:
        contact_phone = int(input("Enter the phone number\n"))
    except ValueError:
        print("Error: Please enter only digit.")
        # continue
    contact = {
        "name": contact_name,
        "phone": contact_phone,
    }

    contacts.append(contact)
    print("added successfully.")
    print()
    
    while True:
        add_choice = input("Do you want to another contact?\n1. Yes\n2. No\n")
        try:
            add_choice = int(add_choice)
        except ValueError:
            print("Invalid input: Please enter only digit.\n")
            continue
        if add_choice == 1:
            break
        # if add_choice == 2:
        #     return