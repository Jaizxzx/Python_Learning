balance = 999999
annualInterestRate = 0.18
updatedBalance = balance
monthlyinterestrate = (annualInterestRate) / 12
lowerBound = balance / 12
upperBound = (balance * (1 + monthlyinterestrate)**12) / 12
ans = (upperBound + lowerBound)/2.0

while abs(0 - updatedBalance) >= 0.01:
    updatedBalance = balance
    for i in range(0, 12):
        updatedBalance = round(((updatedBalance - ans) * (1 + monthlyinterestrate)), 2)
    if updatedBalance >= 0:
        lowerBound = ans
    else:
        upperBound = ans
    ans = (upperBound + lowerBound) / 2.0
print("Lowest Payment: ", round(ans, 2))