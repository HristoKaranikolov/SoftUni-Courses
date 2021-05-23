hour = int(input())
day = input()

result = ''
if hour not in range(10, 19) or day == 'Sunday':
    result = 'closed'
else:
    result = 'open'

print(result)
