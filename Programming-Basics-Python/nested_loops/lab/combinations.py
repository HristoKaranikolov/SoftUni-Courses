number = int(input())

combinations_counter = 0
for i in range(0, number + 1):
    for j in range(number + 1):
        for k in range(number + 1):
            if i + j + k == number:
                combinations_counter += 1

print(combinations_counter)