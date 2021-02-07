bad_grades_counter = int(input())

problems = []
grades = []
bad_grades = []
has_failed = False

while True:
    problem_name = input()
    if problem_name == 'Enough':
        break
    problems.append(problem_name)

    grade = int(input())
    if grade <= 4:
        bad_grades.append(grade)
        if len(bad_grades) == bad_grades_counter:
            has_failed = True
            break

    grades.append(grade)

if has_failed:
    print(f"You need a break, {len(bad_grades)} poor grades.")
else:
    average = sum(grades) / len(grades)
    last_problem = problems[-1]
    print(f"Average score: {average:.2f}")
    print(f"Number of problems: {len(grades)}")
    print(f"Last problem: {last_problem}")
