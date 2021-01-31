tournaments_count = int(input())
points = int(input())

stages_and_points = {"W": 2000,
                     "F": 1200,
                     "SF": 720}
won_points = 0
won_tournaments = 0
for tournament in range(tournaments_count):
    stage = input()
    if stage == "W":
        won_tournaments += 1

    if stage in stages_and_points:
        won_points += stages_and_points[stage]
        points += stages_and_points[stage]

average_points = int(won_points / tournaments_count)
percentage_won = (won_tournaments / tournaments_count) * 100
print(f"Final points: {points}")
print(f"Average points: {average_points}")
print(f"{percentage_won:.2f}%")
