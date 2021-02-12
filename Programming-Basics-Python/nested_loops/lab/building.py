floors = int(input())
rooms_per_floor = int(input())

building = []
# for floor in range()


for floor in range(1, floors + 1):
    building.append([])
    room_type = ''
    for room in range(0, rooms_per_floor):
        if floor == floors:
            room_type = 'L'
        elif floor % 2 == 0:
            room_type = 'O'
        else:
            room_type = 'A'

        building[floor - 1].append(f"{room_type}{floor}{room}")

[print(' '.join(x)) for x in reversed(building)]

# number_of_floors = int(input())
# number_of_rooms_per_floor = int(input())
#
#
# apartment_count = 0
# office_counter = 0
#
# for floors in range(number_of_floors, 0, -1):
#     for room in range(0, number_of_rooms_per_floor):
#         if floors == number_of_floors:
#             print(f'L{floors}{room}', end=' ')
#         elif floors % 2 == 0:
#             print(f'O{floors}{room}', end=' ')
#         elif floors % 2 != 0:
#             print(f'A{floors}{room}', end=' ')
#     print()
