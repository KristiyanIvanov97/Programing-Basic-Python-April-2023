starting_food = int(input())

starting_food_in_grams = starting_food * 1000
total_food_eaten = 0

for _ in range(10000):
    grams_eaten = int(input())
    starting_food -= grams_eaten
    if grams_eaten == "Adopted":
        break

if starting_food > 0:
    print(f"Food is enough! Leftovers: {starting_food} grams.")
else:
    print(f"Food is not enough. You need {abs(starting_food)} grams more.")

# Ако количеството храна е достатъчно да се отпечата:
# "Food is enough! Leftovers: {останала храна} grams."
#  Ако количеството храна не е достатъчно да се отпечата:
# "Food is not enough. You need {нужно количество храна} grams more."