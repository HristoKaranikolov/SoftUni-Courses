jury_count = int(input())

presentations_and_ratings = {}
presentation = input()
while not presentation == "Finish":
    presentations_and_ratings[presentation] = []
    for i in range(jury_count):
        assessment = float(input())
        presentations_and_ratings[presentation].append(assessment)

    presentation = input()

all_ratings = []
for key, value in presentations_and_ratings.items():
    average_rating = sum(value) / len(value)
    all_ratings.append(average_rating)
    print(f"{key} - {average_rating:.2f}.")

all_average = sum(all_ratings) / len(all_ratings)
print(f"Student's final assessment is {all_average:.2f}.")
