students_num = int(input())

top_students = 0
percentage_top_students = 0.0
between_4_and_5 = 0
percentage_between_4_and_5 = 0.0
between_3_and_4 = 0
percentage_between_3_and_4 = 0.0
fail_students = 0
percentage_fail_students = 0.0
average_grades = 0
grades_sum = 0
for i in range(students_num):
    grade = float(input())
    if grade >= 5.00:
        top_students += 1
    elif 4 <= grade <= 4.99:
        between_4_and_5 += 1
    elif 3 <= grade <= 3.99:
        between_3_and_4 += 1
    elif grade < 3:
        fail_students += 1
    grades_sum += grade

percentage_top_students = (top_students / students_num) * 100
percentage_between_4_and_5 = (between_4_and_5 / students_num) * 100
percentage_between_3_and_4 = (between_3_and_4 / students_num) * 100
percentage_fail_students = (fail_students / students_num) * 100
average_grades = grades_sum / students_num

print(f'Top students: {percentage_top_students:.2f}%')
print(f'Between 4.00 and 4.99: {percentage_between_4_and_5:.2f}%')
print(f'Between 3.00 and 3.99: {percentage_between_3_and_4:.2f}%')
print(f'Fail: {percentage_fail_students:.2f}%')
print(f'Average: {average_grades:.2f}')
