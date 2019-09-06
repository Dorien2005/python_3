def omdraaien(x):
    reverse_x = x[::-1]
    if x == reverse_x:
        return True
    else:
        return False
    
print(omdraaien("racecar"))