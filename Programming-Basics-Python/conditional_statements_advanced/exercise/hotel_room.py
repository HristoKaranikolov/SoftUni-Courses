month = input()
nights_to_stay = int(input())

months_and_prices_per_night = {'May': {'Studio': 50.00,
                                       'Apartment': 65.00},
                               'October': {'Studio': 50.00,
                                           'Apartment': 65.00},
                               'June': {'Studio': 75.20,
                                        'Apartment': 68.70},
                               'September': {'Studio': 75.20,
                                             'Apartment': 68.70},
                               'July': {'Studio': 76.00,
                                        'Apartment': 77.00},
                               'August': {'Studio': 76.00,
                                          'Apartment': 77.00}}

if month in months_and_prices_per_night:
    apartment_price = months_and_prices_per_night[month]['Apartment']
    studio_price = months_and_prices_per_night[month]['Studio']

    if nights_to_stay > 14:
        apartment_price *= 0.90  # Apartment discount
        if month == 'May' or month == 'October':
            studio_price *= 0.70  # Studio discount
        elif month == 'June' or month == 'September':
            studio_price *= 0.80  # Studio discount

    elif 7 < nights_to_stay <= 14:
        if month == 'May' or month == 'October':
            studio_price *= 0.95  # Studio discount

    total_apartment_price = apartment_price * nights_to_stay
    total_studio_price = studio_price * nights_to_stay

    print(f"Apartment: {total_apartment_price:.2f} lv.", end='\n'
          f"Studio: {total_studio_price:.2f} lv.")
