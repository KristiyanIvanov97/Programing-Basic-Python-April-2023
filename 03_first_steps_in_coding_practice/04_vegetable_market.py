#     • Първи ред – Цена за килограм зеленчуци – реално число[0.00… 1000.00]
#     • Втори ред – Цена за килограм плодове – реално число[0.00… 1000.00]
#     • Трети ред – Общо килограми на зеленчуците – цяло число[0… 1000]
#     • Четвърти ред – Общо килограми на плодовете – цяло число[0… 1000]
# Изход
# Да се отпечата на конзолата едно число: приходите от всички плодове и зеленчуци в евро.
# Резултата да се форматира до втория знак след десетичния разделител.

vegetables_price_per_kilo = float(input())
fruits_price_per_kilo = float(input())
total_vegetables_kilos = int(input())
total_fruits_kilos = int(input())

bill_in_lv = total_vegetables_kilos * vegetables_price_per_kilo + total_fruits_kilos * fruits_price_per_kilo
bill_in_euro = bill_in_lv / 1.94

print(f"{bill_in_euro:.2f}")