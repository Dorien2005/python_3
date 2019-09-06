def hoogste_van_drie(x):
    if x[0] > x[1] and x[0]>x[2]:
        print(x[0])
    elif x[1] > x[0] and x[1] > x[2]:
        print(x[1])
    else:
        print(x[2])
        
    
hoogste_van_drie([4,2,9])