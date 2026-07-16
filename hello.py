import sys
#!/usr/bin/env python3

greeting="Hello, world!"
print(greeting)
# print(name)

def test():
    print("A")
    return
    print("B")

print("1")
test()
print("2")

print(f"|{'Food':<15}|")
print(f"|{'Transportation':>15}|")

print(sys.version)

print()

print("I am", 24, "years old.")

print("I am", 25)


x = y = z = "Orange"
print(x)
print(y)
print(z)



age = 36
txt = f"My name is John, I am {age}"
print(txt)

price = 60

text = f"The total is {price:.2f} dollars"

print(text)

#A backslash followed by three integers will result in a octal value:
txt = "\110\145\154\154\157"
print(txt) 


txt = "Hello\rWorld!"
print(txt) 


# #A backslash followed by an 'x' and a hex number represents a hex value:
# txt = "\x48\x65\x6c\x6c\x6f"
# print(txt) 


# x = ["apple", "banana"]
# y = ["apple", "banana"]
# z = ["apple", "banana"]

# print(x is z)
# print(x is y)
# print(x == y)


x = ["apple", "banana"]
y = ["apple", "banana"]

print(x is not y)


x = [1, 2, 3]
y = [1, 2, 3]

print(x == y)
print(x is y)
print(x is not y)

container = ["me", "mother"]
fruits = ["apple", "banana", "cherry"]
for one in fruits:
    container.append(one)
print(f"Total content: {container}")
print("banan" in fruits)



# Inside the editor, complete the following steps:

#     Create two variables a = 15 and b = 4
#     Print the result of a modulus b (the % operator)
#     Print the result of a floor division b (the // operator)
#     Print the result of a to the power of b (the ** operator)
#     Use an assignment operator to add 10 to a (use +=)




a = 15
b = 4
print(a%b)
print(a//b)
print(a**b)
a = a + 10
print(a)


print("09-090".isnumeric())



contact_phone = input("Enter phone number: ")

if not contact_phone.isdigit():
    print("Phone number must contain only digits.")




if not contact_phone.isnumeric():
    print("Only digits are allowed.")



if contact_phone.isnumeric() == False:
    print("Only digits are allowed.")