def kwardaat(getal):
    dictionary = {}
    for i in range(getal):
        dictionary[i + 1] = (i+1)*(i+1)
    return dictionary
print(kwardaat(5))