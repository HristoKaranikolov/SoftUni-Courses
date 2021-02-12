destination = input()

while not destination == "End":

    min_budget = float(input())
    curr_destination_total_savings = 0
    data = input()
    while not data.isalpha():
        savings = float(data)
        curr_destination_total_savings += savings
        data = input()

    if curr_destination_total_savings >= min_budget:
        print(f"Going to {destination}!")

    destination = data
