def calculator(amount,taxrate,roi,inflation,years):
    compount_interest =  amount * (((1 + roi/100)**years) - 1)
    after_deduct_tax = compount_interest - (compount_interest * taxrate/100)
    total_amount = round(amount + after_deduct_tax , 2)
    after_deduct_inflation = total_amount - (total_amount * inflation/100)
    final_amount = after_deduct_inflation

    print(total_amount)
    print("After deducting tax and inflation* your investment value would be " + str(final_amount) + " at the rate of " + str(roi) + "% compunded " + str(years) + " times.")
    print(" * - inflation is deducted on total amount")

calculator(100,30,10,4,4)