number = int(input())

counter = 1
all_is_printed = False
for row in range(1, number + 1):
    for col in range(row):
        print(counter, end=' ')
        counter += 1
        if counter > number:
            all_is_printed = True
            break
    print()
    if all_is_printed:
        break
