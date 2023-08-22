balance = float(input('Enter the initial amount in your card:'))
annualInterestRate = float(input('Enter the annual interest rate:'))
monthlyPaymentRate = float(input('Enter the monthly payment rate:'))
ub0 = balance - balance*monthlyPaymentRate
interest = (annualInterestRate/12*ub0)
b1 = ub0 + interest
#print(round(b1,2))
ub1 = b1 - b1*monthlyPaymentRate
interest = (annualInterestRate/12*ub1)
b2 = ub1 + interest
#print(round(b2,2))
ub2 = b2 - b2*monthlyPaymentRate
interest = (annualInterestRate/12*ub2)
b3 = ub2 + interest
#print(round(b3,2))
ub3 = b3 - b3*monthlyPaymentRate
interest = (annualInterestRate/12*ub3)
b4 = ub3 + interest
#print(round(b4,2))
ub4 = b4 - b4*monthlyPaymentRate
interest = (annualInterestRate/12*ub4)
b5 = ub4 + interest
#print(round(b5,2))
ub5 = b5 - b5*monthlyPaymentRate
interest = (annualInterestRate/12*ub5)
b6 = ub5 + interest
#print(round(b6,2))
ub6 = b6 - b6*monthlyPaymentRate
interest = (annualInterestRate/12*ub6)
b7 = ub6 + interest
#print(round(b7,2))
ub7 = b7 - b7*monthlyPaymentRate
interest = (annualInterestRate/12*ub7)
b8 = ub7 + interest
#print(round(b8,2))
ub8 = b8 - b8*monthlyPaymentRate
interest = (annualInterestRate/12*ub8)
b9 = ub8 + interest
#print(round(b9,2))
ub9 = b9 - b9*monthlyPaymentRate
interest = (annualInterestRate/12*ub9)
b10 = ub9 + interest
#print(round(b10,2))
ub10 = b10 - b10*monthlyPaymentRate
interest = (annualInterestRate/12*ub10)
b11 = ub10 + interest
#print(round(b11,2))
ub11 = b11 - b11*monthlyPaymentRate
interest = (annualInterestRate/12*ub11)
b12 = ub11 + interest
print('Remaining Balance:',round(b12,2))