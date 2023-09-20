width_of_the_room = int(input())
length_of_the_room = int(input())
height_of_the_room = int(input())

total_space = width_of_the_room * length_of_the_room * height_of_the_room

while True:
    command = input()

    if command == "Done":
        print(f"{total_space} Cubic meters left.")
        break

    boxes = int(command)
    total_space -= boxes

    if total_space <= 0:
        print(f"No more free space! You need {abs(total_space)} Cubic meters more.")
        break

