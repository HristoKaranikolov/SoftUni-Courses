def calc_trapezoid_area(side_1, side_2, height_num):
    area = (side_1 + side_2) * height_num / 2
    return f"{area:.2f}"


side_a = float(input())
side_b = float(input())
height = float(input())

print(calc_trapezoid_area(side_a, side_b, height))
