import math
# string data types

first = "Benjamin"
last = "Agogo"
print(type(first))
print(type(first) == str)
print(isinstance(last, str))

# concatenation

fullname = "otete Benjamin" " Agogo"
# print(fullname)

fullname += "!"
print(fullname)

decade = str(2000)
print(type(decade))

statement = "I like soulful gospel songs from " + decade + "s."
print(statement)

# Escaping Specail Characters

sentence = "I'm back at work\ntHey!\n\ntcome"
print(sentence)

print("")
print("")

print(first)
print(first.lower())
print(first.upper())
print(last.replace("Agogo", "Otete"))
last = "Otete"
print(fullname)

print("")

title = "menu".upper()
print(title.center(24, "="))
print("Bread".ljust(16, ".") + " #200")
print("Fish".ljust(16, ".") + " #500")
print("Oil".ljust(16, ".") + " #1000")
print("menu".upper().center(24, "="))


print("")

# string index vlues

me = "Benjamin"
he = "Agogo"
# print(me[-1])
# print(me[0])
# print(me[1:])

print(me.startswith("k"))
print(me.startswith("B"))


# Boolean Datat Type
MyValue = True
x = bool(False)
print(x)
print(MyValue)
print(isinstance(MyValue, bool))


# Numeric data types
 
# Integer type
price = 100
best_price = 600
print(type(price))
print(isinstance(best_price, int))

# float type

print("")

gpa = 3.35
pa = 5
print(gpa)
print(abs(gpa))
print(abs(gpa *-1))
print(round(gpa, 1))
print(math.pi)
print(float(pa))
print(type(gpa))

# complex type

comp_value = 5j+3j
print(comp_value)
print(comp_value.real)
print(comp_value.imag)
print(type(comp_value))