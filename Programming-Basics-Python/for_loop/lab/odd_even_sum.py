number_counter = int(input())

odd_sum = 0
even_sum = 0
for i in range(1, number_counter + 1):
    num = int(input())

    if i % 2 == 0:
        odd_sum += num
    else:
        even_sum += num

diff = abs(odd_sum - even_sum)
if odd_sum == even_sum:
    print('Yes', end='\n'
          f'Sum = {even_sum}')
else:
    print('No', end='\n'
          f'Diff = {diff}')
