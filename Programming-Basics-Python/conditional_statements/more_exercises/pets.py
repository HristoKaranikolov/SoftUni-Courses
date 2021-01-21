import math


num_days = int(input())
food_kg = int(input())
daily_dog_food_kg = float(input())
daily_cat_food_kg = float(input())
daily_turtle_food_gr = float(input())

dog_food = num_days * daily_dog_food_kg
cat_food = num_days * daily_cat_food_kg
turtle_food = num_days * (daily_turtle_food_gr/1000)

sum_food_kg = dog_food + cat_food + turtle_food

if sum_food_kg <= food_kg:
    left_food = math.floor(food_kg - sum_food_kg)
    print(f'{left_food} kilos of food left.')
else:
    needed_food = math.ceil(sum_food_kg - food_kg)
    print(f'{needed_food} more kilos of food are needed.')