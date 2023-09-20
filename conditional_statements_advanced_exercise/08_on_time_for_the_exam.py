hour_exam = int(input())
minute_exam = int(input())
hour_arrival = int(input())
minute_arrival = int(input())

exam_time_in_minutes = hour_exam * 60 + minute_exam
arrival_time_in_minutes = hour_arrival * 60 + minute_arrival

difference = arrival_time_in_minutes - exam_time_in_minutes

if difference > 0:
    print("Late")
    if difference < 60:
        print(f"{difference} minutes after the start")
    else:
        hh = abs(difference) // 60
        mm = abs(difference) % 60
        print(f"{hh}:{mm :02d} hours after the start")
elif difference >= -30:
    print("On time")
    if not difference == 0:
        print(f"{abs(difference)} minutes before the start")
else:
    print("Early")
    if difference > -60:
        print(f"{abs(difference)} minutes before the start")
    else:
        hh = abs(difference) // 60
        mm = abs(difference) % 60
        print(f"{hh}:{mm :02d} hours before the start")

