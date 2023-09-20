ROSES_PRICE = 5
DAHLIAS_PRICE = 3.80
TULIPS_PRICE = 2.80
NARCISSUS_PRICE = 3
GLADIOLUS_PRICE = 2.50

flower_type = input()
flower_count = int(input())
budget = int(input())
total_price = 0
discount = 1

if flower_type == "Roses":
    if flower_count > 80:
        discount = 0.90
    total_price = flower_count * ROSES_PRICE * discount
elif flower_type == "Dahlias":
    if flower_count > 90:
        discount = 0.85
    total_price = flower_count * DAHLIAS_PRICE * discount
elif flower_type == "Tulips":
    if flower_count > 80:
        discount = 0.85
    total_price = flower_count * TULIPS_PRICE * discount
elif flower_type == "Narcissus":
    if flower_count < 120:
        discount = 1.15
    total_price = flower_count * NARCISSUS_PRICE * discount
elif flower_type == "Gladiolus":
    if flower_count < 80:
        discount = 1.20
    total_price = flower_count * GLADIOLUS_PRICE * discount

if budget >= total_price:
    print(f"Hey, you have a great garden with {flower_count} {flower_type} and {budget - total_price :.2f} leva left.")
else:
    print(f"Not enough money, you need {total_price - budget :.2f} leva more.")




















# · Ако бюджетът им е достатъчен - "Hey, you have a great garden with {броя цвета} {вид цветя} and {останалата сума} leva left.";
# · Ако бюджета им е НЕ достатъчен - "Not enough money, you need {нужната сума} leva more.".