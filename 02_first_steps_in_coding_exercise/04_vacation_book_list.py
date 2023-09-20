pages = int(input())
pages_per_hour = int(input())
days = int(input())

total_time = pages / pages_per_hour
needed_hours_per_day = total_time / days

print(int(needed_hours_per_day))