chicken_menu_count = int(input())
fish_menu_count = int(input())
vegetarian_menu_count = int(input())

# Preferential prices that the news restaurant offers
chicken_menu_price = 10.35
fish_menu_price = 12.40
vegetarian_menu_price = 8.15

chicken_menu_total_price = chicken_menu_price * chicken_menu_count
fish_menu_total_price = fish_menu_price * fish_menu_count
vegetarian_menu_total_price = vegetarian_menu_price * vegetarian_menu_count

total_menu_price = chicken_menu_total_price + fish_menu_total_price + vegetarian_menu_total_price

dessert_price = total_menu_price * 0.20
delivery_cost = 2.50

final_price = total_menu_price + dessert_price + delivery_cost
print(final_price)