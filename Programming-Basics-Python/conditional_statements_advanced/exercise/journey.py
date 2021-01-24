budget = float(input())
season = input()

valid_seasons = 'summer', 'winter'

bulgaria_prices = {'summer': budget * 0.3,
                   'winter': budget * 0.7}

balkans_prices = {'summer': budget * 0.4,
                  'winter': budget * 0.8}

europe_prices = {'summer': budget * 0.9,
                 'winter': budget * 0.9}


possible_rest_types = {'summer': 'Camp',
                       'winter': 'Hotel'}
price = 0
rest_type = ''
destination = ''
if season in valid_seasons:
    rest_type = possible_rest_types[season]
    if budget <= 100:
        price = bulgaria_prices[season]
        destination = 'Bulgaria'
    elif 100 < budget <= 1000:
        price = balkans_prices[season]
        destination = 'Balkans'
    else:
        rest_type = 'Hotel'
        price = europe_prices[season]
        destination = 'Europe'

print(f"Somewhere in {destination}", end='\n'
      f"{rest_type} - {price:.2f}")
