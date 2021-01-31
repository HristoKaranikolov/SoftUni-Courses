import sys

number_counter = int(input())
nums_list = []

for i in range(number_counter):
    num = int(input())
    nums_list.append(num)

max_num = max(nums_list)
total_sum = sum(nums_list) - max_num
result = ''
if total_sum == max_num:
    result = "Yes" + '\n' + f"Sum = {total_sum}"
else:
    diff = abs(max_num - total_sum)
    result = "No" + "\n" + f"Diff = {diff}"

print(result)
