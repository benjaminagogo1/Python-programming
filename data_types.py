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