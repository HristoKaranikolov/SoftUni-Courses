budget = float(input())
gpu_count = int(input())
cpu_count = int(input())
ram_count = int(input())

one_gpu_price = 250
gpu_total_price = gpu_count * one_gpu_price

one_cpu_price = gpu_total_price * 0.35
one_ram_price = gpu_total_price * 0.10

cpu_total_price = cpu_count * one_cpu_price
ram_total_price = ram_count * one_ram_price

total_price = gpu_total_price + cpu_total_price + ram_total_price

if gpu_count > cpu_count:
    total_price *= 0.85

difference = abs(budget - total_price)
if budget >= total_price:
    print(f"You have {difference:.2f} leva left!")
else:
    print(f"Not enough money! You need {difference:.2f} leva more!")
