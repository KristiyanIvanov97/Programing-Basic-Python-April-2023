searched_number = int(input())
combinations = 0

for first_number in range(0, searched_number + 1):
    for second_number in range(0, searched_number + 1):
        for third_number in range(0, searched_number + 1):
            result = first_number + second_number + third_number
            if result == searched_number:
                combinations += 1

print(combinations)