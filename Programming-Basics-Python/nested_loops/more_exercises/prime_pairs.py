def check_if_num_is_prime(num):
    if num > 1:
        for i in range(2, num):
            if num % i == 0:
                return False
        return True


first_start_range = int(input())
second_start_range = int(input())
first_additional = int(input())
second_additional = int(input())

first_end_range = first_start_range + first_additional
second_end_range = second_start_range + second_additional

res = []
for num_1 in range(first_start_range, first_end_range + 1):
    if check_if_num_is_prime(num_1):
        for num_2 in range(second_start_range, second_end_range + 1):
            if check_if_num_is_prime(num_2):
                res.append(f"{num_1}{num_2}")

print('\n'.join(res))
