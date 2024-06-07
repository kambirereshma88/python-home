def convertor(usd_val):
    inr_val=usd_val*83
    print(usd_val,"USD",inr_val,"INR")

convertor(85)


#even odd  number
def number(n):
    if n%2==0:
        return ("even")
    else:
        return ("odd")
    
print (number(10))