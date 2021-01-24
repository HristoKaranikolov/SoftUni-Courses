group_budget = int(input())
season = input()
fishermen_count = int(input())

ship_price_thru_seasons = {"Spring": 3000,
                           "Summer": 4200,
                           "Autumn": 4200,
                           "Winter": 2600}

ship_price = 0
if season in ship_price_thru_seasons:
    ship_price = ship_price_thru_seasons[season]
    if 0 < fishermen_count <= 6:
        ship_price *= 0.90
    elif 7 <= fishermen_count <= 11:
        ship_price *= 0.85
    else:
        ship_price *= 0.75

    if fishermen_count % 2 == 0 and not season == "Autumn":
        ship_price *= 0.95

diff = abs(group_budget - ship_price)
if group_budget < ship_price:
    print(f"Not enough money! You need {diff:.2f} leva.")
else:
    print(f"Yes! You have {diff:.2f} leva left.")
