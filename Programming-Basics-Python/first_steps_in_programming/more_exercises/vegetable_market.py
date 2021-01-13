def calc_price_in_euro(price):
    return price / 1.94


def calc_total_price_for_product(price, weight):
    res = price * weight
    return res


vegies_price_per_kg = float(input())
fruits_price_per_kg = float(input())
vegies_total_kg = int(input())
fruits_total_kg = int(input())

vegetables_total_cost = calc_total_price_for_product(vegies_price_per_kg, vegies_total_kg)
fruits_total_cost = calc_total_price_for_product(fruits_price_per_kg, fruits_total_kg)

vegies_price_in_euro = calc_price_in_euro(vegetables_total_cost)
fruits_price_in_euro = calc_price_in_euro(fruits_total_cost)
result = vegies_price_in_euro + fruits_price_in_euro
print(f"{result:.2f}")

# veggies_price_kg = float(input())
# fruits_price_kg = float(input())
# veggies_kg = int(input())
# fruits_kg = int(input())
#
# veggies_price = veggies_price_kg * veggies_kg
# fruits_price = fruits_price_kg * fruits_kg
# sum = fruits_price + veggies_price
# euro = sum / 1.94
# print(f"{euro:.2f}")
