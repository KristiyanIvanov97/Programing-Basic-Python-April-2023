fruit = input()
size = input()
drinks_amount = int(input())
drink_price = 0
total_sum = 0

if size == "small":
    if fruit == "Watermelon":
        drink_price = 56
    elif fruit == "Mango":
        drink_price = 36.66
    elif fruit == "Pineapple":
        drink_price = 42.10
    elif fruit == "Raspberry":
        drink_price = 20
    total_sum = drinks_amount * drink_price * 2
elif size == "big":
    if fruit == "Watermelon":
        drink_price = 28.70
    elif fruit == "Mango":
        drink_price = 19.60
    elif fruit == "Pineapple":
        drink_price = 24.80
    elif fruit == "Raspberry":
        drink_price = 15.20
    total_sum = drinks_amount * drink_price * 5

if 400 <= total_sum <= 1000:
    total_sum *= 0.85
elif total_sum > 1000:
    total_sum *= 0.50

print(f"{total_sum:.02f} lv.")
