trip_price = float(input())
puzzles_count = int(input())
barbies_count = int(input())
bears_count = int(input())
minions_count = int(input())
trucks_count = int(input())

puzzle_price = 2.60
barbie_price = 3.00
bear_price = 4.10
minion_price = 8.20
truck_price = 2.00

toys_total_price = puzzles_count * puzzle_price + \
                   barbies_count * barbie_price + \
                   bears_count * bear_price + \
                   minions_count * minion_price + \
                   trucks_count * truck_price

toys_count = puzzles_count + barbies_count + bears_count + \
             minions_count + trucks_count

final_price = toys_total_price

if toys_count >= 50:
    final_price -= final_price * 0.25

shop_rent_price = final_price * 0.1
final_price -= shop_rent_price

if trip_price > final_price:
    needed_money = trip_price - final_price
    print(f"Not enough money! {needed_money:.2f} lv needed.")
else:
    left_money = final_price - trip_price
    print(f"Yes! {left_money:.2f} lv left.")

