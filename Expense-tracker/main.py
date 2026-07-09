expenses = []

print("welcome!".upper().center(30, "="))
print("Welcome to My Expense Tracker.\nA companion that never forgets where your money goes!")
print()

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
        expenseName = input("Enter expense name..\n")
        amount = input("Enter expense amount..\n")
        try:
            amount = int(amount)
        except ValueError:
            print("Invalid input: enter only digit")
            continue
        expenseDate = input("Enter the date..\n")
        expense = {
            "name": expenseName,
            "amount": amount,
            "date": expenseDate
        }
        expenses.append(expense)
    elif option == 2:
        total = 0
        number = 1
        print("expenses".upper().center(28, "="))
        for expense in expenses:
            print(f"{number}. {expense["name"]}: ₦{expense["amount"]} |{expense["date"]}")
            number += 1
            total += expense["amount"]
        print()
        print(f"Total expenses: = ₦{total}")
    elif option == 3:
        if not expenses:
            print("No expense to delete.")
            continue
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
            continue
        index = choice -1
        if choice < 1 or choice > len(expenses):
            print("Choose from the the list of expenses")
            continue
        deleted = expenses.pop(index)
        print(f"\033[31m{deleted["name"]} deleted successfully.\033[0m")

    elif option == 4:
        running = False











