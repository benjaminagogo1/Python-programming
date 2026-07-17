import json

from utilities.add_contact import add_contact
from utilities.view_contacts import view_contacts
from utilities.edit_contact import edit_contact
from utilities.delete_contact import delete_contact
from utilities.load_contacts import load_contacts
from utilities.save_contact import save_contact



def main():
    contacts = load_contacts()

    running = True
    while running:

        print("Contact-Book".upper().center(28, "="))
        chosen_option = (input("Choose an option.\n\n1. Add contact\n2. View contacts\n3. Edit contacts\n4. Delete contact\n5. Exit\n"))

        if not chosen_option.isdigit():
            print("Invalid input: choose the number from the list")
            continue
        chosen_option = int(chosen_option)
        if chosen_option < 1 or chosen_option > 5:
            print("Invalid input: Choose from the menu number provided.")
            continue
        if chosen_option == 1:
            add_contact(contacts)
        if chosen_option == 2:
            view_contacts(contacts)
        if chosen_option == 3:
            edit_contact(contacts)
        if chosen_option == 4:
            delete_contact(contacts)
        if chosen_option == 5:
            running = False
main()