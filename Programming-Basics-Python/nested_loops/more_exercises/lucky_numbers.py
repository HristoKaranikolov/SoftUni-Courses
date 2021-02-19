divider = int(input())

''' The number should be with four digits (etc.1221), in which every digit should be in range 1 - 9 inclusive.
A number is happy, if the sum of the first two digits(12) is equal of the sum of the last two digits(21)
 and the sum of the first two digits(12), divided by the divider, returns a digit without remainder.'''

happy_numbers = []
for num_1 in range(1, 10):
    for num_2 in range(1, 10):
        for num_3 in range(1, 10):
            for num_4 in range(1, 10):
                first_sum = num_1 + num_2
                second_sum = num_3 + num_4
                if first_sum == second_sum and divider % first_sum == 0:
                    number = f"{num_1}{num_2}{num_3}{num_4}"
                    happy_numbers.append(number)

print(' '.join(happy_numbers))
