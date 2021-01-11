from math import floor

pages_count = int(input())
pages_per_hour = int(input())
days = int(input())  # The days that the book must be read!

time_to_read = pages_count / pages_per_hour
pages_per_day = time_to_read / days

print(floor(pages_per_day))
