last_sector = input()  # B-Z
first_sector_seat_count = int(input())
odd_row_seats_count = int(input())
even_row_seat_count = odd_row_seats_count + 2

sector_start = ord("A")
sector_end = ord(last_sector)
seat_start = ord("a")
seat_end = seat_start + odd_row_seats_count

all_places = []
for sector in range(sector_start, sector_end + 1):
    for row in range(1, first_sector_seat_count + 1):
        if row % 2 == 0:
            seat_end = seat_start + even_row_seat_count
        else:
            seat_end = seat_start + odd_row_seats_count

        for seat in range(seat_start, seat_end):
            place = f"{chr(sector)}{row}{chr(seat)}"
            all_places.append(place)

    first_sector_seat_count += 1

print('\n'.join(all_places))
print(len(all_places))
