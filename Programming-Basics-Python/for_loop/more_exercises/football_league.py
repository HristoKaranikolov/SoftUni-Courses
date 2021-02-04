stadium_capacity = int(input())
num_fans = int(input())

sector_a_fans = 0
sector_b_fans = 0
sector_v_fans = 0
sector_g_fans = 0

for fans in range(num_fans):
    sector_of_stadium = input()
    if sector_of_stadium == 'A':
        sector_a_fans += 1
    elif sector_of_stadium == 'B':
        sector_b_fans += 1
    elif sector_of_stadium == 'V':
        sector_v_fans += 1
    elif sector_of_stadium == 'G':
        sector_g_fans += 1
percentage_a_fans = (sector_a_fans / num_fans) * 100
percentage_b_fans = (sector_b_fans / num_fans) * 100
percentage_v_fans = (sector_v_fans / num_fans) * 100
percentage_g_fans = (sector_g_fans / num_fans) * 100
percentage_fans = (num_fans / stadium_capacity) * 100

print(f'{percentage_a_fans:.2f}%')
print(f'{percentage_b_fans:.2f}%')
print(f'{percentage_v_fans:.2f}%')
print(f'{percentage_g_fans:.2f}%')
print(f'{percentage_fans:.2f}%')
