starting_point_in_meters = 5364
days_climbing = 1
command = ""
total_climbed = starting_point_in_meters
command_no = 0

while True:
    command = input()
    if command == "END":
        break

    if command == "Yes":
        current_meters_climb = int(input())
        total_climbed += current_meters_climb
        days_climbing += 1
        command_no = 0
        if days_climbing >= 5:
            break
    elif command == "No":
        current_meters_climb = int(input())
        total_climbed += current_meters_climb
        if command_no >= 1:
            days_climbing += 1
        command_no += 1

    if days_climbing >= 5:
        break
    if total_climbed >= 8848:
        break

if total_climbed >= 8848:
    print(f"Goal reached for {days_climbing} days!")
else:
    print(f"Failed!\n{total_climbed}")