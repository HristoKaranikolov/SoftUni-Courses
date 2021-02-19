# num_1 - upper limit of first number:
# num_2 - upper limit of second number:
# num_3 - upper limit of third number:

num_1 = int(input())
num_2 = int(input())
num_3 = int(input())

for first_number in range(1, num_1 + 1):
    if first_number % 2 == 0:
        for second_number in range(2, num_2 + 1):
            if second_number == 2 or second_number == 3 or second_number == 5 or second_number == 7:
                for third_number in range(1, num_3 + 1):
                    if third_number % 2 == 0:
                        print(f"{first_number} {second_number} {third_number}", end='')
                        print()
