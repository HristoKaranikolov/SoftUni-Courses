num_loads = int(input())

average_price_per_tone = 0
total_load_tonnage = 0
total_bus_load = 0
total_truck_load = 0
total_train_load = 0
price_bus = 0
price_truck = 0
price_train = 0

for load in range(num_loads):
    load_tonnage = int(input())
    total_load_tonnage += load_tonnage

    if 0 < load_tonnage <= 3:
        total_bus_load += load_tonnage
        price_bus = total_bus_load * 200
    elif 4 <= load_tonnage <= 11:
        total_truck_load += load_tonnage
        price_truck = total_truck_load * 175
    elif load_tonnage >= 12:
        total_train_load += load_tonnage
        price_train = total_train_load * 120

average_price_per_tone = (price_train + price_truck + price_bus) / total_load_tonnage
bus_percentage = total_bus_load / total_load_tonnage * 100
truck_percentage = total_truck_load / total_load_tonnage * 100
train_percentage = total_train_load / total_load_tonnage * 100

print(f'{average_price_per_tone:.2f}')
print(f'{bus_percentage:.2f}%')
print(f'{truck_percentage:.2f}%')
print(f'{train_percentage:.2f}%')
