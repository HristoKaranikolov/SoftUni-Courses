world_record_in_seconds = float(input())
track_length = float(input())
time_per_meter = float(input())  # The time is in seconds.
water_resistance = 12.5  # The water resistance is per 15 meters.

delay_from_resistance = (track_length // 15) * water_resistance
swimmer_time = track_length * time_per_meter + delay_from_resistance

if swimmer_time < world_record_in_seconds:
    print(f"Yes, he succeeded! The new world record is {swimmer_time:.2f} seconds.")
else:
    left_seconds = swimmer_time - world_record_in_seconds
    print(f"No, he failed! He was {left_seconds:.2f} seconds slower.")
