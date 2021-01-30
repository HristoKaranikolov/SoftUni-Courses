import sys
import time

start_time = time.time()

numbers_count = int(input())
max_num = - sys.maxsize
min_num = sys.maxsize

for i in range(numbers_count):
    number = int(input())
    if number > max_num:
        max_num = number
    if number < min_num:
        min_num = number

print(f'Max number: {max_num}')
print(f'Min number: {min_num}')

end_time = time.time()
print(end_time - start_time)

# start_time = time.time()
#
# numbers_count = int(input())
# max_num = - sys.maxsize
# min_num = sys.maxsize
#
# nums = []
# for i in range(numbers_count):
#     number = int(input())
#     nums.append(number)
#
# sorted_nums = sorted(nums)
#
# print(f'Max number: {sorted_nums[-1]}')
# print(f'Min number: {sorted_nums[0]}')
#
#
# end_time = time.time()
# print(end_time - start_time)
