expected_amount_to_collect = int(input())

articles_sum = 0

card_payment_count = 0
card_payment_sum = 0

cash_payment_count = 0
cash_payment_sum = 0
loop_counter = 0

command = input()
while command != "End":
    article_price = int(command)
    loop_counter += 1
    if loop_counter % 2 != 0:
        if article_price <= 100:
            cash_payment_count += 1
            cash_payment_sum += article_price
            articles_sum += article_price
            print("Product sold!")
        else:
            print("Error in transaction!")
    else:
        if article_price >= 10:
            card_payment_count += 1
            card_payment_sum += article_price
            articles_sum += article_price
            print("Product sold!")
        else:
            print("Error in transaction!")
    if articles_sum >= expected_amount_to_collect:
        break
    command = input()
if command == 'End' and articles_sum < expected_amount_to_collect:
    print("Failed to collect required money for charity.")
else:
    if cash_payment_count == 0:
        print(f"Average CS: {0:.2f}")
        print(f"Average CC: {card_payment_sum / card_payment_count:.2f}")
    elif card_payment_count == 0:
        print(f"Average CS: {cash_payment_sum / cash_payment_count:.2f}")
        print(f"Average CC: {0:.2f}")
    else:
        print(f"Average CS: {cash_payment_sum / cash_payment_count:.2f}")
        print(f"Average CC: {card_payment_sum / card_payment_count:.2f}")
