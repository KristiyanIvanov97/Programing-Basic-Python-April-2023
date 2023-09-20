money_needed = float(input())
current_money = float(input())
days = 0
spending_days = 0

while True:
    money_operation = input()
    daily_money = float(input())
    days += 1

    if money_operation == "save":
        current_money += daily_money
        spending_days = 0
    else:
        if daily_money > current_money:
            current_money -= current_money
        else:
            current_money -= daily_money

        spending_days += 1
        if spending_days == 5 or current_money < 0:
            print("You can't save the money.")
            print(f"{days}")
            break

    if current_money >= money_needed:
        print(f"You saved the money for {days} days.")
        break
