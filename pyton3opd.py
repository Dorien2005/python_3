def boek(numbers, key):
    del numbers[key]
    return numbers

print(boek({1:2,2:3,3:4,4:5,5:6}, 5))