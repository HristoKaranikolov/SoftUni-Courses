import math

num_magnolia = int(input())
num_hyacinths = int(input())
num_roses = int(input())
num_cacti = int(input())
gift_price = float(input())

magnolias = 3.25
hyacinths = 4
roses = 3.50
cacti = 8

sum_flowers = magnolias * num_magnolia + hyacinths * num_hyacinths + roses * num_roses + cacti * num_cacti
flower_tax = sum_flowers * 5/100
final_price = sum_flowers - flower_tax

if final_price < gift_price:
    needed_money = math.ceil(gift_price - final_price)
    print(f'She will have to borrow {needed_money} leva.')
else:
    left_money = math.floor(final_price - gift_price)
    print(f'She is left with {left_money} leva.')

