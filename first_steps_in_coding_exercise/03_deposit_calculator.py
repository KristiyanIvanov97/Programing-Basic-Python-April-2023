deposit_amount = float(input())
deposit_for_months = int(input())
percent_per_year = float(input()) / 100

final_amount = deposit_amount + deposit_for_months * ((deposit_amount * percent_per_year) / 12)

print(final_amount)