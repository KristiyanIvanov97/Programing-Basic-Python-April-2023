fuel_type = input()
liters_in_fuel_tank = float(input())

if liters_in_fuel_tank >= 25:
    if fuel_type != "Diesel" and fuel_type != "Gasoline" and fuel_type != "Gas":
        print("Invalid fuel!")
    else:
        print(f"You have enough {fuel_type.lower()}.")
elif liters_in_fuel_tank < 25:
    if fuel_type != "Diesel" and fuel_type != "Gasoline" and fuel_type != "Gas":
        print("Invalid fuel!")
    else:
        print(f"Fill your tank with {fuel_type.lower()}!")

