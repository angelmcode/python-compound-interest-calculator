#the data for the variables is requested
initial_capital=int(input("Enter the initial capital: "))
years_invest=int(input("Enter the number of years to invest: "))
annual_interest=float(input("Enter the annual interest rate: "))
monthly_contribution=int(input("Enter the monthly contribution amount: "))


# the variables are adjusted
initialcapital=int(initial_capital)
yearsinvest=int(years_invest*12)
annualinterest=float((annual_interest/100)/12)
monthly_contribution=int(monthly_contribution)


# the initial capital is converted into the resulting capital to perform the calculation
resulting_capital = initial_capital

# the calculation of the capital plus the interest for the first period is performed
resulting_capital = resulting_capital * (1 + annualinterest)

# print the calculation of the initial capital plus the interests for the first period
print(resulting_capital)

# a loop is performed to calculate the capital plus the interest plus the monthly contribution
for i in range( yearsinvest - 1 ):
    resulting_capital = resulting_capital + monthly_contribution
    resulting_capital = resulting_capital * (1 + annualinterest)
    
    # the result is formatted to only show two decimal places, but without rounding
    print("{:.2f}".format(resulting_capital))
    



