VIP = 499.99
Normal_ticket_price = 249.99

budget = float(input())
tickets_category = input()
people = int(input())
transport = 0
total_tickets_price = 0

if 1 <= people <= 4:
    transport = budget * 0.75
elif 5 <= people <= 9:
    transport = budget * 0.60
elif 10 <= people <= 24:
    transport = budget * 0.50
elif 25 <= people <= 49:
    transport = budget * 0.40
else:
    transport = budget * 0.25

if tickets_category == "VIP":
    total_tickets_price = people * VIP
elif tickets_category == "Normal":
    total_tickets_price = people * Normal_ticket_price

if budget > total_tickets_price + transport:
    print(f"Yes! You have {budget - (total_tickets_price + transport) :.2f} leva left.")
else:
    print(f"Not enough money! You need {(total_tickets_price + transport) - budget :.2f} leva.")



