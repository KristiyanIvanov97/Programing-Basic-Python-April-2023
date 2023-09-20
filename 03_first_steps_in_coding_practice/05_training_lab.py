length_in_m = float(input())
width_in_m = float(input())

length_in_cm = length_in_m * 100
width_in_cm = width_in_m * 100
lengthwise_rows = length_in_cm // 120
width_desks = (width_in_cm - 100) // 70
work_places = lengthwise_rows * width_desks - 3

print(int(work_places))