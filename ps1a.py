annual_salary = int(input('Enter your annual salary: '))
portion_saved = float(input('Enter the percent of your salary to save, as a decimal: '))
total_cost = int(input('Enter the cost of your dream home: '))

portion_down_payment = 0.25
down_payment = portion_down_payment * total_cost
monthly_salary = annual_salary / 12
monthly_earnings = monthly_salary * portion_saved
current_savings = 0
total_months = 0

while current_savings <= down_payment:
    current_savings += monthly_earnings + ((current_savings * 0.04) / 12)
    total_months += 1

print('Number of months:', total_months)