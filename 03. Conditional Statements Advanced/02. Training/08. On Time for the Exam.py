# https://youtu.be/veHqJSC-9Lo
exam_hour = int(input()) * 60
exam_minutes = int(input())
arrival_hour = int(input()) * 60
arrival_minutes = int(input())

time_of_exam = exam_hour + exam_minutes
time_of_arrival = arrival_minutes + arrival_hour

hours = abs(time_of_exam - time_of_arrival) // 60
minutes = abs(time_of_exam - time_of_arrival) % 60

if time_of_arrival == time_of_exam:
    print("On time")
if (time_of_arrival < time_of_exam) and (time_of_arrival >= time_of_exam - 30):
    print(f"On time\n"
          f"{minutes} minutes before the start")
if (time_of_arrival < time_of_exam - 30) and (time_of_arrival >= time_of_exam - 59):
    print(f"Early\n"
          f"{minutes} minutes before the start")
elif time_of_arrival <= time_of_exam - 60:
    if minutes <= 9:
        print(f"Early\n"
              f"{hours}:0{minutes} hours before the start")
    else:
        print(f"Early\n"
              f"{hours}:{minutes} hours before the start")
if time_of_arrival > time_of_exam:
    if hours < 1 and minutes < 60:
        print(f"Late\n"
              f"{minutes} minutes after the start")
    elif hours >= 1:
        if minutes <= 9:
            print(f"Late\n"
                  f"{hours}:0{minutes} hours after the start")
        else:
            print(f"Late\n"
                  f"{hours}:{minutes} hours after the start")
