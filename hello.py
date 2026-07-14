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


#A backslash followed by an 'x' and a hex number represents a hex value:
txt = "\x48\x65\x6c\x6c\x6f"
print(txt) 
