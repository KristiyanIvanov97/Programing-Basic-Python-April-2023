age = int(input())
washing_machine_price = float(input())
toy_price = int(input())

money_for_birthdays = 0
toys_for_birthdays = 0

for birthdays in range(1, age + 1):
    if birthdays % 2 == 0:
        money_for_birthdays += birthdays * 5
        money_for_birthdays -= 1
    else:
        toys_for_birthdays += 1

total_sum = money_for_birthdays + toys_for_birthdays * toy_price

if total_sum >= washing_machine_price:
    print(f"Yes! {total_sum - washing_machine_price :.2f}")
else:
    print(f"No! {washing_machine_price - total_sum :.2f}")
