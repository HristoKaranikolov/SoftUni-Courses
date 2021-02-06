command = input()

total_money = 0
while not command == "NoMoreMoney":
    cash = float(command)
    if cash <= 0:
        print("Invalid operation!")
        break
    print(f"Increase: {cash:.2f}")
    total_money += cash

    command = input()

print(f"Total: {total_money:.2f}")
