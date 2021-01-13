def calc_product_total_price(weight, price_per_kg):
    res = weight * price_per_kg
    return res


mackerel_price_kg = float(input())
sprat_price_kg = float(input())
bonito_kg = float(input())
scad_kg = float(input())
mussels_kg = float(input())

bonito_price_kg = (mackerel_price_kg * 60 / 100) + mackerel_price_kg
scad_price_kg = (sprat_price_kg * 80 / 100) + sprat_price_kg
mussels_price_kg = 7.50

bonito_total_price = calc_product_total_price(bonito_kg, bonito_price_kg)
scad_total_price = calc_product_total_price(scad_kg, scad_price_kg)
mussels_total_price = calc_product_total_price(mussels_kg, mussels_price_kg)

total_cost = bonito_total_price + scad_total_price + mussels_total_price
print(f"{total_cost:.2f}")
