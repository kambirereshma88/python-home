principal = int(input("Enter the principal amount :") )
rate = float(input("Enter the rate:"))
time = float(input("Enter the time duration :"))

#I=P*R*T/100
interest= (principal * rate * time) / 100
total_amt= principal + interest

print("interest received :", interest)
print("Total Amount:",total_amt)