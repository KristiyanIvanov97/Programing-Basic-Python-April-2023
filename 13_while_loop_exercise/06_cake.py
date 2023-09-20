width = int(input())
length = int(input())

number_of_pieces = width * length

while True:
    command = input()

    if command == "STOP":
        break

    current_pieces = int(command)
    number_of_pieces -= current_pieces
    if number_of_pieces <= 0:
        break

if number_of_pieces <= 0:
    print(f"No more cake left! You need {abs(number_of_pieces)} pieces more.")
else:
    print(f"{number_of_pieces} pieces are left.")