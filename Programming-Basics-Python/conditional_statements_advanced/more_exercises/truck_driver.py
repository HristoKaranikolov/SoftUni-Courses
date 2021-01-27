season = input()
km_travelled_monthly = float(input())
season_duration = 4
salary = 0

if km_travelled_monthly <= 5000:
    if season == 'Spring' or season == 'Autumn':
        price_per_km = 0.75
        salary = price_per_km * km_travelled_monthly
    elif season == 'Summer':
        price_per_km = 0.90
        salary = price_per_km * km_travelled_monthly
    elif season == 'Winter':
        price_per_km = 1.05
        salary = price_per_km * km_travelled_monthly
elif 5000 < km_travelled_monthly <= 10000:
    if season == 'Spring' or season == 'Autumn':
        price_per_km = 0.95
        salary = price_per_km * km_travelled_monthly
    elif season == 'Summer':
        price_per_km = 1.10
        salary = price_per_km * km_travelled_monthly
    elif season == 'Winter':
        price_per_km = 1.25
        salary = price_per_km * km_travelled_monthly
elif 10000 < km_travelled_monthly <= 20000:
    if season == 'Spring' or season == 'Autumn':
        price_per_km = 1.45
        salary = price_per_km * km_travelled_monthly
    elif season == 'Summer':
        price_per_km = 1.45
        salary = price_per_km * km_travelled_monthly
    elif season == 'Winter':
        price_per_km = 1.45
        salary = price_per_km * km_travelled_monthly


final_salary = (salary * season_duration) - ((salary * season_duration) * 0.10)

print(f'{final_salary:.2f}')
