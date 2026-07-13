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



From a programmer's perspective, a file is simply a sequence of bytes stored permanently on a storage device (SSD, HDD, USB, etc.).

A try block tells Python:

"I'm about to do something that might fail."

An except block tells Python:

"If it does fail, don't crash the program. Instead, run this code to handle the problem."



with open(...) as file:
    ...

The with statement makes a promise:

"No matter how this block of code ends—normally or because of an exception—I will close the file."




Reading
File
   ↓
open(..., "r")
   ↓
file.read()
   ↓
JSON string
   ↓
json.loads()
   ↓
Python list (expenses)
Writing

Now we go in the opposite direction.

Python list (expenses)
   ↓
json.dumps()
   ↓
JSON string
   ↓
file.write()
   ↓
File

Notice how beautiful the symmetry is.

Reading	Writing
open(..., "r")	open(..., "w")
file.read()	file.write(text)
json.loads()	json.dumps()



There are several approaches. For your current level, some are much better than others.

Approach 1: Move the function definition above the call ⭐ (Recommended)

Define load_expense() before you call it.

expenses = load_expense()

This is simple, readable, and common.

Approach 2: Call it after all your function definitions ⭐ (Also recommended)

Keep all your function definitions together.

Then, just before your while loop starts, do:

expenses = load_expense()

running = True
while running:
    ...

This is probably the approach I would choose for your project because it groups all the function definitions together and then starts the program.

Approach 3: Create a main() function ⭐⭐ (Best as your programs grow)

Instead of starting the program immediately, put the startup code inside a function:

def main():
    expenses = load_expense()
    ...

Then at the bottom:

main()

This becomes very useful as your projects become larger.

Approach 4: Use the if __name__ == "__main__": pattern ⭐⭐⭐ (Professional Python)
if __name__ == "__main__":
    expenses = load_expense()
    ...

This is the standard Python pattern for programs that can also be imported by other Python files.

We'll learn this later. There's no need to introduce it into this project yet.

Which one should you use?

For your Expense Tracker, I'd rank them like this:

Approach 2 — Best fit.
Approach 1 — Also perfectly fine.
Approach 3 — Learn after you've finished this project.
Approach 4 — Learn after you're comfortable with modules and importing.

I recommend Approach 2 because it keeps your code organized:

Imports
Global variables
Function definitions
Load the saved data
Start the menu (while loop)

It's clean, easy to read, and scales well as your project grows.

I do not understand this problem very well or the problem the solution below seems to solve.

Good. Let's focus on only the problem. Forget the solutions for now.

Step 1

You have this at the top of your file:

expenses = []

Later, much further down, you define:

def load_expense():
    ...

Still later, you have:

running = True
while running:
    ...

No problem so far.

Step 2

You want the program to load the saved expenses when it starts.

So naturally, you think:

expenses = load_expense()

Correct?

Step 3

Where do you want to put that line?

Do you want to put it:

A. Right after:

expenses = []
B. Somewhere else.

Tell me A or B. We won't discuss any solution until we've identified exactly where you intended to place it.



Here's the closest mapping:

Go	Python Equivalent
os.ReadFile(path)	with open(path, "r") as f: content = f.read()
os.Open(path)	open(path, "r") or with open(path, "r") as f:
os.WriteFile(path, data, perm)	with open(path, "w") as f: f.write(data)
Comparison

Go

data, err := os.ReadFile("expense.json")

Python

with open("expense.json", "r") as file:
    data = file.read()

Go

file, err := os.Open("expense.json")

Python

file = open("expense.json", "r")

or preferably:

with open("expense.json", "r") as file:
    ...

Go

err = os.WriteFile("expense.json", data, 0644)

Python

with open("expense.json", "w") as file:
    file.write(data)

One important difference you've probably noticed:

Go has convenience functions like os.ReadFile() and os.WriteFile().
Python usually uses open() together with .read() or .write() instead of separate ReadFile and WriteFile functions.






This is actually an excellent question, especially because I know where you left off in Go.

You weren't a complete beginner anymore. You had learned things like:

Functions
Structs (basic use)
Slices
Maps
Packages
Reading/writing files
JSON (Marshal/Unmarshal)
Error handling
HTTP servers (ascii-art-web)
Dockerizing an application

So rather than relearning programming, you're translating concepts from Go into Python.

If I were mentoring you, these are the differences I'd keep reminding you about.

1. Variables
Go
age := 20
Python
age = 20

Python has no := for normal variable declaration and no explicit types.

Remember: Python variables are names pointing to objects.

2. Types

Go

var age int

Python

age = 20

No type declaration.

Python figures it out.

3. Braces vs Indentation

Go

if age > 18 {
    fmt.Println("Adult")
}

Python

if age > 18:
    print("Adult")

This is the biggest visual change.

Indentation replaces braces.

4. Semicolons

Go

fmt.Println("Hello")

Python

print("Hello")

No semicolons.

5. Error Handling

Go

file, err := os.Open(...)
if err != nil {
    return err
}

Python

try:
    ...
except FileNotFoundError:
    ...

This is probably the biggest conceptual difference.

6. Functions Returning Values

Go

return value

Python

return value

Exactly the same.

7. Lists vs Slices

Go

[]string

Python

[]

Python lists are much more powerful.

Think of them as slices that already have many built-in methods.

8. Maps vs Dictionaries

Go

map[string]int

Python

{}

These are almost the same idea.

9. Structs vs Dictionaries

Go

type Expense struct {
    Name string
}

Python beginner code

{
    "name": "Food"
}

Later you'll learn Python classes, which are closer to Go structs.

10. Methods

Go

expense.Print()

Python

Exactly the same idea with classes.

You'll learn this later.

11. Loops

Go

One keyword:

for

Python

Mostly:

for

and

while

Python's for loop feels much more natural.

12. File Handling

Go

os.ReadFile()
os.WriteFile()

Python

open()
read()
write()

You've already learned this.

13. JSON

Go

json.Marshal()
json.Unmarshal()

Python

json.dumps()
json.loads()

You already understand this mapping.

14. Pointers

Go

Pointers are everywhere.

Python

Almost never.

This surprises many Go programmers.

15. Interfaces

Go

Huge topic.

Python

Duck typing.

If something behaves correctly, Python usually doesn't care about its type.

16. Packages

Go

import "fmt"

Python

import json

Almost identical.

17. Visibility

Go

Print()

Exported.

print()

Private.

Python

Uses convention:

_print()

means "internal".

No compiler enforcement.

18. Classes

Go

Struct + methods.

Python

Class.

Very similar once you learn them.

19. Concurrency

Go

go function()

Python

Different tools (threading, asyncio, multiprocessing).

This comes much later.

20. Philosophy

This is the biggest difference.

Go says:

Be explicit.

Python says:

Be readable.

The three mindset changes I'd keep reminding you of
Don't look for Go syntax in Python. Learn the Python way instead of translating line by line.
Python has many built-in conveniences. Before writing code yourself, ask, "Does Python already provide this?"
Write for readability first. In Python, code is expected to be easy to read by another programmer.

These are the differences I'd keep at your fingertips as you continue your Python journey. Many of the remaining concepts—classes, modules, testing, decorators, generators, asynchronous programming—will build on the programming foundation you already developed in Go, but they'll often be expressed in a more concise, Pythonic way.






Yes. There are many exception types in Python. Here are some of the most common ones you'll encounter.

try:
    ...
except FileNotFoundError:
    ...
File-related
except FileNotFoundError:

File does not exist.

except PermissionError:

No permission to access the file.

except OSError:

General operating system/file error.

except IsADirectoryError:

Expected a file but got a directory.

except NotADirectoryError:

Expected a directory but got a file.

JSON
except json.JSONDecodeError:

Invalid JSON.

Numbers
except ValueError:

Correct type, invalid value.

Example:

int("abc")
except TypeError:

Wrong data type.

Example:

5 + "hello"
except ZeroDivisionError:

Division by zero.

Collections
except IndexError:

List index out of range.

Example:

expenses[10]
except KeyError:

Dictionary key does not exist.

Example:

expense["price"]

when only "amount" exists.

Variables
except NameError:

Using a variable that doesn't exist.

Example:

print(totalExpense)

before defining it.

Importing
except ImportError:

Module cannot be imported.

Catching multiple exceptions
try:
    ...
except (FileNotFoundError, PermissionError):
    print("Unable to open file.")
Catching any exception
try:
    ...
except Exception as err:
    print(err)

or

try:
    ...
except Exception:
    print("Something went wrong.")

Exception catches most runtime errors. It's useful as a last resort, but when you know the specific error (like FileNotFoundError or JSONDecodeError), it's better to catch that specific exception