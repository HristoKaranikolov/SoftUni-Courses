letter_1 = input()
letter_2 = input()
exclusive_letter = input()

start_range = ord(letter_1)
end_range = ord(letter_2)
exclusive_letter_ord = ord(exclusive_letter)
combinations = []

for first_ord in range(start_range, end_range + 1):
    if first_ord == exclusive_letter_ord:
        continue
    for second_ord in range(start_range, end_range + 1):
        if second_ord == exclusive_letter_ord:
            continue
        for third_ord in range(start_range, end_range + 1):
            if third_ord == exclusive_letter_ord:
                continue
            combination = chr(first_ord) + chr(second_ord) + chr(third_ord)
            combinations.append(combination)


print(f"{' '.join(combinations)} {len(combinations)}")
