male_clients = int(input())
female_clients = int(input())
tables_max_count = int(input())

dates = []
for male in range(1, male_clients + 1):
    for female in range(1, female_clients + 1):
        if tables_max_count == 0:
            break
        dates.append(f"({male} <-> {female})")
        tables_max_count -= 1

print(' '.join(dates))
