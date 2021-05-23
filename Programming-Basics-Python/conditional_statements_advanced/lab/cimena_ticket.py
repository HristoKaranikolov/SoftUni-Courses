day = input()

days_and_prices = {'Monday': 12,
                   'Tuesday': 12,
                   'Wednesday': 14,
                   'Thursday': 14,
                   'Friday': 12,
                   'Saturday': 16,
                   'Sunday': 16}

result = 0
if day in days_and_prices:
    result = days_and_prices[day]
print(result)
