flower_type = input()
flower_count = int(input())
budget = int(input())

flower_types_and_prices = {"Roses": 5.00,
                           "Dahlias": 3.80,
                           "Tulips": 2.80,
                           "Narcissus": 3.00,
                           "Gladiolus": 2.50}

price = 0
if flower_type in flower_types_and_prices:
    price = flower_types_and_prices[flower_type] * flower_count
    if flower_type == "Roses" and flower_count > 80:
        price *= 0.90  # Price with discount
    elif flower_type == "Dahlias" and flower_count > 90:
        price *= 0.85  # Price with discount

    elif flower_type == 'Tulips' and flower_count > 80:
        price *= 0.85  # Price with discount
    elif flower_type == 'Narcissus' and flower_count < 120:
        price *= 1.15  # More expensive
    elif flower_type == 'Gladiolus' and flower_count < 80:
        price *= 1.20  # More expensive

difference = abs(budget - price)
if budget < price:
    print(f"Not enough money, you need {difference:.2f} leva more.")
else:
    print(f"Hey, you have a great garden with {flower_count} {flower_type} and {difference:.2f} leva left.")
