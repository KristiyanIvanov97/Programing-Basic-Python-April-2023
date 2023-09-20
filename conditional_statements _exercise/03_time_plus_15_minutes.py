# Да се напише програма, която чете час и минути от 24-часово денонощие, въведени от потребителя и изчислява колко ще е часът след 15 минути.
# Резултатът да се отпечата във формат часове:минути. Часовете винаги са между 0 и 23, а минутите винаги са между 0 и 59.
# Часовете се изписват с една или две цифри.
# Минутите се изписват винаги с по две цифри, с водеща нула, когато е необходимо.

hour = int(input())
minute = int(input())

future_minute = (minute + 15) % 60
future_hour = (hour + (minute + 15) // 60) % 24

if future_minute < 10:
    print(f"{future_hour}:0{future_minute}")
else:
    print(f"{future_hour}:{future_minute}")
















#
#     print(f"{hour}:{extra_minutes}")

# hour = int(input())
# minute = int(input())
#
# # изчисляваме бъдещия час и минути
# future_minute = (minute + 15) % 60
# future_hour = (hour + (minute + 15) // 60) % 24
#
# # извеждаме резултата в желания формат
# print(f"{future_hour}:{future_minute:02d}")