first_limit = int(input())
second_limit = int(input())
third_limit = int(input())

code_nums = []

prime_numbers = 2, 3, 5, 7
for num_1 in range(1, first_limit + 1):
    for num_2 in range(1, second_limit + 1):
        for num_3 in range(1, third_limit + 1):
            if (num_1 % 2 == 0 and num_3 % 2 == 0) and 2 <= num_2 <= 7 and num_2 in prime_numbers:
                special_code = f"{num_1} {num_2} {num_3}"
                code_nums.append(special_code)

print('\n'.join(code_nums))
