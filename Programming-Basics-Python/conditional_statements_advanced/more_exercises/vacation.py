budget = float(input())
season = input()

accommodation_place = ''
location = ''
price = 0

if budget <= 1000:
    accommodation_place = 'Camp'
    if season == 'Summer':
        location = 'Alaska'
        price = budget * 0.65
    elif season == 'Winter':
        location = 'Morocco'
        price = budget * 0.45
elif 1000 < budget <= 3000:
    accommodation_place = 'Hut'
    if season == 'Summer':
        location = 'Alaska'
        price = budget * 0.80
    elif season == 'Winter':
        location = 'Morocco'
        price = budget * 0.60
elif budget > 3000:
    accommodation_place = 'Hotel'
    if season == 'Summer':
        location = 'Alaska'
        price = budget * 0.90
    elif season == 'Winter':
        location = 'Morocco'
        price = budget * 0.90

print(f"{location} - {accommodation_place} - {price:.2f}")
