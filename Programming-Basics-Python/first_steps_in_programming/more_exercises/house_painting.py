def calc_area(height, width):
    res = height * width
    return res


wall_height = float(input())
wall_width = float(input())
roof_height = float(input())

window_height = 1.5
window_width = 1.5
entrance_height = 2
entrance_width = 1.2
front_wall_width = wall_height
front_wall_height = wall_height

green_paint_per_sq_meter = 3.4
red_paint_per_sq_meter = 4.3

'''Walls calculations'''

side_wall_area = calc_area(wall_height, wall_width)
front_wall_area = calc_area(front_wall_height, front_wall_width)
back_wall_area = front_wall_area

entrance_area = calc_area(entrance_height, entrance_width)
window_area = calc_area(window_height, window_width)

two_side_walls_area = side_wall_area * 2 - window_area * 2
front_and_back_walls_area = 2 * front_wall_area - entrance_area
total_area = two_side_walls_area + front_and_back_walls_area

green_paint_liters = total_area / green_paint_per_sq_meter

'''Roof calculations'''
roof_width = wall_height
roof_triangles_area = 2 * (calc_area(roof_height, roof_width) / 2)
roof_rectangles_area = 2 * (calc_area(wall_height, wall_width))
roof_total_area = roof_triangles_area + roof_rectangles_area

red_paint_liters = roof_total_area / red_paint_per_sq_meter

print(f"{green_paint_liters:.2f}")
print(f"{red_paint_liters:.2f}")


# x = float(input())
# y = float(input())
# h = float(input())
#
# # Walls
#
# side_wall = x * y
# window = 1.5 * 1.5
# two_sides = (2 * side_wall) - (2 * window)
# back_wall = x * x
# entrance = 1.2 * 2
#
# back_front_sum = (2 * back_wall) - entrance
#
# area_sum = two_sides + back_front_sum
#
# green_paint = area_sum / 3.4
#
# print(f'{green_paint:.2f}')
#
# # Roof
#
# roof_rectangles = 2 * (x * y)
# roof_triangles = 2 * (x * h / 2)
# roof_area_sum = roof_triangles + roof_rectangles
#
# red_paint = roof_area_sum / 4.3
# print(f'{red_paint:.2f}')
