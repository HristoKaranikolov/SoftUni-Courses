start_range = int(input())
end_range = int(input())
magical_num = int(input())

counter = 0
combination_found = False
result = ''
for num_1 in range(start_range, end_range + 1):
    for num_2 in range(start_range, end_range + 1):
        counter += 1
        if num_1 + num_2 == magical_num:
            result = f"Combination N:{counter} ({num_1} + {num_2} = {magical_num})"
            combination_found = True
            break
    if combination_found:
        break

if combination_found:
    print(result)
else:
    print(f"{counter} combinations - neither equals {magical_num}")