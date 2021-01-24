projection_type = input()
rows = int(input())
columns = int(input())

premiere_projection = 12.00
normal_projection = 7.50
discount_projection = 5.00

ticket_income = 0
cinema_capacity = rows * columns
if projection_type == 'Premiere':
    ticket_income = premiere_projection * cinema_capacity
elif projection_type == 'Normal':
    ticket_income = normal_projection * cinema_capacity
elif projection_type == 'Discount':
    ticket_income = discount_projection * cinema_capacity

print(f'{ticket_income:.2f} leva')
