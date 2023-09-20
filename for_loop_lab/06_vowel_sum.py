text = input()
vowels_sum = 0

for i in range(0, len(text)):
    if text[i] == "a":
        vowels_sum += 1
    if text[i] == "e":
        vowels_sum += 2
    if text[i] == "i":
        vowels_sum += 3
    if text[i] == "o":
        vowels_sum += 4
    if text[i] == "u":
        vowels_sum += 5

print(vowels_sum)


