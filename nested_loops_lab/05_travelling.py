destination = input()
total_money = 0
while True:
    if destination == "End":
        break
    needed_money = float(input())
    while True:
        saved_money = float(input())
        total_money += saved_money

        if total_money >= needed_money:
            print(f"Going to {destination}!")
            break

    destination = input()
    total_money = 0
