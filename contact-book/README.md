A better version of Approach 3

Instead of a string, use a collection of valid choices.

accepted_numbers = ["1", "2", "3", "4"]

if chosen_option not in accepted_numbers:

or even better,

accepted_numbers = {"1", "2", "3", "4"}

if chosen_option not in accepted_numbers:

A set ({}) is designed for membership testing.



What is bytecode?

Think of it as:

A simpler, lower-level version of Python instructions that the Python Virtual Machine can understand


It is not human-readable.

It is not machine code either.

It sits in between.



Why does Python use bytecode?

Imagine reading a book written in French.

If you read it every day, would you translate every sentence from scratch every morning?

Probably not.

You would translate it once and keep the translated version.

Python does something similar.

Instead of translating your .py file every time, it stores the translated version as:



The next time you run your program, Python can often use that compiled version, making startup faster.

Who understands bytecode?

Not the CPU.

The Python Virtual Machine (PVM) understands bytecode.

Think of it as a translator:

Bytecode
    │
    ▼
Python Virtual Machine
    │
    ▼
Machine instructions
    │
    ▼
CPU


Does every programming language use bytecode?

No.

Different languages take different approaches.

Python → Source Code → Bytecode → Python Virtual Machine → CPU
Java → Source Code → Bytecode → Java Virtual Machine (JVM) → CPU
Go → Source Code → Machine Code → CPU
C → Source Code → Machine Code → CPU

So bytecode is one possible design, not a requirement for every language.


Earlier, we said Python creates a .pyc file to make future runs faster. That's true, but the .pyc file specifically contains Python bytecode—instructions for the Python Virtual Machine, not instructions that the CPU can execute directly.