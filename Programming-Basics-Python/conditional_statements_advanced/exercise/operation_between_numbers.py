num_1 = int(input())
num_2 = int(input())
operator = input()  # Possible operators - '+', '-', '*', '/', '%'

if num_2 == 0:
    print(f"Cannot divide {num_1} by zero")
    quit()

calc_result = 0
result = ''
if operator == '+' or operator == '*' or operator == '-':
    calc_result = num_1 + num_2
    if operator == '*':
        calc_result = num_1 * num_2
    elif operator == '-':
        calc_result = num_1 - num_2

    even_or_odd = 'odd'
    if calc_result % 2 == 0:
        even_or_odd = 'even'

    result = f'{num_1} {operator} {num_2} = {calc_result} - {even_or_odd}'

elif operator == '/':
    calc_result = num_1 / num_2
    result = f"{num_1} / {num_2} = {calc_result:.2f}"

elif operator == '%':
    calc_result = num_1 % num_2
    result = f"{num_1} % {num_2} = {calc_result}"

print(result)
