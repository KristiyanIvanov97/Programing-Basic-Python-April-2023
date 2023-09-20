walking_in_minutes = int(input())
walking_amount = int(input())
calories_per_day = int(input())

burned_calories = (walking_amount * walking_in_minutes) * 5

if burned_calories >= calories_per_day / 2:
    print(f"Yes, the walk for your cat is enough. Burned calories per day: {burned_calories}.")
else:
    print(f"No, the walk for your cat is not enough. Burned calories per day: {burned_calories}.")
