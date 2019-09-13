def copy(dict):
    dictionary = dict.copy()
    return dictionary
    
print(copy({1,2,3,4,5}))


def boek(numbers):
    maximum = max(numbers.values())
    minimum = min(numbers.values())
    lijst = [maximum, minimum]
    return lijst

print(boek({1:2,2:3,3:4,4:5,5:6}))
