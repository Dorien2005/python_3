dieren = {"panda": "bamboe", "leeuw": "zebra", "haai": "vis"}

dieren["koe"] = "gras"

del dieren["koe"]

for key in dieren:
    print(key)
    print(dieren[key])
    
print("raad welke dieren in de dictonary zitten")
gok = input()

if gok in dieren:
    print(gok + " ja die zit er tussen")
else:
    print(gok + " nee die zit er niet tussen")