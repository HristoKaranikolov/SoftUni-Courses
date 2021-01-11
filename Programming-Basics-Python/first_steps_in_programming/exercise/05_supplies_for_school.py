pen_package_count = int(input())
markers_package_count = int(input())
liters = int(input())  # Liters liquid for desk cleaning
percentage_discount = int(input())

# prices per package
pens_cost = 5.80
markers_cost = 7.20
detergent_cost = 1.20  # price per liter

pens_price = pen_package_count * pens_cost
markers_price = markers_package_count * markers_cost
detergent_price = detergent_cost * liters

total_price = pens_price + markers_price + detergent_price

price_with_discount = total_price - (total_price * (percentage_discount * 0.01))

print(price_with_discount)