num_chrysanthemums = int(input())
num_roses = int(input())
num_tulips = int(input())
season = input()
holiday = input()

bought_flowers_sum = num_chrysanthemums + num_tulips + num_roses
price = 0
bouquet_preparation = 2

if season == 'Summer' or season == 'Spring':
    chrysanthemum_price = 2.00
    rose_price = 4.10
    tulip_price = 2.50
    price = num_chrysanthemums * chrysanthemum_price + num_roses * rose_price + num_tulips * tulip_price
    if holiday == 'Y':
        price += (price * 0.15)
    if season == 'Spring' and num_tulips > 7:
        price -= (price * 0.05)
    if bought_flowers_sum > 20:
        price -= (price * 0.20)
elif season == 'Autumn' or season == 'Winter':
    chrysanthemum_price = 3.75
    rose_price = 4.50
    tulip_price = 4.15
    price = num_chrysanthemums * chrysanthemum_price + num_roses * rose_price + num_tulips * tulip_price
    if holiday == 'Y':
        price += (price * 0.15)
    if season == 'Winter' and num_roses >= 10:
        price -= (price * 0.10)
    if bought_flowers_sum > 20:
        price -= (price * 0.20)

bouquet_price = price + bouquet_preparation
print(f'{bouquet_price:.2f}')
