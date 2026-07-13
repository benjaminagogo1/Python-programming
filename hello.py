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