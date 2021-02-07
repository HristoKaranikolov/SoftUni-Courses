steps_daily_goal = 10000
walked_steps = 0
while walked_steps < steps_daily_goal:
    data = input()
    if data == 'Going home':
        steps_to_home = int(input())
        walked_steps += steps_to_home
        break

    steps = int(data)
    walked_steps += steps

diff = abs(steps_daily_goal - walked_steps)
if walked_steps >= steps_daily_goal:
    print("Goal reached! Good job!")
    print(f"{diff} steps over the goal!")
else:
    print(f"{diff} more steps to reach goal.")
