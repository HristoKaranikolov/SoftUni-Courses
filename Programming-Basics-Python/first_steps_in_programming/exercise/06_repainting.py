needed_nylon = int(input())
needed_paint = int(input())
paint_thinner_quantity = int(input())
hours = int(input())  # Hours, that painters need to finish the painting

# material prices
nylon_price_per_meter = 1.50
paint_price_per_liter = 14.50
paint_thinner_price_per_liter = 5.00

nylon_price = (needed_nylon + 2) * nylon_price_per_meter
paint_price = (needed_paint + (needed_paint * 0.1)) * paint_price_per_liter
paint_thinner_price = paint_thinner_quantity * paint_thinner_price_per_liter
sack_price = 0.40

total_price = nylon_price + paint_price + paint_thinner_price + sack_price
workers_salary = (total_price * 0.3) * hours

amount_needed = total_price + workers_salary
print(amount_needed)
