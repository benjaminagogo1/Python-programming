import json

def view_contacts(contacts):
    longest_contact = 0
    serial = 1
    if not contacts:
        print("No contact found.")
        print()
        return
    print("all contacts".upper().center(40, "="))
    for contact_for_header in contacts:
        if len(contact_for_header["Contact-Name"]) > longest_contact:
            longest_contact = len(contact_for_header["Contact-Name"])
    print(f"{"No"}. {"Name":<{longest_contact}}  {"Phone Number":<{longest_contact}}")
    print("----------------------------------------")
    for contact in contacts:
        print(f"{serial}. {contact['Contact-Name']:<{longest_contact}} - {contact['Contact-Phone']:<{longest_contact}}")
        print()
        serial += 1
   