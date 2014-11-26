#work details
def work_details(hours,pay):
    hours = int(input("please enter total hours worked: "))
    pay = float(input("please enter pay rate: "))
    return hours,pay

#basic pay

def calculate_basic_pay(hours,pay):
    total = hours * pay
    return total

#overtime pay

def overtime_pay(hours,pay):
    total= (hours - 40) * (pay * 1.5) + (pay * 40)
    return total

#calculate total pay
def calculate_total_pay(hours,pay):
    if hours <= 40:
        total = calculate_basic_pay(hours,pay)
    else:
        total = overtime_pay(hours,pay)
    return total

def calculate_pay(hours,pay):
    hours,pay = work_details(hours,pay)
    total = calculate_total_pay(hours,pay)
    print("You earned a total of £{0}".format(total))

#main program
hours = 0
pay = 0
calculate_pay(hours,pay)
    
