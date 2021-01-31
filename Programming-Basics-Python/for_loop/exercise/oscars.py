actor_name = input()
academy_points = float(input())
voters_count = int(input())
got_the_role = False

for i in range(voters_count):
    voter_name = input()
    voter_points = float(input())
    total_points = (len(voter_name) * voter_points) / 2
    academy_points += total_points
    if academy_points > 1250.5:
        got_the_role = True
        break

if got_the_role:
    print(f"Congratulations, {actor_name} got a nominee for leading role with {academy_points:.1f}!")
else:
    diff = 1250.5 - academy_points
    print(f"Sorry, {actor_name} you need {diff:.1f} more!")
