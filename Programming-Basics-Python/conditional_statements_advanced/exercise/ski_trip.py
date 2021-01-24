days = int(input())
room_type = input()
review = input()
nights = days - 1

rooms_and_prices_per_night = {"room for one person": 18.00,
                              "apartment": 25.00,
                              "president apartment": 35.00}

price = rooms_and_prices_per_night[room_type] * nights

# Discounts
if room_type == 'apartment':
    if days < 10:
        price *= 0.70
    elif 10 < days <= 15:
        price *= 0.65
    else:
        price *= 0.50
if room_type == 'president apartment':
    if days < 10:
        price *= 0.90
    elif 10 < days <= 15:
        price *= 0.85
    else:
        price *= 0.80

if review == 'positive':
    price *= 1.25
else:
    price *= 0.9

print(f'{price:.2f}')
