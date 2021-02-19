a = int(input())
b = int(input())
max_count_passwords = int(input())

start_range_a = ord("#")
end_range_a = ord('7')

start_range_b = ord('@')
end_range_b = ord("`")
nums_limit_reached = False
password_limit_reached = False
passwords = []

for a_ord in range(start_range_a, end_range_a + 1):
    for b_ord in range(start_range_b, end_range_b + 1):

        for num1 in range(1, a + 1):
            for num2 in range(1, b + 1):

                password = f"{chr(a_ord)}{chr(b_ord)}{num1}{num2}{chr(b_ord)}{chr(a_ord)}"
                passwords.append(password)
                a_ord += 1
                b_ord += 1
                if a_ord > end_range_a:
                    a_ord = start_range_a
                if b_ord > end_range_b:
                    b_ord = start_range_b

                if num1 == a and num2 == b:
                    nums_limit_reached = True
                    break
                if len(passwords) == max_count_passwords:
                    password_limit_reached = True
                    break
            if nums_limit_reached:
                break
            if password_limit_reached:
                break
        if nums_limit_reached:
            break
        if password_limit_reached:
            break
    if nums_limit_reached:
        break
    if password_limit_reached:
        break

print('|'.join(passwords) + "|")
