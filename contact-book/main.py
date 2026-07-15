contacts = []



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
for contact in contacts:
    print(f"contact Number: {contact["name"]}")
    print(f"contact phone: {contact["phone"]}")
      


