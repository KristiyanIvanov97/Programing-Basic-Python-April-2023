PRICE_FOR_ARRANGEMENT = 2

chrysanthemums = int(input())
roses = int(input())
tulips = int(input())
season = input()
is_it_holiday = input()
chrysanthemums_price = 0
roses_price = 0
tulips_price = 0

if season == "Spring" or season == "Summer":
    chrysanthemums_price = 2
    roses_price = 4.10
    tulips_price = 2.50
elif season == "Autumn" or season == "Winter":
    chrysanthemums_price = 3.75
    roses_price = 4.50
    tulips_price = 4.15

if is_it_holiday == "Y":
    chrysanthemums_price *= 1.15
    roses_price *= 1.15
    tulips_price *= 1.15

total_price = chrysanthemums * chrysanthemums_price + roses * roses_price + tulips * tulips_price

if season == "Spring" and tulips > 7:
    total_price *= 0.95
if season == "Winter" and roses >= 10:
    total_price *= 0.90
if chrysanthemums + roses + tulips > 20:
    total_price *= 0.80

print(f"{total_price + PRICE_FOR_ARRANGEMENT :.2f}")
