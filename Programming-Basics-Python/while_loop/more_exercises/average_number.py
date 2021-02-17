number = int(input())

numbers_sum = 0

loop_counter = 0
while number > 0:
    n = int(input())
    loop_counter += 1
    numbers_sum += n
    if loop_counter == number:
        break

average = numbers_sum / loop_counter

print(f'{average:.2f}')
