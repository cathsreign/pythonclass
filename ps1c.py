annual_salary = int(input('Enter the starting salary: '))

total_cost = 1000000
portion_down_payment = 0.25
down_payment = portion_down_payment * total_cost
semi_annual_raise = 0.07
current_savings = 0

steps = 0
low = 0
high = 10000

guess = int((low + high) / 2)
guess_rate = guess / 1000

def savings (current_savings, down_payment, annual_salary, semi_annual_raise, guess_rate):

    for months in range(0,36):
        if months % 6 == 0 and months != 0:
            annual_salary += (annual_salary * semi_annual_raise)

        current_savings += guess_rate * annual_salary / 12 + current_savings * 0.04 / 12

    return current_savings

current_savings = savings (0, down_payment, annual_salary, semi_annual_raise, guess_rate)

if current_savings < down_payment:
    print("You cannot pay for the down payment in 3 years.")

else:
    current_savings = savings(0, down_payment, annual_salary, semi_annual_raise, guess_rate)
    steps += 1

    while abs(down_payment - current_savings) >= 100:
        if down_payment > current_savings:
            guess = low
        else:
            guess = high

        guess = int((low + high) / 2)
        guess_rate = guess / 1000

        current_savings = int(savings(0, down_payment, annual_salary, semi_annual_raise, guess_rate))
        steps += 1

print('Best savings rate:', guess_rate)
print('Steps in bisection search:', steps)