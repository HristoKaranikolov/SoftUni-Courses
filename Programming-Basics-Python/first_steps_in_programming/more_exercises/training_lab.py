import math

len_in_meters = float(input())
width_in_meters = float(input())

total_places = 0
if 3 <= width_in_meters <= len_in_meters <= 100:
    width_building_cm = width_in_meters * 100 - 100
    places_width = width_building_cm // 70

    len_building_cm = len_in_meters * 100
    places_len = len_building_cm // 120

    total_places = places_width * places_len - 3

print(math.floor(total_places))
