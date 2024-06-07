# Write a program using functions to Compute the monthly payment, given the loan amount, number of years and

#the annual interest rate.



def calculate_monthlypay(loan_amt,annual_int_rate,years):

    monthly_int_rate = annual_int_rate/100/12

    total_payment= years*12

    if monthly_int_rate == 0:
        monthlypay=loan_amt/total_payment
    else:
        monthlypay=loan_amt*(monthly_int_rate*(1+monthly_int_rate)**total_payment)/((1+monthly_int_rate) ** total_payment-1)


    return monthlypay



loan_amt=float(input("Enter the loan amount:"))
annual_int_rate=float(input("Enter the annual interest rate(as a percentage): "))
years=int(input("Enter the number of years for the loan: "))


monthlypay= calculate_monthlypay(loan_amt,annual_int_rate,years)

print(f"the monthly payment for the loan is :{monthlypay:.2f} ")



    
