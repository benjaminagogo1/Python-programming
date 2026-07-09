expenses = []

print("Welcome To My Expense Tracker.\nA companion that never forgets where your money goes!")
print()

running = True
while running:

    userOption = input("Choose....\n1. Add Expense\n2. Show Expense\n3. Exit\n")


    if userOption != "1" and userOption != "2" and userOption != "3":
        print("You must choose between 1, 2 or 3")

    option = int(userOption)

    if option == 1:
        expenseName = input("Expense Name..\n")
        amount = input("Expense Amount..\n")
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















