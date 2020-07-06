def calculator(amount,taxrate,roi,inflation,years):
    interest = (amount * roi)/100 
    after_tax = interest - (interest * taxrate)/100
    sum_up = after_tax + amount
    after_inflation = sum_up - (sum_up * inflation)/100

    interest_amnt = after_inflation - amount
    interest_rate_calc = (interest_amnt * 100)/amount

    ior = (interest_rate_calc/100)
    compound_interest_amnt = round(amount * ((1 + ior)**years - 1))

    print("On your investment you will recieve total interest of " + str(compound_interest_amnt) + " at the rate of " + str(interest_rate_calc) + "% p.a.")

calculator(100000,30,10,4,4)


