fats_percent = int(input()) / 100
protein_percent = int(input()) / 100
carbohydrates_percent = int(input()) / 100
calories = int(input())
water_percent = int(input()) / 100

fats = fats_percent * calories / 9
protein = protein_percent * calories / 4
carbohydrates = carbohydrates_percent * calories / 4

total_food = calories / (fats + protein + carbohydrates)

food_without_water = total_food * (1 - water_percent)

print(f"{food_without_water :.4f}")
