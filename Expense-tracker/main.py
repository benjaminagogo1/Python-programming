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
    expenseDate = input("Enter the date..\n")
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
    print("expenses".upper().center(28, "="))
    for expense in expenses:
        print(f"{number}. {expense["name"]}: ₦{expense["amount"]} |{expense["date"]}")
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
    item_selected = input("which expense do you want to edit?\n")
    for expense_to_edit in expenses:
        if item_selected != expense_to_edit["name"]:
            print()


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
