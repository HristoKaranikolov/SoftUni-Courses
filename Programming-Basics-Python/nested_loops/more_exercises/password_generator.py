number_limit = int(input())
letter_limit = int(input())

letter_start_range = ord('a')
letter_end_range = letter_start_range + letter_limit


passwords_list = []
for symbol_1 in range(1, number_limit):
    for symbol_2 in range(1, number_limit):
        for symbol_3 in range(letter_start_range, letter_end_range):
            for symbol_4 in range(letter_start_range, letter_end_range):
                for symbol_5 in range(1, number_limit + 1):
                    if symbol_5 > symbol_1 and symbol_5 > symbol_2:
                        password = f"{symbol_1}{symbol_2}{chr(symbol_3)}{chr(symbol_4)}{symbol_5}"
                        passwords_list.append(password)

print(' '.join(passwords_list))
