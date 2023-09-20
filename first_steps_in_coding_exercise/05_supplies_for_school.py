PENS_PRICE = 5.80
MARKERS_PRICE = 7.20
CLEANING_SPRAY_PRICE_PER_LITER = 1.20

pens = int(input())
markers = int(input())
cleaning_spray_liters = int(input())
discount_percent = int(input()) / 100

bill = (pens * PENS_PRICE + markers * MARKERS_PRICE + cleaning_spray_liters * CLEANING_SPRAY_PRICE_PER_LITER)
bill_with_discount = bill - (bill * discount_percent)

print(bill_with_discount)