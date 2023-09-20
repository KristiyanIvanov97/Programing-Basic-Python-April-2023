from math import ceil

training_days = int(input())
km_done_firs_day = float(input())
total_km_done = km_done_firs_day

for _ in range(training_days):
    percent_daily_norm = int(input()) / 100
    current_day = km_done_firs_day * (1 + percent_daily_norm)
    km_done_firs_day = current_day

    total_km_done += km_done_firs_day

if total_km_done >= 1000:
    print(f"You've done a great job running {ceil(total_km_done - 1000)} more kilometers!")
else:
    print(f"Sorry Mrs. Ivanova, you need to run {ceil(1000 - total_km_done)} more kilometers")
