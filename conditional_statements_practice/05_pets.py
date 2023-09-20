from math import floor, ceil
days_off = int(input())
food_left = int(input())
food_for_dog = float(input())
food_for_cat = float(input())
food_for_turtle_in_grams = float(input())

food_needed = (food_for_dog + food_for_cat + (food_for_turtle_in_grams / 1000)) * days_off

if food_left >= food_needed:
    print(f"{floor(food_left - food_needed)} kilos of food left.")
elif food_left < food_needed:
    print(f"{ceil(food_needed - food_left)} more kilos of food are needed.")