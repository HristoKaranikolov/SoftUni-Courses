needed_money = float(input())
budget = float(input())

days_counter = 0
spend_days_counter = 0
reached_spend_limit = False
while True:
    if budget >= needed_money:
        break

    save_or_spend = input()
    amount = float(input())
    days_counter += 1
    if save_or_spend == 'spend':
        spend_days_counter += 1
        if spend_days_counter == 5:  # Here if we reach the spend limit we need to stop spending!
            break

        budget -= amount
        if budget < 0:
            budget = 0
    else:
        spend_days_counter = 0
        budget += amount

if budget < needed_money:
    print("You can't save the money.", end='\n'
          f"{days_counter}")
else:
    print(f"You saved the money for {days_counter} days.")
