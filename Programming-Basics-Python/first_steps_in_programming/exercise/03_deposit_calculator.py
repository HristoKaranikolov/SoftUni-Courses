deposit_amount = float(input())
deposit_term = int(input())  # the term is in months
annual_increase_percentage = float(input())

increase = deposit_amount * (annual_increase_percentage * 0.01)
increase_per_month = increase / 12

total_sum = deposit_amount + deposit_term * increase_per_month

print(total_sum)