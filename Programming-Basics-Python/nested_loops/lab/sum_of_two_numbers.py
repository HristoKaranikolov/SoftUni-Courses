start_num = int(input())
end_num = int(input())
magical_num = int(input())

is_combination_found = False
combinations_counter = 0
for first_num in range(start_num, end_num + 1):
    for second_num in range(start_num, end_num + 1):
        combinations_counter += 1
        if first_num + second_num == magical_num:
            is_combination_found = True
            print(f"Combination N:{combinations_counter} ({first_num} + {second_num} = {magical_num})")
            break

    if is_combination_found:
        break

if not is_combination_found:
    print(f"{combinations_counter} combinations - neither equals {magical_num}")
