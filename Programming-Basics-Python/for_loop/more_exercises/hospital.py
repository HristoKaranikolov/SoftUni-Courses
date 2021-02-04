time_interval = int(input())

doctors = 7
treated_patients = 0
untreated_patients = 0

for day in range(1, time_interval + 1):
    if day % 3 == 0:
        if untreated_patients > treated_patients:
            doctors += 1

    patients_num = int(input())
    if patients_num <= doctors:
        treated_patients += patients_num
    else:
        treated_patients += doctors
        untreated_patients += (patients_num - doctors)

print(f"Treated patients: {treated_patients}.")
print(f"Untreated patients: {untreated_patients}.")
