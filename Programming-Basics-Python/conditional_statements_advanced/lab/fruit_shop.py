fruit = input()
day = input()
quantity = float(input())

weekdays = 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday'
weekend = 'Saturday', 'Sunday'
weekday__fruits_and_prices = {'banana': 2.50,
                              'apple': 1.20,
                              'orange': 0.85,
                              'grapefruit': 1.45,
                              'kiwi': 2.70,
                              'pineapple': 5.50,
                              'grapes': 3.85}

weekend_fruits_and_prices = {'banana': 2.70,
                             'apple': 1.25,
                             'orange': 0.90,
                             'grapefruit': 1.60,
                             'kiwi': 3.00,
                             'pineapple': 5.60,
                             'grapes': 4.20}

if day in weekdays:
    if fruit in weekday__fruits_and_prices:
        price = weekday__fruits_and_prices[fruit]
        print(f'{price * quantity:.2f}')
    else:
        print('error')

elif day in weekend:
    if fruit in weekend_fruits_and_prices:
        price = weekend_fruits_and_prices[fruit]
        print(f'{price * quantity:.2f}')
    else:
        print('error')
else:
    print('error')
