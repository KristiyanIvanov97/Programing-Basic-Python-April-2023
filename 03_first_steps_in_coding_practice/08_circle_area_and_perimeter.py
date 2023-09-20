# Напишете програма, която чете от конзолата число r и пресмята и отпечатва лицето и периметъра на кръг / окръжност с радиус r,
# като форматирате изхода в следния вид: "<calculated area>"
# "<calculated parameter>". Форматирайте изходните данни до втория знак след десетичната запетая.
import math

r = float(input())

circle_area = math.pi * (r ** 2)
circle_perimeter = 2 * math.pi * r

print(f"{circle_area:.2f}")
print(f"{circle_perimeter:.2f}")