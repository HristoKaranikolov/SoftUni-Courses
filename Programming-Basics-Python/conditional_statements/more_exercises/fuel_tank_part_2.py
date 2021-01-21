fuel_type = input()
quantity_fuel = float(input())
club_card = input()

gasoline_price = 2.22
diesel_price = 2.33
gas_price = 0.93

if fuel_type == 'Gas':
    if club_card == 'Yes':
        if 50 >= quantity_fuel > 25:
            load_price_l = 0.93 - 0.08
            load_price_sum = quantity_fuel * load_price_l
            discount = load_price_sum * 10/100
            final_sum = load_price_sum - discount
            print(f'{final_sum:.2f} lv.')
        elif 20 <= quantity_fuel <= 25:
            load_price_l = 0.93 - 0.08
            load_price_sum = quantity_fuel * load_price_l
            discount = load_price_sum * 8 / 100
            final_sum = load_price_sum - discount
            print(f'{final_sum:.2f} lv.')
        elif 1 <= quantity_fuel < 20:
            load_price_l = 0.93 - 0.08
            final_sum = quantity_fuel * load_price_l
            print(f'{final_sum} lv.')
    elif club_card == 'No':
        if 50 >= quantity_fuel > 25:
            load_price = quantity_fuel * 0.93
            discount = load_price * 10/100
            final_sum = load_price - discount
            print(f'{final_sum:.2f} lv.')
        elif 20 <= quantity_fuel <= 25:
            load_price_sum = quantity_fuel * 0.93
            discount = load_price_sum * 8 / 100
            final_sum = load_price_sum - discount
            print(f'{final_sum:.2f} lv.')
        elif 1 <= quantity_fuel < 20:
            load_price_sum = quantity_fuel * 0.93
            print(f'{load_price_sum} lv.')

elif fuel_type == 'Gasoline':
    if club_card == 'Yes':
        if 50 >= quantity_fuel > 25:
            load_price_l = 2.22 - 0.18
            load_price_sum = quantity_fuel * load_price_l
            discount = load_price_sum * 10 / 100
            final_sum = load_price_sum - discount
            print(f'{final_sum:.2f} lv.')
        elif 20 <= quantity_fuel <= 25:
            load_price_l = 2.22 - 0.18
            load_price_sum = quantity_fuel * load_price_l
            discount = load_price_sum * 8 / 100
            final_sum = load_price_sum - discount
            print(f'{final_sum:.2f} lv.')
        elif 1 <= quantity_fuel < 20:
            load_price_l = 2.22 - 0.18
            load_price_sum = quantity_fuel * load_price_l
            print(f'{load_price_sum} lv.')
    elif club_card == 'No':
        if 50 >= quantity_fuel > 25:
            load_price = quantity_fuel * 2.22
            discount = load_price * 10/100
            final_sum = load_price - discount
            print(f'{final_sum:.2f} lv.')
        elif 20 <= quantity_fuel <= 25:
            load_price_sum = quantity_fuel * 2.22
            discount = load_price_sum * 8 / 100
            final_sum = load_price_sum - discount
            print(f'{final_sum:.2f} lv.')
        elif 1 <= quantity_fuel < 20:
            load_price_sum = quantity_fuel * 2.22
            print(f'{load_price_sum} lv.')

elif fuel_type == 'Diesel':
    if club_card == 'Yes':
        if 50 >= quantity_fuel > 25:
            load_price_l = 2.33 - 0.12
            load_price_sum = quantity_fuel * load_price_l
            discount = load_price_sum * 10 / 100
            final_sum = load_price_sum - discount
            print(f'{final_sum:.2f} lv.')
        elif 20 <= quantity_fuel <= 25:
            load_price_l = 2.33 - 0.12
            load_price_sum = quantity_fuel * load_price_l
            discount = load_price_sum * 8 / 100
            final_sum = load_price_sum - discount
            print(f'{final_sum:.2f} lv.')
        elif 1 <= quantity_fuel < 20:
            load_price_l = 2.33 - 0.12
            load_price_sum = quantity_fuel * load_price_l
            print(f'{load_price_sum} lv.')
    elif club_card == 'No':
        if 50 >= quantity_fuel > 25:
            load_price = quantity_fuel * 2.33
            discount = load_price * 10/100
            final_sum = load_price - discount
            print(f'{final_sum:.2f} lv.')
        elif 20 <= quantity_fuel <= 25:
            load_price_sum = quantity_fuel * 2.33
            discount = load_price_sum * 8 / 100
            final_sum = load_price_sum - discount
            print(f'{final_sum:.2f} lv.')
        elif 1 <= quantity_fuel < 20:
            load_price_sum = quantity_fuel * 2.33
            print(f'{load_price_sum} lv.')
