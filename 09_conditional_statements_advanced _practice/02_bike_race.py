junior_cyclist = int(input())
senior_cyclist = int(input())
trace_type = input()
participation_fee = 0
cross_country_discount = 0
junior_tax = 0
senior_tax = 0
expenses = 0.95

if trace_type == "trail":
    junior_tax = 5.50
    senior_tax = 7
    participation_fee = (senior_cyclist * senior_tax + junior_cyclist * junior_tax) * expenses
elif trace_type == "cross-country":
    junior_tax = 8
    senior_tax = 9.50
    participation_fee = senior_cyclist * senior_tax + junior_cyclist * junior_tax
    if senior_cyclist + junior_cyclist > 50:
        participation_fee *= 0.75 * expenses   # participation_fee = participation_fee * 0.75 * expenses
    else:
        participation_fee = (senior_cyclist * senior_tax + junior_cyclist * junior_tax) * expenses
elif trace_type == "downhill":
    junior_tax = 12.25
    senior_tax = 13.75
    participation_fee = (senior_cyclist * senior_tax + junior_cyclist * junior_tax) * expenses
elif trace_type == "road":
    junior_tax = 20
    senior_tax = 21.50
    participation_fee = (senior_cyclist * senior_tax + junior_cyclist * junior_tax) * expenses

print(f"{participation_fee:.2f}")

