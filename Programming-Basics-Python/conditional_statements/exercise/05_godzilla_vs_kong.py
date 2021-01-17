budget = float(input())
extras_count = int(input())
clothing_per_extra_price = float(input())

decor_price = budget * 0.1
clothing_price = clothing_per_extra_price * extras_count
if extras_count > 150:
    discount = 0.1
    clothing_price -= clothing_price * discount

total_price = decor_price + clothing_price


difference = abs(budget - total_price)
if total_price > budget:
    print("Not enough money!", end='\n'
          f"Wingard needs {difference:.2f} leva more.")
else:
    print("Action!", end='\n'
          f"Wingard starts filming with {difference:.2f} leva left.")
