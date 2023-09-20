import math

days = int(input())
food_in_kg = int(input())
food_per_day_for_first_deer = float(input())
food_per_day_for_second_deer = float(input())
food_per_day_for_third_deer = float(input())

eaten_food_by_first_deer = days * food_per_day_for_first_deer
eaten_food_by_second_deer = days * food_per_day_for_second_deer
eaten_food_by_third_deer = days * food_per_day_for_third_deer

total_food_eaten = eaten_food_by_first_deer + eaten_food_by_second_deer + eaten_food_by_third_deer

if food_in_kg >= total_food_eaten:
    print(f"{math.floor(food_in_kg - total_food_eaten)} kilos of food left.")
else:
    print(f"{math.ceil(total_food_eaten - food_in_kg)} more kilos of food are needed.")


#  Ако оставената храна Е достатъчна:
# o “{килограми, които остават} kilos of food left.”
#  Резултатът трябва да е закръглен към ПО-МАЛКОТО цяло число
#  Ако оставената храна НЕ Е достатъчна:
# o “{килограми, които не недостигат} more kilos of food are needed.”
#  Резултатът трябва да е закръглен към ПО-ГОЛЯМОТО цяло число