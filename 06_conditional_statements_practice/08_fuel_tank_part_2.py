GASOLINE = 2.22
DIESEL = 2.33
GAS = 0.93
GASOLINE_DISCOUNT = 0.18
DIESEL_DISCOUNT = 0.12
GAS_DISCOUNT = 0.08

fuel_type = input()
fuel_amount = float(input())
card_for_discount = input()

if fuel_type == "Diesel":
    if card_for_discount == "Yes":
        diesel_with_discount = DIESEL - DIESEL_DISCOUNT
        price_for_total_amount = fuel_amount * diesel_with_discount
    else:
        price_for_total_amount = fuel_amount * DIESEL
    if fuel_amount > 20 and fuel_amount <= 25:
        price_for_total_amount_with_discount = price_for_total_amount * 0.92
    elif fuel_amount > 25:
        price_for_total_amount_with_discount = price_for_total_amount * 0.90
    else:
        price_for_total_amount_with_discount = price_for_total_amount
    print(f"{price_for_total_amount_with_discount:.2f} lv.")

if fuel_type == "Gasoline":
    if card_for_discount == "Yes":
        gasoline_with_discount = GASOLINE - GASOLINE_DISCOUNT
        price_for_total_amount = fuel_amount * gasoline_with_discount
    else:
        price_for_total_amount = fuel_amount * GASOLINE
    if fuel_amount > 20 and fuel_amount <= 25:
        price_for_total_amount_with_discount = price_for_total_amount * 0.92
    elif fuel_amount > 25:
        price_for_total_amount_with_discount = price_for_total_amount * 0.90
    else:
        price_for_total_amount_with_discount = price_for_total_amount
    print(f"{price_for_total_amount_with_discount:.2f} lv.")

if fuel_type == "Gas":
    if card_for_discount == "Yes":
        gas_with_discount = GAS - GAS_DISCOUNT
        price_for_total_amount = fuel_amount * gas_with_discount
    else:
        price_for_total_amount = fuel_amount * GAS
    if fuel_amount > 20 and fuel_amount <= 25:
        price_for_total_amount_with_discount = price_for_total_amount * 0.92
    elif fuel_amount > 25:
        price_for_total_amount_with_discount = price_for_total_amount * 0.90
    else:
        price_for_total_amount_with_discount = price_for_total_amount
    print(f"{price_for_total_amount_with_discount:.2f} lv.")
