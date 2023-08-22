balance = float(input('Enter the initial amount in your card:'))
annualInterestRate = float(input('Enter the annual interest rate:'))
monthlyinterestRate = annualInterestRate/12
mfmp = 10
while True:
    ub0 = balance - balance*monthlyinterestRate
    interest = (annualInterestRate/12*ub0)
    b1 = ub0 + interest
    mub1 = balance - mfmp
    ubem1 = mub1 + monthlyinterestRate*mub1
    #print(round(b1,2))
    ub1 = b1 - b1*monthlyinterestRate
    interest = (annualInterestRate/12*ub1)
    b2 = ub1 + interest
    mub2 = ubem1 - mfmp
    ubem2 = mub2 + monthlyinterestRate*mub2
    #print(round(b2,2))
    ub2 = b2 - b2*monthlyinterestRate
    interest = (annualInterestRate/12*ub2)
    b3 = ub2 + interest
    mub3 = ubem2 - mfmp
    ubem3 = mub3 + monthlyinterestRate*mub3
    #print(round(b3,2))
    ub3 = b3 - b3*monthlyinterestRate
    interest = (annualInterestRate/12*ub3)
    b4 = ub3 + interest
    mub4 = ubem3 - mfmp
    ubem4 = mub4 + monthlyinterestRate*mub4
    #print(round(b4,2))
    ub4 = b4 - b4*monthlyinterestRate
    interest = (annualInterestRate/12*ub4)
    b5 = ub4 + interest
    mub5 = ubem4 - mfmp
    ubem5 = mub5 + monthlyinterestRate*mub5
    #print(round(b5,2))
    ub5 = b5 - b5*monthlyinterestRate
    interest = (annualInterestRate/12*ub5)
    b6 = ub5 + interest
    mub6 = ubem5 - mfmp
    ubem6 = mub6 + monthlyinterestRate*mub6
    #print(round(b6,2))
    ub6 = b6 - b6*monthlyinterestRate
    interest = (annualInterestRate/12*ub6)
    b7 = ub6 + interest
    mub7 = ubem6 - mfmp
    ubem7 = mub7 + monthlyinterestRate*mub7
    #print(round(b7,2))
    ub7 = b7 - b7*monthlyinterestRate
    interest = (annualInterestRate/12*ub7)
    b8 = ub7 + interest
    mub8 = ubem7 - mfmp
    ubem8 = mub8 + monthlyinterestRate*mub8
    #print(round(b8,2))
    ub8 = b8 - b8*monthlyinterestRate
    interest = (annualInterestRate/12*ub8)
    b9 = ub8 + interest
    mub9 = ubem8 - mfmp
    ubem9 = mub9 + monthlyinterestRate*mub9
    #print(round(b9,2))
    ub9 = b9 - b9*monthlyinterestRate
    interest = (annualInterestRate/12*ub9)
    b10 = ub9 + interest
    mub10 = ubem9 - mfmp
    ubem10 = mub10 + monthlyinterestRate*mub10
    #print(round(b10,2))
    ub10 = b10 - b10*monthlyinterestRate
    interest = (annualInterestRate/12*ub10)
    b11 = ub10 + interest
    mub11 = ubem10 - mfmp
    ubem11 = mub11 + monthlyinterestRate*mub11
    #print(round(b11,2))
    ub11 = b11 - b11*monthlyinterestRate
    interest = (annualInterestRate/12*ub11)
    b12 = ub11 + interest
    mub12 = ubem11 - mfmp
    ubem12 = mub12 + monthlyinterestRate*mub12
    if ubem12 >0:
        mfmp = mfmp +10
        continue
    elif ubem12 <0:
        print('Lowest Payment:',mfmp)
        break