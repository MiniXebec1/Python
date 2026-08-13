# Function: block of code to perform some specfic task
# game: sound,UI,levels,players
# small chunks: functions
# in-built: print(), input(),int(),enumerate(),len()...
# user-define function:by using def keyword
# Syntax:
# def functionName():
#     function code
# functionName()

def greet():
    print("Hello! Welcome to functions world! ")
greet()

def greetings(name):
    print("Hello", name, "! Welcome to functions world! ")
greetings("Ben")
def greet_customer():
    print("Welcome to the lemonade stand")
    print("fresh lemonade is available")
    greet_customer()
    price_per_cup = float(input("Enter the price per cup: "))
    cups_sold = int(input("Enter the number of cups sold: "))
    def calculate_total_sales(price, cups):
        total_sales = price * cups
        return total_sales
    total = calculate_total_sales(price_per_cup, cups_sold)
    rounded_total = round(total, 2)
    print("Total sales: $", rounded_total)
    amount_paid = float(input("Enter the amount paid by the customer: "))