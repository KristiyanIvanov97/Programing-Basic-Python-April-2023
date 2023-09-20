student_name = input()
current_class = 1
total_grade = 0
total_fail = 0

while current_class <= 12:
    grade = float(input())
    if grade < 4:
        total_fail += 1
        if total_fail > 1:
            print(f"{student_name} has been excluded at {current_class} grade")
            break
        continue
    current_class += 1
    total_grade += grade
else:
    average_grade = total_grade / 12
    print(f"{student_name} graduated. Average grade: {average_grade:.2f}")
