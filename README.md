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