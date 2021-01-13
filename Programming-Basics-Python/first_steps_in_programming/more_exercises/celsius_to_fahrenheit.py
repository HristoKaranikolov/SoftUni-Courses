def convert_celsius_to_fahrenheit(degrees_num):
    result = (degrees_num * 1.8) + 32
    return f"{result:.2f}"


degrees = float(input())

print(convert_celsius_to_fahrenheit(degrees))