maximum_bad_grades = int(input())
exam_name = input()
exam_grade = int(input())
total_grade = 0
exam_count = 0
bad_exam_grade_count = 0
last_exam = ""

while exam_name != "Enough":
    if exam_grade <= 4:
        bad_exam_grade_count += 1
        if bad_exam_grade_count == maximum_bad_grades:
            print(f"You need a break, {maximum_bad_grades} poor grades.")
            break

    total_grade += exam_grade
    exam_count += 1
    last_exam = exam_name
    exam_name = input()
    if exam_name == "Enough":
        continue
    exam_grade = int(input())

else:
    average_score = total_grade / exam_count
    print(f"Average score: {average_score :.2f}")
    print(f"Number of problems: {exam_count}")
    print(f"Last problem: {last_exam}")









