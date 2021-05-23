product = input()
city = input()
quantity = float(input())

sofia = {'coffee': 0.50,
         'water': 0.80,
         'beer': 1.20,
         'sweets': 1.45,
         'peanuts': 1.60}

plovdiv = {'coffee': 0.40,
           'water': 0.70,
           'beer': 1.15,
           'sweets': 1.30,
           'peanuts': 1.50}

varna = {'coffee': 0.45,
         'water': 0.70,
         'beer': 1.10,
         'sweets': 1.35,
         'peanuts': 1.55}

price = 0

if city == 'Sofia':
    if product in sofia:
        price = sofia[product]
elif city == 'Plovdiv':
    if product in plovdiv:
        price = plovdiv[product]
elif city == 'Varna':
    if product in varna:
        price = varna[product]

print(price * quantity)
