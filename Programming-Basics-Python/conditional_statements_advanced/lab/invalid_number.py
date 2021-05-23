number = int(input())

is_valid_num = (100 <= number <= 200) or number == 0

if not is_valid_num:
    print('invalid')
