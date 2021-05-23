age = float(input())
gender = input()

result = ''
if gender == 'm':
    if age < 16:
        result = 'Master'
    else:
        result = 'Mr.'
elif gender == 'f':
    if age < 16:
        result = 'Miss'
    else:
        result = 'Ms.'

print(result)
