expenses = []

print("welcome!".upper().center(30, "="))
print("Welcome to My Expense Tracker.\nA companion that never forgets where your money goes!")
print()

running = True
while running:

    print()
    print("menu".upper().center(24, "="))
    userOption = input("Choose....\n1. Add Expense\n2. Show Expense\n3. Exit\n")

    print("You entered =", repr(userOption))

    print()
    if userOption != "1" and userOption != "2" and userOption != "3":
        print("You must choose between 1, 2 or 3")
        continue

    option = int(userOption)
    print()
    if option == 1:
        expenseName = input("enter expense name..\n")
        amount = input("Enter expense amount..\n")
        userAmount = int(amount)
        expense = {
            "name": expenseName,
            "amount": userAmount,
        }
        expenses.append(expense)
        print(expenses)
    elif option == 2:
        get()

    elif option == 3:
        running = False















