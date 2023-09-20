numbers_count = int(input())

numbers1 = 0
numbers2 = 0
numbers3 = 0
numbers4 = 0
numbers5 = 0

for _ in range(numbers_count):
    current_number = int(input())
    if current_number < 200:
        numbers1 += 1
    elif current_number < 400:
        numbers2 += 1
    elif current_number < 600:
        numbers3 += 1
    elif current_number < 800:
        numbers4 += 1
    elif current_number >= 800:
        numbers5 += 1

numbers1_in_percent = numbers1 / numbers_count * 100
numbers2_in_percent = numbers2 / numbers_count * 100
numbers3_in_percent = numbers3 / numbers_count * 100
numbers4_in_percent = numbers4 / numbers_count * 100
numbers5_in_percent = numbers5 / numbers_count * 100

print(f"{numbers1_in_percent :.2f}%")
print(f"{numbers2_in_percent :.2f}%")
print(f"{numbers3_in_percent :.2f}%")
print(f"{numbers4_in_percent :.2f}%")
print(f"{numbers5_in_percent :.2f}%")
