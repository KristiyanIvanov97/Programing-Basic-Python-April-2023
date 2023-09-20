house_height = float(input())
side_wall_length = float(input())
triangle_wall_height = float(input())

front_wall_door = 1.20 * 2
front_and_rear_walls = ((house_height ** 2) * 2) - front_wall_door
side_wall_windows = (1.5 ** 2) * 2
side_walls = (side_wall_length * house_height) * 2 - side_wall_windows

rectangle_roof_sides = house_height * side_wall_length * 2
triangle_roof_sides = ((house_height * triangle_wall_height) / 2) * 2

green_paint = (front_and_rear_walls + side_walls) / 3.4
red_paint = (rectangle_roof_sides + triangle_roof_sides) / 4.3

print(f"{green_paint:.2f}")
print(f"{red_paint:.2f}")
