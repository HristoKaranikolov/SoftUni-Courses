# Fish tank measurements
length_in_cm = int(input())
width_in_cm = int(input())
height_in_cm = int(input())

percentage = float(input())

fish_tank_volume = length_in_cm * width_in_cm * height_in_cm
volume_in_liters = fish_tank_volume / 1000

percentage_filled = percentage * 0.01

needed_liters_to_be_filled = volume_in_liters * (1 - percentage_filled)
print(needed_liters_to_be_filled)
