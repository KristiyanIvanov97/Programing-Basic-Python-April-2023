import math
figure = input()
if figure == "square":
    side_lenght = float(input())
    area = side_lenght * side_lenght
    print(f"{area:.3f}")
elif figure == "rectangle":
    side_a = float(input())
    side_b = float(input())
    area = side_a * side_b
    print(f"{area:.3f}")
elif figure == "circle":
    radius = float(input())
    area = math.pi * radius ** 2
    print(f"{area:.3f}")
else:
    figure == "triangle"
    side_a = float(input())
    height_a = float(input())
    area = (side_a * height_a) / 2
    print(f"{area:.3f}")