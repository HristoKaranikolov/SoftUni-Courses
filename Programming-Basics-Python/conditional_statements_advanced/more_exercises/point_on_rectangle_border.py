# Coordinates of the rectangle.
x1 = float(input())
y1 = float(input())
x2 = float(input())
y2 = float(input())

# Coordinates of the searched point.
x = float(input())
y = float(input())

is_point_on_the_border = False

# Conditions for the point to be on the border in any of the sides of the rectangle.
if ((x == x1 or x == x2) and y1 <= y <= y2) or \
   ((y == y1 or y == y2) and x1 <= x <= x2):

    is_point_on_the_border = True

result = ''
if is_point_on_the_border:
    result = 'Border'
else:
    result = 'Inside / Outside'
print(result)
