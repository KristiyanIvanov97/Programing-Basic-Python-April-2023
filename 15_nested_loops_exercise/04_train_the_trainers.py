judges_count = int(input())
command = input()

total_score = 0
all_scores = 0
presentation_count = 0
while command != "Finish":
    presentation = command
    total_score = 0

    for current_presentation in range(judges_count):
        current_score = float(input())
        total_score += current_score
        all_scores += current_score

    presentation_count += 1
    average_score = total_score / judges_count
    print(f"{presentation} - {average_score :.2f}.")

    command = input()

total_average = all_scores / (judges_count * presentation_count)
print(f"Student's final assessment is {total_average :.2f}.")