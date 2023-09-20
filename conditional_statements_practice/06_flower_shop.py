from math import floor, ceil

MAGNOLIAS = 3.25
HYACINTHS = 4
ROSES = 3.50
CACTUS = 8

magnolias_count = int(input())
hyacinths_count = int(input())
roses_count = int(input())
cactus_count = int(input())
gift_price = float(input())

money_earned = magnolias_count * MAGNOLIAS + hyacinths_count * HYACINTHS + roses_count * ROSES + cactus_count * CACTUS
money_after_tax = money_earned * 0.95

if money_after_tax >= gift_price:
    print(f"She is left with {floor(money_after_tax - gift_price)} leva.")
else:
    print(f"She will have to borrow {ceil(gift_price - money_after_tax)} leva.")
