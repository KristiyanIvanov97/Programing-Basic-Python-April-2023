import sys
numbers_count = int(input())

total_sum = 0
max_number = -sys.maxsize

for i in range(numbers_count):
    current_number = int(input())
    if current_number > max_number:
        max_number = current_number
    total_sum += current_number

if max_number == total_sum - max_number:
    print(f"Yes\nSum = {max_number}")
else:
    total_sum -= max_number
    print(f"No\nDiff = {abs(max_number - total_sum)}")
