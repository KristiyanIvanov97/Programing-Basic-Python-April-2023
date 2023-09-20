room_for_one_person = 18
apartment = 25
president_apartment = 35

days = int(input())
room = input()
grade = input()
total_bill = 0

if room == "room for one person":
    total_bill = (days - 1) * room_for_one_person

if room == "apartment":
    total_bill = (days - 1) * apartment
    if days < 10:
        total_bill *= 0.70
    elif 10 < days < 15:
        total_bill *= 0.65
    elif days > 15:
        total_bill *= 0.50

if room == "president apartment":
    total_bill = (days - 1) * president_apartment
    if days < 10:
        total_bill *= 0.90
    elif 10 < days < 15:
        total_bill *= 0.85
    elif days > 15:
        total_bill *= 0.80

if grade == "positive":
    total_bill *= 1.25
elif grade == "negative":
    total_bill *= 0.90

print(f"{total_bill:.2f}")
