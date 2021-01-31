lilly_age = int(input())
dishwasher_price = float(input())
toy_price_per_one = int(input())
toys_counter = 0
cash_as_present = 0
taken_money = 0  # Her brother took 1 lev per every even birthday!
even_birthday_counter = 0

for birthday in range(1, lilly_age + 1):
    if not birthday % 2 == 0:
        toys_counter += 1
    else:
        even_birthday_counter += 1
        cash_as_present += 10 * even_birthday_counter
        taken_money += 1

sold_toys_price = toy_price_per_one * toys_counter
saved_money = (cash_as_present + sold_toys_price) - taken_money
diff = abs(dishwasher_price - saved_money)
if dishwasher_price > saved_money:
    print(f"No! {diff:.2f}")
else:
    print(f"Yes! {diff:.2f}")
