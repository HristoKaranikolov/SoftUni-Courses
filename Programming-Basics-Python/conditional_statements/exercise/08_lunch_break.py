from math import ceil

series_name = input()
episode_time = int(input())
rest_time = int(input())

lunch_time = rest_time * 1/8
relaxation_time = rest_time * 1/4
left_time = rest_time - lunch_time - relaxation_time

difference = ceil(abs(episode_time - left_time))
if episode_time > left_time:
    print(f"You don't have enough time to watch {series_name}, you need {difference} more minutes.")
else:
    print(f"You have enough time to watch {series_name} and left with {difference} minutes free time.")

