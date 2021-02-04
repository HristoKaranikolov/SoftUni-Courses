num_months = int(input())

monthly_water_bill = 20
monthly_internet_bill = 15
total_water_bill = num_months * 20
total_internet_bill = num_months * 15
total_electricity_bill = 0
total_other_bills = 0
average_bills = 0

for period in range(num_months):
    monthly_electricity_bill = float(input())
    total_electricity_bill += monthly_electricity_bill
    other_bills = total_electricity_bill + (num_months * (monthly_water_bill + monthly_internet_bill))
    total_other_bills = other_bills + (other_bills * 0.2)
    average_bills = (total_electricity_bill + total_water_bill + total_internet_bill + total_other_bills) / num_months

print(f'Electricity: {total_electricity_bill:.2f} lv')
print(f'Water: {total_water_bill:.2f} lv')
print(f'Internet: {total_internet_bill:.2f} lv')
print(f'Other: {total_other_bills:.2f} lv')
print(f'Average: {average_bills:.2f} lv')

