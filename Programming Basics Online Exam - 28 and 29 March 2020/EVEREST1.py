starting_point_in_meters = 5364
climbing_days = 1
total_climbed = starting_point_in_meters

while True:
    command = input()
    if command == "END":
        break

    if command == "Yes":
        climbing_days += 1
        current_meters_climb = int(input())
        total_climbed += current_meters_climb
    elif command == "No":
        current_meters_climb = int(input())
        total_climbed += current_meters_climb

    if climbing_days > 5:
        break
    if total_climbed >= 8848:
        break

if total_climbed >= 8848:
    print(f"Goal reached for {climbing_days} days!")
else:
    print(f"Failed!\n{total_climbed}")