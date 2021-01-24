exam_hour = int(input())
exam_minutes = int(input())
arriving_hour = int(input())
arriving_min = int(input())

exam_time = exam_hour * 60 + exam_minutes
arriving_time = arriving_hour * 60 + arriving_min

result = ''
if arriving_time > exam_time:
    result = 'Late'
elif arriving_time < exam_time - 30:
    result = 'Early'
else:
    result = 'On time'

time_difference = ''
if result == 'Early':
    if arriving_time <= exam_time - 60:  # If we are early for the exam with 1.00 hour or more.
        hours = (exam_time - arriving_time) // 60
        minutes = (exam_time - arriving_time) % 60
        time_difference = f"{hours}:{minutes:02d} hours before the start"
    else:
        minutes = (exam_time - arriving_time) % 60
        time_difference = f"{minutes} minutes before the start"

elif result == 'On time' and exam_time - 60 < arriving_time < exam_time:  # if we are early less than an hour.
    minutes = (exam_time - arriving_time) % 60
    time_difference = f"{minutes} minutes before the start"

elif result == 'Late':
    if arriving_time >= exam_time + 60:  # if we are late with an hour and more.
        hours = (arriving_time - exam_time) // 60
        minutes = (arriving_time - exam_time) % 60
        time_difference = f"{hours}:{minutes:02d} hours after the start"

    elif exam_time + 60 > arriving_time > exam_time:  # if we are late with less than an hour.
        minutes = (arriving_time - exam_time) % 60
        time_difference = f"{minutes} minutes after the start"

print(result)
print(time_difference)

# hour_of_exam = int(input())
# minutes_of_exam = int(input())
# hour_of_arriving = int(input())
# minutes_of_arriving = int(input())
#
# time_of_examine = hour_of_exam * 60 + minutes_of_exam
# time_of_arriving = hour_of_arriving * 60 + minutes_of_arriving
#
# result = ''
# if time_of_arriving > time_of_examine:
#     result = "Late"
# elif time_of_examine - 30 <= time_of_arriving <= time_of_examine:
#     result = "On time"
# elif time_of_arriving < time_of_examine - 30:
#     result = "Early"
#
# time_diff = ''
# if time_of_examine - 60 < time_of_arriving < time_of_examine:
#     minutes = time_of_examine - time_of_arriving
#     time_diff = f'{minutes} minutes before the start'
#
# elif time_of_arriving <= time_of_examine - 60:
#     hours = (time_of_examine - time_of_arriving) // 60
#     minutes = (time_of_examine - time_of_arriving) % 60
#     time_diff = f"{hours}:{minutes:0>2d} hours before the start"
#
# elif time_of_examine < time_of_arriving < time_of_examine + 60:
#     minutes = time_of_arriving - time_of_examine
#     time_diff = f'{minutes} minutes after the start'
#
# elif time_of_arriving >= time_of_examine + 60:
#     hours = (time_of_arriving - time_of_examine) // 60
#     minutes = (time_of_arriving - time_of_examine) % 60
#     time_diff = f"{hours}:{minutes:0>2d} hours after the start"
#
# print(result)
# print(time_diff)
