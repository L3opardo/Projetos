def make_negative( number ):

    if number < 0:
        return number
    else: 
        number = number - ( number * 2 )
        return number

num = int(input("numero:"))
print(make_negative(num))