heritage_money = float(input())
final_year = int(input())

odd_year = 0
even_year = 0
ivan_age = 18

for year in range(1800, final_year + 1):
    if year % 2 == 0:
        heritage_money -= 12000
    else:
        heritage_money -= 12000 + 50 * ivan_age
    ivan_age += 1

if heritage_money >= 0:

    print(f"Yes! He will live a carefree life and will have {heritage_money:.2f} dollars left.")
else:

    print(f"He will need {abs(heritage_money):.2f} dollars to survive.")

