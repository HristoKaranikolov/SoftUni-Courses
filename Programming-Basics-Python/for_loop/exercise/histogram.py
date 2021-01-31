numbers_counter = int(input())

first_range = []
second_range = []
third_range = []
fourth_range = []
fifth_range = []

for i in range(numbers_counter):
    number = int(input())
    if number < 200:
        first_range.append(number)
    elif 200 <= number <= 399:
        second_range.append(number)
    elif 400 <= number <= 599:
        third_range.append(number)
    elif 600 <= number <= 799:
        fourth_range.append(number)
    elif number >= 800:
        fifth_range.append(number)

first_range_result = (len(first_range) / numbers_counter) * 100
second_range_result = (len(second_range) / numbers_counter) * 100
third_range_result = (len(third_range) / numbers_counter) * 100
fourth_range_result = (len(fourth_range) / numbers_counter) * 100
fifth_range_result = (len(fifth_range) / numbers_counter) * 100

print(f"{first_range_result:.2f}%")
print(f"{second_range_result:.2f}%")
print(f"{third_range_result:.2f}%")
print(f"{fourth_range_result:.2f}%")
print(f"{fifth_range_result:.2f}%")
