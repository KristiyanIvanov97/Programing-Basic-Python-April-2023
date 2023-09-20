groups_count = int(input())

total_people = 0
people_for_mussala = 0
people_for_monblan = 0
people_for_kilimanjaro = 0
people_for_k2 = 0
people_for_everest = 0

for _ in range(groups_count):
    people_in_group = int(input())
    if people_in_group <= 5:
        people_for_mussala += people_in_group
    elif people_in_group <= 12:
        people_for_monblan += people_in_group
    elif people_in_group <= 25:
        people_for_kilimanjaro += people_in_group
    elif people_in_group <= 40:
        people_for_k2 += people_in_group
    elif people_in_group >= 40:
        people_for_everest += people_in_group

    total_people += people_in_group

percent_people_for_mussala = people_for_mussala / total_people * 100
percent_people_for_monblan = people_for_monblan / total_people * 100
percent_people_for_kilimanjaro = people_for_kilimanjaro / total_people * 100
percent_people_for_k2 = people_for_k2 / total_people * 100
percent_people_for_everest = people_for_everest / total_people * 100

print(f"{percent_people_for_mussala:.2f}%")
print(f"{percent_people_for_monblan:.2f}%")
print(f"{percent_people_for_kilimanjaro:.2f}%")
print(f"{percent_people_for_k2:.2f}%")
print(f"{percent_people_for_everest:.2f}%")
