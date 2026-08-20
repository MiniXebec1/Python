#positional arguments,
#docstrings,
#recursions....
def total_calc(bill_amount, tip_percentage):
    total=bill_amount*(1+0.01*tip_percentage)
    total=round(total,2)
    print("please pay:",{total})
total_calc(550,20)

def cube(number):
    return number*number*number

def by_three(number):
    if number%3 ==0:
        return cube(number)
    else:
        return False
    print(by_three(10))
    print(by_three(9))
