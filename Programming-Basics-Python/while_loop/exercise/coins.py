change = float(input())
change = int(change * 100)
num_coins = 0

while change > 0:
    if change - 200 >= 0:
        change -= 200
        num_coins += 1
    elif change - 100 >= 0:
        change -= 100
        num_coins += 1
    elif change - 50 >= 0:
        change -= 50
        num_coins += 1
    elif change - 20 >= 0:
        change -= 20
        num_coins += 1
    elif change - 10 >= 0:
        change -= 10
        num_coins += 1
    elif change - 5 >= 0:
        change -= 5
        num_coins += 1
    elif change - 2 >= 0:
        change -= 2
        num_coins += 1
    else:
        change -= 1
        num_coins += 1

print(num_coins)
