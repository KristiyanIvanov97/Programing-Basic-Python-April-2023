change = float(input())
change_in_pennies = int(change * 100)
number_of_coins = 0

while change_in_pennies > 0:
    if change_in_pennies // 200 > 0:
        change_in_pennies -= 200
    elif change_in_pennies // 100 > 0:
        change_in_pennies -= 100
    elif change_in_pennies // 50 > 0:
        change_in_pennies -= 50
    elif change_in_pennies // 20 > 0:
        change_in_pennies -= 20
    elif change_in_pennies // 10 > 0:
        change_in_pennies -= 10
    elif change_in_pennies // 5 > 0:
        change_in_pennies -= 5
    elif change_in_pennies // 2 > 0:
        change_in_pennies -= 2
    elif change_in_pennies // 1 > 0:
        change_in_pennies -= 1

    number_of_coins += 1
print(number_of_coins)
