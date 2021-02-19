start_range = int(input())
end_range = int(input())

valid_license_plates = []
for num_1 in range(start_range, end_range + 1):
    for num_2 in range(start_range, end_range + 1):
        for num_3 in range(start_range, end_range + 1):
            for num_4 in range(start_range, end_range + 1):
                middle_digits_sum = num_2 + num_3
                if num_1 > num_4:
                    if (num_1 % 2 == 0 and not num_4 % 2 == 0) \
                            or (not num_1 % 2 == 0 and num_4 % 2 == 0):
                        if middle_digits_sum % 2 == 0 and num_1 > num_4:

                            license_plate = f"{num_1}{num_2}{num_3}{num_4}"
                            valid_license_plates.append(license_plate)


print(' '.join(valid_license_plates))
