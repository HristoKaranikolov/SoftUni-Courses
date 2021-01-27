command = input()

while command != "Negative number!":
    number = float(command)
    if number < 0:
        print("Negative number!")
        break
    result = number * 2
    print(f"Result: {result:.2f}")

    command = input()

