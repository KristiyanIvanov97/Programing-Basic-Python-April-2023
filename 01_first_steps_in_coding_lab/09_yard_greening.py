Discount = 18 / 100
Price_Per_Sqr_Meter = 7.61

sqr_meters = float(input())

bill = sqr_meters * Price_Per_Sqr_Meter
total_discount = bill * Discount
total_bill = bill - total_discount

print(f"The final price is: {total_bill} lv.")
print(f"The discount is: {total_discount} lv.")