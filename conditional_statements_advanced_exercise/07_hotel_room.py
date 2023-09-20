month = input()
number_of_nights = int(input())
studio = 0
apartment = 0
discount = 1
if month == "May" or month == "October":
    studio = 50
    apartment = 65
    if number_of_nights > 14:
        studio = 50 * 0.70
        apartment = 65 * 0.90
    elif number_of_nights > 7:
        studio = 50 * 0.95

elif month == "June" or month == "September":
    studio = 75.20
    apartment = 68.70
    if number_of_nights > 14:
        studio = 75.20 * 0.80
        apartment = 68.70 * 0.90
elif month == "July" or month == "August":
    studio = 76
    apartment = 77
    if number_of_nights > 14:
        apartment = 77 * 0.90

total_sum_studio = number_of_nights * studio
total_sum_apartment = number_of_nights * apartment

print(f"Apartment: {total_sum_apartment:.2f} lv.\nStudio: {total_sum_studio:.2f} lv.")


