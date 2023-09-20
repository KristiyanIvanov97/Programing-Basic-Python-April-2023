# mackerel = skumriya
# sprinkle = caca
# bonito = palamud
# saffron = safrid
# mussels = midi
MUSSELS_PRICE = 7.50

mackerel = float(input())
sprinkle = float(input())
bonito = float(input())
saffron = float(input())
mussels = int(input())

bonito_price = mackerel + (mackerel * 0.60)
saffron_price = sprinkle + (sprinkle * 0.80)

bill = bonito * bonito_price + saffron * saffron_price + mussels * MUSSELS_PRICE

print(f"{bill:.2f}")
