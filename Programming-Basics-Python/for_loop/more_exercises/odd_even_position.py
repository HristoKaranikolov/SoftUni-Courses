nums_count = int(input())
list_of_nums = []
for num in range(nums_count):
    number = float(input())
    list_of_nums.append(number)

odd_positions = [num for index, num in enumerate(list_of_nums) if index % 2 == 0]
odd_sum = sum(odd_positions)
min_odd_num = 'No'
max_odd_num = 'No'
if odd_positions:
    min_odd_num = f"{min(odd_positions):.2f}"
    max_odd_num = f"{max(odd_positions):.2f}"

even_positions = [num for index, num in enumerate(list_of_nums) if not index % 2 == 0]
even_sum = sum(even_positions)
min_even_num = 'No'
max_even_num = 'No'
if even_positions:
    min_even_num = f"{min(even_positions):.2f}"
    max_even_num = f"{max(even_positions):.2f}"

print(f"OddSum={odd_sum:.2f},")
print(f"OddMin={min_odd_num},")
print(f"OddMax={max_odd_num},")
print(f"EvenSum={even_sum:.2f},")
print(f"EvenMin={min_even_num},")
print(f"EvenMax={max_even_num}")
