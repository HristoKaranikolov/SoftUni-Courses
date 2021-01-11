annual_basketball_tax = int(input())

shoes = annual_basketball_tax - (annual_basketball_tax * 0.4)
clothes = shoes - (shoes * 0.2)
ball = clothes * 0.25
accessories = ball * 0.2

total_sum = annual_basketball_tax + shoes + clothes + ball + accessories
print(total_sum)