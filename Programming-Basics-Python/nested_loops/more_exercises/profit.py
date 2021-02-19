counter_1_lev_coins = int(input())
counter_2_lev_coins = int(input())
counter_5_lev_banknote = int(input())
cash_sum = int(input())

for coin_1 in range(counter_1_lev_coins + 1):
    for coin_2 in range(counter_2_lev_coins + 1):
        for banknote in range(counter_5_lev_banknote + 1):
            if coin_1 * 1 + coin_2 * 2 + banknote * 5 == cash_sum:
                print(f"{coin_1} * 1 lv. + {coin_2} * 2 lv. + {banknote} * 5 lv. = {cash_sum} lv.")
