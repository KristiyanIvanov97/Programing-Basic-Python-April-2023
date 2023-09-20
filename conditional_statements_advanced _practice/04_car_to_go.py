budget = float(input())
season = input()
car_type = ""
car_class = ""
price_for_rent = 0

if budget <= 100:
    car_class = "Economy class"
    if season == "Summer":
        car_type = "Cabrio"
        price_for_rent = budget * 0.35
    elif season == "Winter":
        car_type = "Jeep"
        price_for_rent = budget * 0.65
elif 100 < budget <= 500:
    car_class = "Compact class"
    if season == "Summer":
        car_type = "Cabrio"
        price_for_rent = budget * 0.45
    elif season == "Winter":
        car_type = "Jeep"
        price_for_rent = budget * 0.80
else:
    car_class = "Luxury class"
    car_type = "Jeep"
    price_for_rent = budget * 0.90


print(f"{car_class}\n{car_type} - {price_for_rent:.2f}")
