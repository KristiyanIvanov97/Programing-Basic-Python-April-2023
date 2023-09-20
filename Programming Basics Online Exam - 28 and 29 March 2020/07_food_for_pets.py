days = int(input())
food_amount = float(input())

dog_food = 0
cat_food = 0
biscuits = 0
total_eaten_food = 0
total_dog_food = 0
total_cat_food = 0

for day in range(1, days + 1):
    dog_food = int(input())
    cat_food = int(input())
    total_dog_food += dog_food
    total_cat_food += cat_food
    total_eaten_food += dog_food + cat_food
    if day % 3 == 0:
        biscuits += (dog_food + cat_food) * 0.10


total_food_eaten_in_percent = (total_eaten_food / food_amount) * 100
dog_food_in_percent = (total_dog_food / total_eaten_food) * 100
cat_food_in_percent = (total_cat_food / total_eaten_food) * 100

print(f"Total eaten biscuits: {round(biscuits)}gr.")
print(f"{total_food_eaten_in_percent:.2f}% of the food has been eaten.")
print(f"{dog_food_in_percent:.2f}% eaten from the dog.")
print(f"{cat_food_in_percent:.2f}% eaten from the cat.")
