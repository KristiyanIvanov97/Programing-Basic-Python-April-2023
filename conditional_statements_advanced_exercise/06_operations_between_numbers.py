first_number = int(input())
second_number = int(input())
operator = input()
odd_or_even = ""
numbers_sum = 0

if operator == "+" or operator == "-" or operator == "*":
    if operator == "+":
        numbers_sum = first_number + second_number
    if operator == "-":
        numbers_sum = first_number - second_number
    if operator == "*":
        numbers_sum = first_number * second_number
    if numbers_sum % 2 == 0:
        odd_or_even = "even"
    else:
        odd_or_even = "odd"
    print(f"{first_number} {operator} {second_number} = {numbers_sum} - {odd_or_even}")

if second_number == 0:
    print(f"Cannot divide {first_number} by zero")
elif operator == "/":
    numbers_sum = first_number / second_number
    print(f"{first_number} / {second_number} = {numbers_sum :.2f}")
elif operator == "%":
    numbers_sum = first_number % second_number
    print(f"{first_number} % {second_number} = {numbers_sum}")


