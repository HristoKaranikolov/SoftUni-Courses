searched_number = int(input())
potential_numbers = []

for num_1 in range(1, 10):
    for num_2 in range(1, 10):
        for num_3 in range(1, 10):
            for num_4 in range(1, 10):
                if num_1 < num_2 and num_3 > num_4:
                    if (num_1 * num_2) + (num_3 * num_4) == searched_number:
                        number = f"{num_1}{num_2}{num_3}{num_4}"
                        potential_numbers.append(number)

if potential_numbers:
    if len(potential_numbers) < 4:
        print(' '.join(potential_numbers))
        print('No!')
    else:
        print(' '.join(potential_numbers))
        print(f"Password: {potential_numbers[3]}")

else:
    print("No!")
