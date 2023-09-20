season = input()
group_type = input()
students = int(input())
days = int(input())
price_per_night = 0
sport = ""

if season == "Winter":
    if group_type == "boys" or group_type == "girls":
        price_per_night = 9.60
        if group_type == "boys":
            sport = "Judo"
        elif group_type == "girls":
            sport = "Gymnastics"
    elif group_type == "mixed":
        price_per_night = 10
        sport = "Ski"
elif season == "Spring":
    if group_type == "boys" or group_type == "girls":
        price_per_night = 7.20
        if group_type == "boys":
            sport = "Tennis"
        elif group_type == "girls":
            sport = "Athletics"
    elif group_type == "mixed":
        price_per_night = 9.50
        sport = "Cycling"
elif season == "Summer":
    if group_type == "boys" or group_type == "girls":
        price_per_night = 15
        if group_type == "boys":
            sport = "Football"
        elif group_type == "girls":
            sport = "Volleyball"
    elif group_type == "mixed":
        price_per_night = 20
        sport = "Swimming"

total_sum = students * price_per_night * days

if students >= 50:
    total_sum *= 0.50
elif 20 <= students < 50:
    total_sum *= 0.85
elif 10 <= students < 20:
    total_sum *= 0.95

print(f"{sport} {total_sum:.2f} lv.")
