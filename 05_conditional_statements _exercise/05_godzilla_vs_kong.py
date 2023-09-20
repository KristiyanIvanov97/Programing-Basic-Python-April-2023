film_budget = float(input())
supernumerary = int(input())    # statisti
cloth_price_per_supernumerary = float(input())

film_decor = film_budget * 0.10


if supernumerary > 150:
    cloth_price_per_supernumerary *= 0.90

money_needed = supernumerary * cloth_price_per_supernumerary + film_decor

if money_needed > film_budget:
    print("Not enough money!")
    print(f"Wingard needs {money_needed - film_budget :.2f} leva more.")
elif money_needed <= film_budget:
    print("Action!")
    print(f"Wingard starts filming with {film_budget - money_needed :.2f} leva left.")
