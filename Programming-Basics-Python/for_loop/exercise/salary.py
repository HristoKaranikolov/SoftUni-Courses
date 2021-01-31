browser_tab_counter = int(input())
salary = float(input())

fines = {"Facebook": 150,
         "Instagram": 100,
         "Reddit": 50}

for i in range(browser_tab_counter):
    website = input()
    if website in fines:
        salary -= fines[website]

if salary > 0:
    print(int(salary))
else:
    print("You have lost your salary.")