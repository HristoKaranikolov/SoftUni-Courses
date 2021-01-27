season = input()
group_type = input()
students_num = int(input())
overnights_num = int(input())

price_per_student = 0
sport_type = ''
final_price = 0

if season == 'Winter':
    if group_type == 'boys':
        price_per_student = 9.60
        sport_type = 'Judo'
    elif group_type == 'girls':
        price_per_student = 9.60
        sport_type = 'Gymnastics'
    elif group_type == 'mixed':
        price_per_student = 10.00
        sport_type = 'Ski'
elif season == 'Spring':
    if group_type == 'boys':
        price_per_student = 7.20
        sport_type = 'Tennis'
    elif group_type == 'girls':
        price_per_student = 7.20
        sport_type = 'Athletics'
    elif group_type == 'mixed':
        price_per_student = 9.50
        sport_type = 'Cycling'
if season == 'Summer':
    if group_type == 'boys':
        price_per_student = 15.00
        sport_type = 'Football'
    elif group_type == 'girls':
        price_per_student = 15.00
        sport_type = 'Volleyball'
    elif group_type == 'mixed':
        price_per_student = 20.00
        sport_type = 'Swimming'

final_price = price_per_student * students_num * overnights_num

if students_num >= 50:
    discount = final_price * 0.50
    final_price -= discount
elif 20 <= students_num < 50:
    discount = final_price * 0.15
    final_price -= discount
elif 10 <= students_num < 20:
    discount = final_price * 0.05
    final_price -= discount

print(f"{sport_type} {final_price:.2f} lv.")
