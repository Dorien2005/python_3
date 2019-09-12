def boek(numbers):
    totaaal = 0
    for key, value in numbers.items():
        totaaal = totaaal + value
    return totaaal
    

print(boek({1:2,2:3,3:4,4:5,5:6}))