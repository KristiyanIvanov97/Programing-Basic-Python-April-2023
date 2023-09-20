budget = int(input())
season = input()
fisherman_count = int(input())
boat_rent = 0
discount_for_number_of_people = 0
extra_discount = 1

if season == "Spring":
    boat_rent = 3000
elif season == "Summer" or season == "Autumn":
    boat_rent = 4200
elif season == "Winter":
    boat_rent = 2600

if fisherman_count <= 6:
    discount_for_number_of_people = 0.90
elif 7 < fisherman_count <= 11:
    discount_for_number_of_people = 0.85
else:
    discount_for_number_of_people = 0.75

if fisherman_count % 2 == 0 and season != "Autumn":
    extra_discount = 0.95

total_sum = boat_rent * discount_for_number_of_people * extra_discount

if budget >= total_sum:
    print(f"Yes! You have {budget - total_sum :.2f} leva left.")
else:
    print(f"Not enough money! You need {total_sum - budget :.2f} leva.")




