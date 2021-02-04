pair_nums = int(input())

even_sum = 0
odd_sum = 0
total = 0
difference = 0

for i in range(pair_nums):
    num1 = int(input())
    num2 = int(input())
    total = num1 + num2

    if i % 2 == 0:
        even_sum = total
    else:
        odd_sum = total
if even_sum == odd_sum:
    difference = 0
    print(f"Yes, value={even_sum}")
elif even_sum != odd_sum and pair_nums == 1:
    print(f"Yes, value={even_sum}")
else:
    difference = abs(even_sum - odd_sum)
    print(f"No, maxdiff={difference}")
