expenses = []
print("welcome!".upper().center(30, "="))
print("Welcome to My Expense Tracker.\nA companion that never forgets where your money goes!")
print()


def add_expense():
    expenseName = input("Enter expense name..\n")
    if expenseName.strip() == "":
        print("Expense name cannot be empty.")
        return
    amount = input("Enter expense amount..\n")
    try:
        amount = int(amount)
    except ValueError:
        print("Invalid input: Please enter only digit")
        return
    expenseDate = input("Enter the date {dd/mm/yy}: \n")
    expense = {
        "name": expenseName,
        "amount": amount,
        "date": expenseDate
     }
    expenses.append(expense)
    print(f"\033[32m{expense["name"]} added successfully!\033[0m")



def show_expense():
    if not expenses:
        print("No expense found. Add some expenses to be displayed.")
        return
    total = 0
    number = 1
    longest_name = 0
    print("expenses".upper().center(50, "="))
    print()
    for expense in expenses:
        if len(expense["name"]) > longest_name:
            longest_name = len(expense["name"])
    print(f"{"N0":<{longest_name}} {"Name":<{longest_name}} {"AMount":<{longest_name}} {"Date":<{longest_name}}")
    for expense in expenses:
        print(f"{number}. {expense["name"]:<{longest_name}}| ₦{expense["amount"]:<{longest_name}}| {expense["date"]:<{longest_name}}|")
        number += 1
        total += expense["amount"]
    print()
    print(f"Total expenses: = ₦{total}")
    print()
    want_to_edit = input("Do you want edit?\n1. Yes\n2. No\n")
    try:
        want_to_edit = int(want_to_edit)
    except ValueError:
        print("Error: Please, only enter only digit")
        return
    if want_to_edit == 1:
        edit_displayed_expenses()
    elif want_to_edit == 2:
        return


def edit_displayed_expenses():
    found = False
    item_selected = input("which expense do you want to edit?\n")
    for expense_to_edit in expenses:
        if item_selected == expense_to_edit["name"]:
            found = True
            selected_option = input("what do you want to edit?\n1. Name\n2. Amount\n3. Date\n")
            try:
                selected_option = int(selected_option)
            except ValueError:
                print("Error: Choose between the given options above")
                return

            if selected_option == 1:
                new_name = input("Enter the new name\n")
                expense_to_edit["name"] = new_name
                print(f"\033[32m{expense_to_edit["name"]} updated successfully!\033[0m")

            if selected_option == 2:
                new_amount = input("Enter the new amount\n")
                try:
                    new_amount = int(new_amount)
                except ValueError:
                    print("Error: Please enter only digit")
                    return
                expense_to_edit["amount"] = new_amount
                print(f"\033[32m{expense_to_edit["amount"]} updated successfully!\033[0m")

            if selected_option == 3:
                new_date = input("Enter the new date\n")
                try:
                    new_date = int(new_date)
                except ValueError:
                    return
                    print("Error: enter the correct date format")
                expense_to_edit["date"] = new_date
                print(f"\033[32m{expense_to_edit["date"]} updated successfully!\033[0m")
            break
    if not found:
        print("Expense not found.")


def delete_expense():
    if not expenses:
        print("No expense to delete.")
        return
    number = 1
    print("Choose the expense to delete".upper().center(40, "="))
    for expense in expenses:
        print(f"{number}. {expense["name"]}: ₦{expense["amount"]} |{expense["date"]}")
        number += 1
    choice = input("which expense do you want to delete?\n")
    try:
        choice = int(choice)
    except ValueError:
        print("Invalid input. Please enter only digits.")
        return
    index = choice -1
    if choice < 1 or choice > len(expenses):
        print("Choose from the the list of expenses")
        return
    deleted = expenses.pop(index)
    print(f"\033[31m{deleted["name"]} deleted successfully!\033[0m")
 


running = True
while running:

    print()
    print("menu".upper().center(24, "="))
    userOption = input("Choose....\n1. Add Expense\n2. Show Expense\n3. Delete Expense\n4. Exit\n")

    print()
    if userOption != "1" and userOption != "2" and userOption != "3" and userOption != "4":
        print("You must choose between 1, 2, 3 or 4")
        continue
    option = int(userOption)
    if option == 1:
        add_expense()
    elif option == 2:
        show_expense()
    elif option == 3:
        delete_expense()
    elif option == 4:
        running = False
        print("Thank you for for using my expense tracker".upper().center(60, "="))
        print("\033[34mgoodbye! ".upper().center(60, "="))
        print()