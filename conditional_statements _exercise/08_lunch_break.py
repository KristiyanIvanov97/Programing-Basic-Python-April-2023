from math import ceil

serial_name = input()
episode_length = int(input())
break_time = int(input())

lunch_time = 1/8 * break_time
rest_time = 1/4 * break_time
total_time = lunch_time + rest_time + episode_length

if total_time <= break_time:
    print(f"You have enough time to watch {serial_name} and left with "
          f"{ceil(break_time - total_time)} minutes free time.")
elif total_time > break_time:
    print(f"You don't have enough time to watch {serial_name}, you need {ceil(total_time - break_time)} more minutes.")
