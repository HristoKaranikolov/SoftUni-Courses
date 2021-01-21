holidays = int(input())
holidays_play = holidays * 127

working_days = 365 - holidays
working_days_play = working_days * 63

total_days_play = working_days_play + holidays_play

diff = abs(total_days_play - 30000)
hours = diff // 60
minutes = diff % 60
result = ''
if total_days_play > 30000:
    result = "Tom will run away" + "\n" +\
             f"{hours} hours and {minutes} minutes more for play"
else:
    result = "Tom sleeps well" + "\n" +\
             f"{hours} hours and {minutes} minutes less for play"

print(result)
