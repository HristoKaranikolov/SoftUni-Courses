from math import pi

figure_type = input()

area = 0

if figure_type == 'square':
    num = float(input())
    area = num * num

elif figure_type == 'rectangle':
    num_1 = float(input())
    num_2 = float(input())
    area = num_1 * num_2

elif figure_type == 'circle':
    num = float(input())
    area = num * num * pi

elif figure_type == 'triangle':
    num_1 = float(input())
    num_2 = float(input())
    area = (num_1 * num_2) / 2

print(f"{area:.3f}")
