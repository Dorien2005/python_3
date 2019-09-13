def boek(numbers):
    maximum = max(numbers.values())
    minimum = min(numbers.values())
    lijst = [maximum, minimum]
    return lijst
    #return minimum
    
print(boek({1:2,2:3,3:4,4:5,5:6}))