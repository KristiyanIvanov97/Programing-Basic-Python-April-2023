ROOM_FOR_ONE_PERSON = 18
APARTMENT = 25
PRESIDENT_APARTMENT = 35

days = int(input())
room = input()
rating = input()
discount = 0
total_sum = 0
rating_discount = 0

if room == "room for one person":
    total_sum = ROOM_FOR_ONE_PERSON * (days - 1)

if room == "apartment":
    if days < 10:
        discount = 0.70
    elif 10 < days < 15:
        discount = 0.65
    elif days > 15:
        discount = 0.50

    total_sum = APARTMENT * (days - 1) * discount

elif room == "president apartment":
    if days < 10:
        discount = 0.90
    elif 10 < days < 15:
        discount = 0.85
    elif days > 15:
        discount = 0.80

    total_sum = PRESIDENT_APARTMENT * (days - 1) * discount

if rating == "positive":
    total_sum *= 1.25
else:
    total_sum *= 0.9

print(f"{total_sum:.2f}")




