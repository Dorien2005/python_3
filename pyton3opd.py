def lampje(array,string):
    array.append(string)
    if string in array:
        array.remove(string)
        return array
    else:
        return array
    
print(lampje(["delete", "formule"],"modus"))
