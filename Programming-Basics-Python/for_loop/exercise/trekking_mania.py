climbers_group_count = int(input())

total_members = 0
musala_climbers_count = 0
monblan_climbers_count = 0
kilimanjaro_climbers_count = 0
k_2_climbers_count = 0
everest_climbers_count = 0

for i in range(climbers_group_count):
    members_count = int(input())
    total_members += members_count
    if members_count <= 5:
        musala_climbers_count += members_count
    elif 6 <= members_count <= 12:
        monblan_climbers_count += members_count
    elif 13 <= members_count <= 25:
        kilimanjaro_climbers_count += members_count
    elif 26 <= members_count <= 40:
        k_2_climbers_count += members_count
    elif members_count >= 41:
        everest_climbers_count += members_count

print(f"{(musala_climbers_count / total_members) * 100:.2f}%")
print(f"{(monblan_climbers_count / total_members) * 100:.2f}%")
print(f"{(kilimanjaro_climbers_count / total_members) * 100:.2f}%")
print(f"{(k_2_climbers_count / total_members) * 100:.2f}%")
print(f"{(everest_climbers_count / total_members) * 100:.2f}%")
