puzzle_price = 2.60
speaking_doll_price = 3
teddy_bear_price = 4.10
minion_price = 8.20
truck_price = 2

vacation_price = float(input())
puzzles = int(input())
speaking_dolls = int(input())
teddy_bears = int(input())
minions = int(input())
trucks = int(input())

number_of_toys = puzzles + speaking_dolls + teddy_bears + minions + trucks

if number_of_toys >= 50:
    discount = 0.25
    sum = puzzles * puzzle_price + speaking_dolls * speaking_doll_price + \
                teddy_bears * teddy_bear_price + minions * minion_price + trucks * truck_price
    total_sum = sum - (sum * discount)
else:
    total_sum = puzzles * puzzle_price + speaking_dolls * speaking_doll_price + \
                teddy_bears * teddy_bear_price + minions * minion_price + trucks * truck_price

sum_after_rent = total_sum - (total_sum * 0.10)

if sum_after_rent >= vacation_price:
    money_left = sum_after_rent - vacation_price
    print(f"Yes! {money_left:.2f} lv left.")
else:
    needed_money = vacation_price - sum_after_rent
    print(f"Not enough money! {needed_money:.2f} lv needed.")
