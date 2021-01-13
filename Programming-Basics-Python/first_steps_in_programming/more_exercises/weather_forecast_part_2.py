def show_weather_type(degrees_num):
    res = ''
    if 5.00 <= degrees_num < 12.00:
        res = "Cold"
    elif 12.00 <= degrees_num < 15.00:
        res = "Cool"
    elif 15.00 <= degrees_num < 20.10:
        res = "Mild"
    elif 20.10 <= degrees_num < 26.00:
        res = "Warm"
    elif 26.00 <= degrees_num <= 35.00:
        res = "Hot"
    else:
        res = "unknown"
    return res


degrees = float(input())

print(show_weather_type(degrees))
