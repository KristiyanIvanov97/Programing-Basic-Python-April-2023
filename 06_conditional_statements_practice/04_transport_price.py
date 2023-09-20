km_count = int(input())
day_or_night = input()


if km_count < 20:
    if day_or_night == "day":
        travel_price = 0.70 + 0.79 * km_count
        print(f"{travel_price:.2f}")
    elif day_or_night == "night":
        travel_price = 0.70 + 0.90 * km_count
        print(f"{travel_price:.2f}")

elif km_count >= 20 and km_count < 100:
    travel_price = km_count * 0.09
    print(f"{travel_price:.2f}")
elif km_count >= 100:
    travel_price = km_count * 0.06
    print(f"{travel_price:.2f}")
