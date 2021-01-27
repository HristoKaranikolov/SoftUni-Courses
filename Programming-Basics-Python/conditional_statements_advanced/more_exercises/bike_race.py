jr_cyclist_num = int(input())
sr_cyclist_num = int(input())
race_type = input()

cyclist_sum = jr_cyclist_num + sr_cyclist_num
collected_amount = 0.0

if race_type == 'trail':
    tax_jr = 5.50
    tax_sr = 7.00
    collected_amount = tax_jr * jr_cyclist_num + tax_sr * sr_cyclist_num

elif race_type == 'cross-country':
    tax_jr = 8.00
    tax_sr = 9.50
    collected_amount = tax_jr * jr_cyclist_num + tax_sr * sr_cyclist_num
    if cyclist_sum >= 50:
        tax_jr = 8.00
        tax_sr = 9.50
        tax_amount = (tax_jr * jr_cyclist_num + tax_sr * sr_cyclist_num) * 0.25
        collected_amount = (tax_jr * jr_cyclist_num + tax_sr * sr_cyclist_num) - tax_amount
elif race_type == 'downhill':
    tax_jr = 12.25
    tax_sr = 13.75
    collected_amount = tax_jr * jr_cyclist_num + tax_sr * sr_cyclist_num
elif race_type == 'road':
    tax_jr = 20.00
    tax_sr = 21.50
    collected_amount = tax_jr * jr_cyclist_num + tax_sr * sr_cyclist_num

total_costs = collected_amount * 0.05
donated_amount = collected_amount - total_costs
print(f'{donated_amount:.2f}')
