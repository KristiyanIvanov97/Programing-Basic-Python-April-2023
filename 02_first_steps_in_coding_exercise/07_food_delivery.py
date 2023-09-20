CHICKEN_MENU_PRICE = 10.35
FISH_MENU_PRICE = 12.40
VEGGIE_MENU_PRICE = 8.15
DELLIVERY_PRICE = 2.50

chicken_menus = int(input())
fish_menus = int(input())
veggie_menus = int(input())

bill = chicken_menus * CHICKEN_MENU_PRICE + fish_menus * FISH_MENU_PRICE + veggie_menus * VEGGIE_MENU_PRICE
desert = bill * 0.20
total_bill = bill + desert + 2.50

print(total_bill)