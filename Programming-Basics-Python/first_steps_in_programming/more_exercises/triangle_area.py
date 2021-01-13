def calc_triangle_area(side_num, height_num):
    area = side_num * height_num / 2
    return f"{area:.2f}"


side = float(input())
height = float(input())

print(calc_triangle_area(side, height))