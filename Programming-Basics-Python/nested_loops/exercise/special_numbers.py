divided_num = int(input())
start_range = 1111
end_range = 9999

special_numbers = []
for number in range(start_range, end_range + 1):
    number_as_str = str(number)
    found_special_num = True
    for el in number_as_str:
        try:
            if divided_num % int(el) == 0:
                continue
            else:
                found_special_num = False
                break
        except ZeroDivisionError:
            found_special_num = False

    if found_special_num:
        special_numbers.append(number)

[print(x, end=' ') for x in special_numbers]
