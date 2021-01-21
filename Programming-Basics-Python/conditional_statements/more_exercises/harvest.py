from math import floor, ceil
vine_area = int(input())
grape_per_sq_meter = float(input())
liters_wine_needed = int(input())
workers_count = int(input())

grapes_kg_per_liter = 2.5
grapes_total = vine_area * grape_per_sq_meter
total_wine = (grapes_total * 40 / 100) / grapes_kg_per_liter
wine_per_person = total_wine / workers_count

diff = abs(total_wine - liters_wine_needed)
if total_wine >= liters_wine_needed:
    print(f"Good harvest this year! Total wine: {floor(total_wine)} liters.")
    print(f"{ceil(diff)} liters left -> {ceil(wine_per_person)} liters per person.")
else:
    print(f"It will be a tough winter! More {floor(diff)} liters wine needed.")