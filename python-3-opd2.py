def is_priemgetal(num):
    if num > 1:
        for i in range(2,num):
           if (num % i) == 0:
               print(num,"is geen priemgetal")
               break
        else:
           print(num,"is een priemgetal")
       
    else:
       print(num,"is geen priemgetal")       
is_priemgetal(23)