command = input()

prime_numbers_total = 0
non_prime_numbers_total = 0

while command != 'stop':
    number = int(command)
    is_prime = True
    if number < 0:
        print("Number is negative.")
    else:
        for check in range(2, number):
            if number % check == 0:
                is_prime = False
                break
        if is_prime:
            prime_numbers_total += number
        else:
            non_prime_numbers_total += number

    command = input()

print(f"Sum of all prime numbers is: {prime_numbers_total}")
print(f"Sum of all non prime numbers is: {non_prime_numbers_total}")