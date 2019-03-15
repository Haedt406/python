# ---------------------------------------
# CSCI 127, Joy and Beauty of Data      |
# Lab 2: Tax Calculator                 |
# Benjamin Haedt                        |
# Date: January 24, 2019                |
# ---------------------------------------
# Calculate the amount of tax owed by an|
# unmarried taxpayer in tax year 2018.  |
# ---------------------------------------

def unmarried_individual_tax (income):
    
    x1 = 9700
    y1 = 9700 * .10
    
    x2 = 39475
    y2 = (39475 - 9700) * .12
    
    x3 = 84200
    y3 = (84200 - 39475)  * .22
    
    x4 = 160725
    y4 = (160725 - 84200) * .24
    
    x5 = 204100
    y5 = (204100 - 160725) * .32
    
    x6 = 510300
    y6 = (510300 - 204100) * .35

    
    if 0 <= income < x1:
        return income * .10
    
    if x1 <= income < x2:
        return (income - x1) * .12 + y1
    
    if x2 <= income < x3:
        return (income - x2) * .22 + (y1 + y2)
    
    if x3 <= income < x4:
        return (income - x3) * .24 + (y3 + y2 + y1)
    
    if x4 <= income < x5:
        return (income - x4) * .32 + (y4 + y3 + y2 + y1)
    
    if x5 <= income < x6:
        return (income - x5) * .35 + (y5 + y4 + y3 + y2 + y1)
    
    if 510300 <= income:
        return (income - x6) * .37 + (y6 + y5 + y4 + y3 + y2 + y1)
    
def process(income):
    print("The 2018 taxable income is ${:.2f}".format(income))
    tax_owed = unmarried_individual_tax(income)
    print("An unmarried individual owes ${:.2f}\n".format(tax_owed))



def main():
    process(5000)      # test case 1
    process(20000)     # test case 2
    process(50000)     # test case 3
    process(100000)    # test case 4
    process(200000)    # test case 5
    process(400000)    # test case 6
    process(600000)    # test case 7



main()
