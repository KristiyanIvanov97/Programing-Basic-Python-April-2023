VIDEO_CARD_PRICE = 250

budget = float(input())
video_card_amount = int(input())
processor_amount = int(input())
ram_amount = int(input())

processor_price = 0.35 * (VIDEO_CARD_PRICE * video_card_amount)
ram_price = 0.10 * (VIDEO_CARD_PRICE * video_card_amount)

total_price = video_card_amount * VIDEO_CARD_PRICE + processor_amount * processor_price + ram_amount * ram_price

if video_card_amount > processor_amount:
    total_price *= 0.85

if budget > total_price:
    print(f"You have {budget - total_price :.2f} leva left!")
elif budget <= total_price:
    print(f"Not enough money! You need {total_price - budget :.2f} leva more!")

