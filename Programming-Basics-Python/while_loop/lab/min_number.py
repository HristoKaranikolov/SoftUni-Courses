command = input()
numbers = []

while not command == 'Stop':
    num = int(command)
    numbers.append(num)

    command = input()

min_num = min(numbers)
print(min_num)
