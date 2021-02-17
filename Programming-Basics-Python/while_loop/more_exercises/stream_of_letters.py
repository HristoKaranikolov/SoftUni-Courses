next_char = input()

is_c_read = False
is_o_read = False
is_n_read = False
final_char = ''

while next_char != 'End':
    if next_char == 'c':
        if is_c_read:
            final_char += next_char
        else:
            is_c_read = True
    elif next_char == 'o':
        if is_o_read:
            final_char += next_char
        else:
            is_o_read = True
    elif next_char == 'n':
        if is_n_read:
            final_char += next_char
        else:
            is_n_read = True
    elif next_char.isalpha():
        final_char += next_char
    if is_c_read and is_n_read and is_o_read:
        is_c_read = False
        is_o_read = False
        is_n_read = False

        print(final_char, end='')
        final_char = ' '

    next_char = input()
