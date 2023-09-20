from math import floor

record_to_beat_in_seconds = float(input())
distance = float(input())
time_in_seconds_per_meter = float(input())

water_resistance = floor(distance / 15) * 12.5
total_time = distance * time_in_seconds_per_meter + water_resistance
needed_seconds = total_time - record_to_beat_in_seconds

if total_time < record_to_beat_in_seconds:
    print(f"Yes, he succeeded! The new world record is {total_time :.2f} seconds.")
elif total_time >= record_to_beat_in_seconds:
    print(f"No, he failed! He was {needed_seconds :.2f} seconds slower.")

