from math import pi


def calc_circle_area(num):
    res = pi * (num ** 2)
    return f"{res:.2f}"


def clac_circle_perimeter(num):
    res = 2 * pi * num
    return f"{res:.2f}"


radius = float(input())

print(calc_circle_area(radius))
print(clac_circle_perimeter(radius))
