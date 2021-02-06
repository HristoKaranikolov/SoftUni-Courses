student_name = input()

class_number = 0
good_grades = []
bad_grades = []
is_excluded = False

while class_number < 12:
    class_number += 1
    grade = float(input())
    if grade < 4:
        bad_grades.append(grade)
        if len(bad_grades) == 2:
            class_number -= 1
            is_excluded = True
            break
    else:
        good_grades.append(grade)

if not is_excluded:
    average_grade = sum(good_grades) / len(good_grades)
    print(f"{student_name} graduated. Average grade: {average_grade:.2f}")
else:
    print(f"{student_name} has been excluded at {class_number} grade")
