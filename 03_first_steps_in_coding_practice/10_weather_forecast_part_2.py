# Напишете програма, която при въведени градуси (реално число) принтира какво е времето, като имате предвид следната таблица:
# Градуси
# Време
# 26.00 - 35.00
# Hot
# 20.1 - 25.9
# Warm
# 15.00 - 20.00
# Mild
# 12.00 - 14.9
# Cool
# 5.00 - 11.9
# Cold
# Ако се въведат градуси, различни от посочените в таблицата, да се отпечата "unknown".


# 16.5
# Mild
# 8
# Cold
# 22.4
# Warm
# 26
# Hot
# 0
# unknown


degrees = float(input())

if degrees >= 5 and degrees <= 11.9:
    print("Cold")
elif degrees >= 12 and degrees <= 14.9:
    print("Cool")
elif degrees >= 15 and degrees <= 20:
    print("Mild")
elif degrees >= 20.1 and degrees <= 25.9:
    print("Warm")
elif degrees >= 26 and degrees <= 35:
    print("Hot")
else:
    print("unknown")