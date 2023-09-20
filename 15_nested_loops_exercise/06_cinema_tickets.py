student_tickets = 0
standard_tickets = 0
kid_tickets = 0
taken_seats = 0
total_tickets = 0
command = input()


while command != "Finish":
    movie_name = command
    free_seats = int(input())
    taken_seats = 0
    while True:
        ticket_type = input()

        if ticket_type == "End":
            break

        if ticket_type == "student":
            student_tickets += 1
            taken_seats += 1
        elif ticket_type == "standard":
            standard_tickets += 1
            taken_seats += 1
        elif ticket_type == "kid":
            kid_tickets += 1
            taken_seats += 1

        if taken_seats == free_seats:
            break

    percent_full = taken_seats / free_seats * 100
    print(f"{movie_name} - {percent_full :.2f}% full.")
    command = input()

    total_tickets += taken_seats

student_tickets_percent = student_tickets / total_tickets * 100
standard_tickets_percent = standard_tickets / total_tickets * 100
kid_tickets_percent = kid_tickets / total_tickets * 100
print(f"Total tickets: {total_tickets}")
print(f"{student_tickets_percent :.2f}% student tickets.")
print(f"{standard_tickets_percent :.2f}% standard tickets.")
print(f"{kid_tickets_percent :.2f}% kids tickets.")
