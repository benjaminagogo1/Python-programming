#!/usr/bin/env python3


Part 1: #!

This is called the shebang (or hashbang).

# is the hash symbol.
! is the exclamation mark.

Together:

#!

tell the Linux kernel:

"This file is not a native executable. Use the program written after these two characters to execute it."

Without the shebang, Linux doesn't know your file contains Python code.

Part 2: /usr/bin/env

This is a path to a program named env.

Let's split it:

/
usr
bin
env
/ means "start from the root directory."
usr is a directory.
bin stands for binaries (executable programs).
env is a program.

So:

/usr/bin/env

is the full path to the env program.

What does env do?

One of its jobs is to find another program using your PATH.

For example, when you type:

python3

your shell searches the directories listed in your PATH until it finds the python3 executable.

env can do the same thing.

Part 3: python3

This is the program that should execute your file.

So Linux reads:

#!/usr/bin/env python3

and understands it like this:

"Run /usr/bin/env and ask it to find python3. Then use that Python interpreter to execute this script."

Why not just write:
#!/usr/bin/python3

You can.

But it's less portable.

Different Linux systems install Python in different locations.

For example:

Ubuntu:

/usr/bin/python3

Another system:

/usr/local/bin/python3

Or a virtual environment:

/your/project/.venv/bin/python3

If you hardcode:

#!/usr/bin/python3

it only works if Python is exactly there.

Using:

#!/usr/bin/env python3

lets env find the correct python3 for the current environment.

That's why it's the recommended form.

What Linux does behind the scenes

When you run:

./hello.py

Linux opens the file and reads the first line:

#!/usr/bin/env python3

Then it effectively runs something like:

/usr/bin/env python3 ./hello.py

env then locates python3 and starts it, passing your script as an argument.

An important observation

Notice that the shebang is not Python code.

Python never executes this line.

It's only read by the operating system when you execute the file directly with:

./hello.py

If you instead run:

python3 hello.py

Python opens the file itself and ignores the shebang, because you have already told it which interpreter to use.

Everything in python is an object.

"benjamin" is an  object type of string.
21 is an object type of int
etc.

A variable is a name that refers to an object in memory.

1. Immutable objects

These cannot be changed after they are created.

Examples:

int
float
bool
str
tuple

Example:

name = "Benjamin"



2. Mutable objects

These can be changed after they are created.

Examples:

list
dict
set

A list is an ordered collection of items.

A parameter is a variable that belongs to the function. Its value is supplied when the function is called.



There is no type annotation required. Python will accept any object unless you explicitly add type.


Imagine you're filling out a form

The form says:

Name: ____________
Age:  ____________

The labels Name and Age are like parameters.

When you fill in:

Name: Benjamin
Age: 25

The values Benjamin and 25 are like arguments.

In Python

Suppose we define a function:

def greet(name):
    print("Hello,", name)
During the definition
def greet(name):

name is the parameter.

Think of it as an empty placeholder.

Parameter

name = ________

Now we call the function:

greet("Benjamin")

Here:

"Benjamin"

is the argument.

It is the actual value being passed into the function.

Python temporarily does something conceptually like this:

name = "Benjamin"

print("Hello,", name)

When the function finishes, that local variable name disappears.

Another example
def add(a, b):
    print(a + b)

Here:

a
b

are parameters.

Now we call it:

add(10, 20)

Here:

10
20

are arguments.

Python conceptually does:

a = 10
b = 20

print(a + b)

Output:

30



A trick to remember

I use this mental shortcut:

Parameter = Placeholder
Argument = Actual value

Or even simpler:

Parameters appear in the function definition.

def greet(name):

Arguments appear in the function call.

greet("Benjamin")


The keys "name" and "amount" are repeated. In a dictionary, each key must be unique. You can't have multiple "name" keys representing different expenses in the same dictionary.

So one dictionary is meant to describe one thing. In our case, that "one thing" is a single expense.


Whenever you have different pieces of information that belong to one thing, a dictionary is often a good choice.

A dictionary is simply a collection of key–value pairs.


print("You entered", repr(userOption))


print("userOption =", userOption)
print(f"userOption = {userOption}")
print(f'userOption = "{userOption}"')
print("You entered", repr(userOption))


Delete an expense.
Show the total amount spent.
Search for an expense by name.
Save expenses to a file so they don't disappear when the program exits.

successfully deleted.
item added




Benjamin, I really like this question.

This is the kind of question a software engineer asks after shipping Version 1:

"How can I improve it?"

Let's review it as if I were reviewing a pull request from a junior developer on my team.

⭐⭐⭐⭐⭐ Program Structure (Already there)

You already have:

A main loop
Clear menu
Logical flow
No duplicated logic that causes bugs
The program keeps running until the user exits

Nothing to change here for Version 1.

Later we'll improve it with functions.

⭐⭐⭐⭐☆ → ⭐⭐⭐⭐⭐ Input Validation

Right now you validate:

✅ Menu choice
✅ Amount
✅ Delete choice

I'd give the last star if you also validate:

Expense name

Don't allow this:

Expense name:
<user presses Enter>

or

Expense name:
     

Instead:

if expenseName.strip() == "":
    print("Expense name cannot be empty.")
    continue
Date

Right now I can type:

banana

as a date.

The program accepts it.

Later we'll learn proper date validation.

⭐⭐⭐⭐☆ → ⭐⭐⭐⭐⭐ Code Readability

Your code is already easy to read.

I'd improve it by reducing duplication.

Look at these two sections:

number = 1
total = 0

for expense in expenses:
    ...

You wrote almost the same code twice.

Professional developers don't like repeating code.

Later we'll do:

show_expenses()

instead.

I'd also improve variable names slightly.

Instead of:

userOption

I'd probably write:

menu_choice

because it immediately tells me what the variable means.

⭐⭐⭐⭐☆ → ⭐⭐⭐⭐⭐ User Experience

This is where you can have the most fun.

For example...

Instead of:

Food deleted successfully.

you could print:

✅ Food deleted successfully.

When adding an expense:

Expense added successfully.

instead of silently returning to the menu.

When exiting:

Thank you for using My Expense Tracker!
Goodbye!

instead of just ending.

When there are no expenses:

Instead of:

==========EXPENSES==========

show:

No expenses found.

After deleting:

Show the updated list automatically.

That feels much smoother.

⭐⭐⭐⭐⭐⭐ (Beyond five stars)

These aren't required, but they're what I'd add to Version 2 or 3.

Search
Search expense:

Food

Found:

Food
₦6000
6/7/26
Edit
Edit expense

1. Food

New amount:
7000
Save to file

Today, every time you exit:

Everything disappears.

We'll fix that.

Load from file

When you start the program again:

Loading expenses...

Everything comes back.

Pretty table

Instead of:

1. Food: ₦6000 |6/7/26

show:

-----------------------------------------
No  Name         Amount      Date
-----------------------------------------
1   Food         ₦6000       6/7/26
2   Transport    ₦4000       4/7/26
-----------------------------------------
Total            ₦10000

That looks like a professional terminal application.

The biggest improvement

If I could only choose one thing to improve your project, it wouldn't be a new feature.

It would be this:

def add_expense():
    ...

def show_expenses():
    ...

def delete_expense():
    ...

Why?

Because your while loop is becoming long.

A good main loop should read almost like English:

while running:
    show_menu()

    if option == 1:
        add_expense()
    elif option == 2:
        show_expenses()
    elif option == 3:
        delete_expense()
    elif option == 4:
        running = False

Look at that.

You can almost read it without knowing Python.

That's one of the goals of clean code.

My recommendation

I don't think you should add more features yet.

I think you've earned the right to learn functions.

Not because your program is broken, but because your program has become large enough that functions will solve a real problem.

That's exactly how I want you to learn: introduce a concept when the project naturally demands it, not because it's next in a textbook.

I think this is the perfect moment to make that transition.

String
   │
   ├── strip()
   ├── upper()
   ├── lower()
   ├── replace()
   └── split()





   found = False

Why?

Because before you search, you haven't found anything yet.

Then during the loop:

If you find a matching expense, change it to:
found = True

After the loop, ask:

if not found:
    print("Expense not found.")