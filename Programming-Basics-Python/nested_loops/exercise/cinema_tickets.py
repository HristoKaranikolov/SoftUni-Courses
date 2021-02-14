ticket_types_and_count = {"student": 0,
                          "standard": 0,
                          "kid": 0}
there_are_free_seats = True

command = input()
while not command == "Finish":
    movie_name = command
    free_seats_capacity = int(input())
    total_capacity = free_seats_capacity

    command_line = input()
    while not command_line == "End":
        ticket = command_line
        if ticket in ticket_types_and_count.keys():
            ticket_types_and_count[ticket] += 1
            free_seats_capacity -= 1
            if free_seats_capacity == 0:
                there_are_free_seats = False
                break
        command_line = input()

    percentage_full_seats = (total_capacity - free_seats_capacity) / total_capacity * 100
    print(f"{movie_name} - {percentage_full_seats:.2f}% full.")

    command = input()

total_tickets = sum([x for x in ticket_types_and_count.values()])
print(f"Total tickets: {total_tickets}")

percentage_student_tickets = ticket_types_and_count['student'] / total_tickets * 100
percentage_kid_tickets = ticket_types_and_count['kid'] / total_tickets * 100
percentage_standard_tickets = ticket_types_and_count['standard'] / total_tickets * 100
print(f"{percentage_student_tickets:.2f}% student tickets.")
print(f"{percentage_standard_tickets:.2f}% standard tickets.")
print(f"{percentage_kid_tickets:.2f}% kids tickets.")
