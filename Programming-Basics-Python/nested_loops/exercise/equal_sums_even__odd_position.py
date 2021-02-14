first_num = int(input())
second_num = int(input())

special_numbers = []
for num in range(first_num, second_num + 1):
    num_string = str(num)
    odd_sum = 0
    even_sum = 0
    for index, el in enumerate(num_string):
        if index % 2 == 0:
            even_sum += int(el)
        else:
            odd_sum += int(el)

    if odd_sum == even_sum:
        special_numbers.append(num)

[print(x, end=' ') for x in special_numbers]
