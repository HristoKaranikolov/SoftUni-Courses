fuel_type = input()
liters_in_tank = float(input())

if fuel_type == "Diesel" and liters_in_tank < 25:
    print(f"Fill your tank with {fuel_type.lower()}!")
elif fuel_type == "Diesel" and liters_in_tank >= 25:
    print(f"You have enough {fuel_type.lower()}.")
elif fuel_type == "Gasoline" and liters_in_tank < 25:
    print(f"Fill your tank with {fuel_type.lower()}!")
elif fuel_type == "Gasoline" and liters_in_tank >= 25:
    print(f"You have enough {fuel_type.lower()}.")
elif fuel_type == "Gas" and liters_in_tank < 25:
    print(f"Fill your tank with {fuel_type.lower()}!")
elif fuel_type == "Gas" and liters_in_tank >= 25:
    print(f"You have enough {fuel_type.lower()}.")
elif fuel_type != "Diesel" or fuel_type != "Gasoline" or fuel_type != "Gas":
    print("Invalid fuel!")
