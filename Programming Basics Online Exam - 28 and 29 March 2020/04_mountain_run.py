from math import ceil

record_in_seconds = float(input())
distance_in_meters = float(input())
time_in_seconds_per_meter = float(input())

slowdown = (distance_in_meters // 50) * 30
time = distance_in_meters * time_in_seconds_per_meter + ceil(slowdown)

if time < record_in_seconds:
    print(f" Yes! The new record is {time:.02f} seconds.")
else:
    print(f"No! He was {time - record_in_seconds:.02f} seconds slower.")
