from utilities.save_contact import save_contact

def delete_contact(contacts):
    serial = 1 
    if not contacts:
        print("Not contact found.")
        return
    print("all contacts".upper().center(30, "="))
    for delete_contact in contacts:
        print(f"{serial}. {delete_contact['Contact-Name']} - {delete_contact['Contact-Phone']}")
        serial += 1
    item_selected = input("Choose the contact number to delete\n")
    if not item_selected.isdigit():
        print("Invalid input: Only digits are allowed.")
        return
    item_selected = int(item_selected)
    item_selected_index = item_selected -1
    if item_selected_index < 0 or item_selected_index >= len(contacts):
        print("Invalid input: Choose from the list of contacts.")
        return
    item_deleted = contacts.pop(item_selected_index)
    save_contact(contacts)
    print(f"\033[31m{item_deleted["Contact-Name"]}: deleted successfully!\033[0m")
