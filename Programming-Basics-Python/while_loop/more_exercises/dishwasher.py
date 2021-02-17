bottles_num = input()

single_bottle = 750
washed_plate = 5
washed_pot = 15

plate_counter = 0
pot_counter = 0
dishwashing_load_count = 0

detergent = int(bottles_num) * 750

plates_num = input()
while plates_num != 'End':
    plates = int(plates_num)
    dishwashing_load_count += 1
    if dishwashing_load_count % 3 == 0:
        detergent -= plates * washed_pot
        pot_counter += plates
    else:
        detergent -= plates * washed_plate
        plate_counter += plates
    if detergent < 0:
        break
    plates_num = input()

difference = abs(detergent)

if detergent >= 0:
    print("Detergent was enough!")
    print(f"{plate_counter} dishes and {pot_counter} pots were washed.")
    print(f"Leftover detergent {difference} ml.")
else:
    print(f"Not enough detergent, {difference} ml. more necessary!")
