upper_limit_first_digit = int(input())
upper_limit_second_digit = int(input())
upper_limit_third_digit = int(input())
first_number = 0
second_number = 0
third_number = 0

for first_digit in range(2, upper_limit_first_digit + 1):
    if first_digit % 2 == 0:
        first_number = first_digit
    else:
        continue
    for second_digit in range(2, upper_limit_second_digit + 1):
        if second_digit == 2:
            second_number = 2
        elif second_digit == 3:
            second_number = 3
        elif second_digit == 5:
            second_number = 5
        elif second_digit == 7:
            second_number = 7
        else:
            continue
        for third_digit in range(2, upper_limit_third_digit + 1):
            # if third_digit % 2 != 0:
            #     continue
            if third_digit % 2 == 0:
                third_number = third_digit
                print(f"{first_number} {second_number} {third_number}")