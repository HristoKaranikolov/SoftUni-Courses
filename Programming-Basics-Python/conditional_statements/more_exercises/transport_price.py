n = int(input())
traveling = input()

taxi = 0.70
taxi_daily = 0.79
taxi_nightly = 0.90
bus = 0.09
train = 0.06

if 0 < n < 20:
    if traveling == 'day':
        price = taxi + n * taxi_daily
        print(f'{price:.2f}')
    elif traveling == 'night':
        price = taxi + n * taxi_nightly
        print(f'{price:.2f}')
elif 20 <= n < 100:
    price = bus * n
    print(f'{price:.2f}')
elif n >= 100:
    price = train * n
    print(f'{price:.2f}')