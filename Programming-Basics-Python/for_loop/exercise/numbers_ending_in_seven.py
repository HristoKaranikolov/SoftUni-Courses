start_num = 1
end_num = 1000


def finding_nums_ending_in_seven(start, end):
    nums = []
    for num in range(start, end + 1):
        if num % 10 == 7:
            nums.append(num)
    return nums


result = finding_nums_ending_in_seven(start_num, end_num)
[print(x) for x in result]


# for num in range(7, 1001, 10):
#     print(num)
#
# for num in range(1, 1001):
#     if num % 10 == 7:
#         print(num)
