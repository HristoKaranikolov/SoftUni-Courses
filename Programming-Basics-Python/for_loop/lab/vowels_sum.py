text = input()

letters_and_values = {"a": 1,
                      "e": 2,
                      "i": 3,
                      "o": 4,
                      "u": 5}
total_sum = 0
for i in text:
    if i in letters_and_values:
        total_sum += letters_and_values[i]
print(total_sum)