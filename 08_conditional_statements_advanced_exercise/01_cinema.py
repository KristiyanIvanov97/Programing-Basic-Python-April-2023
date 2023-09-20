PREMIERE = 12.00
NORMAL = 7.50
FOR_KIDS_AND_STUDENTS = 5

projection = input()
rows = int(input())
columns = int(input())
income = 0
number_of_seats = rows * columns

if projection == "Premiere":
    income = number_of_seats * PREMIERE
elif projection == "Normal":
    income = number_of_seats * NORMAL
elif projection == "Discount":
    income = number_of_seats * FOR_KIDS_AND_STUDENTS

print(f"{income:.2f} leva.")