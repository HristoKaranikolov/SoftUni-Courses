days_count = int(input())
hours_per_day = int(input())

total_parking_price = 0
for day in range(1, days_count + 1):
    daily_parking_price = 0
    for hour in range(1, hours_per_day + 1):

        if day % 2 == 0 and not hour % 2 == 0:
            daily_parking_price += 2.50
        elif not day % 2 == 0 and hour % 2 == 0:
            daily_parking_price += 1.25
        else:
            daily_parking_price += 1

    print(f"Day: {day} - {daily_parking_price:.2f} leva")
    total_parking_price += daily_parking_price

print(f"Total: {total_parking_price:.2f} leva")
