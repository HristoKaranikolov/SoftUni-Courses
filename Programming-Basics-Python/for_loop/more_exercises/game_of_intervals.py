game_moves = int(input())

count_nums_0_to_9 = 0.0
count_nums_10_to_19 = 0.0
count_nums_20_to_29 = 0.0
count_nums_30_to_39 = 0.0
count_nums_40_to_50 = 0.0
count_invalid_nums = 0.0
total_result = 0

for moves in range(game_moves):
    number = int(input())
    if 0 <= number <= 9:
        count_nums_0_to_9 += 1
        total_result += (number * 0.2)
    elif 10 <= number <= 19:
        count_nums_10_to_19 += 1
        total_result += (number * 0.3)
    elif 20 <= number <= 29:
        count_nums_20_to_29 += 1
        total_result += (number * 0.4)
    elif 30 <= number <= 39:
        count_nums_30_to_39 += 1
        total_result += 50
    elif 40 <= number <= 50:
        count_nums_40_to_50 += 1
        total_result += 100
    else:
        count_invalid_nums += 1
        total_result /= 2

percentage_nums_0_to_9 = (count_nums_0_to_9 / game_moves) * 100
percentage_nums_10_to_19 = (count_nums_10_to_19 / game_moves) * 100
percentage_nums_20_to_29 = (count_nums_20_to_29 / game_moves) * 100
percentage_nums_30_to_39 = (count_nums_30_to_39 / game_moves) * 100
percentage_nums_40_to_50 = (count_nums_40_to_50 / game_moves) * 100
percentage_invalid_nums = (count_invalid_nums / game_moves) * 100

print(f'{total_result:.2f}')
print(f'From 0 to 9: {percentage_nums_0_to_9:.2f}%')
print(f'From 10 to 19: {percentage_nums_10_to_19:.2f}%')
print(f'From 20 to 29: {percentage_nums_20_to_29:.2f}%')
print(f'From 30 to 39: {percentage_nums_30_to_39:.2f}%')
print(f'From 40 to 50: {percentage_nums_40_to_50:.2f}%')
print(f'Invalid numbers: {percentage_invalid_nums:.2f}%')
