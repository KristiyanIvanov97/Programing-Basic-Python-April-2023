start_of_interval = int(input())
final_of_interval = int(input())
magic_number = int(input())
combination = 0
result = 0

for first_number in range(start_of_interval, final_of_interval + 1):
    for second_number in range(start_of_interval, final_of_interval + 1):
        combination += 1
        result = first_number + second_number
        if result == magic_number:
            print(f"Combination N:{combination} ({first_number} + {second_number} = {magic_number})")
            break
    if result == magic_number:
        break
if result != magic_number:
    print(f"{combination} combinations - neither equals {magic_number}")






# На конзолата трябва да се отпечата един ред, според резултата:
# • Ако е намерена комбинация чиито сбор на числата е равен на магическото число
# o "Combination N:{пореден номер} ({първото число} + {второ число} = {магическото число})"
# • Ако не е намерена комбинация отговаряща на условието
# o "{броят на всички комбинации} combinations - neither equals {магическото число}"
