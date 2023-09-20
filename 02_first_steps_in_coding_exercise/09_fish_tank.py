lenght = int(input())
width = int(input())
height = int(input())
percent_busy = float(input()) / 100

total_capacity_in_liters = (lenght * width * height) / 1000
liters_needed = total_capacity_in_liters - (total_capacity_in_liters * percent_busy)

print(liters_needed)