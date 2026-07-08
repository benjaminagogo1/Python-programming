print("Welcome To My Expense Tracker.\nA companion that never forgets where your money go!")
print("")
userOption = input("Choose....\n1. Add Expense\n2. Show Expense\n3. Exit\n")

if userOption != "1" and userOption != "2" and userOption != "3":
    print("You must choose between 1, 2 or 3")

option = int(userOption)

if option == 1:
    print("Expense Name..")