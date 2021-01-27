budget = float(input())
category = input()
num_people = int(input())

vip = 499.99
normal = 249.99
ticket_price = 0.0

if 1 <= num_people <= 4:
    transport_tax = budget * 0.75
    budget -= transport_tax
    if category == 'Normal':
        ticket_price = normal * num_people
    elif category == 'VIP':
        ticket_price = vip * num_people
elif 5 <= num_people <= 9:
    transport_tax = budget * 0.60
    budget -= transport_tax
    if category == 'Normal':
        ticket_price = normal * num_people
    elif category == 'VIP':
        ticket_price = vip * num_people
elif 10 <= num_people <= 24:
    transport_tax = budget * 0.50
    budget -= transport_tax
    if category == 'Normal':
        ticket_price = normal * num_people
    elif category == 'VIP':
        ticket_price = vip * num_people
elif 25 <= num_people <= 49:
    transport_tax = budget * 0.40
    budget -= transport_tax
    if category == 'Normal':
        ticket_price = normal * num_people
    elif category == 'VIP':
        ticket_price = vip * num_people
elif num_people > 50:
    transport_tax = budget * 0.25
    budget -= transport_tax
    if category == 'Normal':
        ticket_price = normal * num_people
    elif category == 'VIP':
        ticket_price = vip * num_people
difference = abs(budget - ticket_price)

if ticket_price < budget:
    print(f"Yes! You have {difference:.2f} leva left.")
else:
    print(f"Not enough money! You need {difference:.2f} leva.")
