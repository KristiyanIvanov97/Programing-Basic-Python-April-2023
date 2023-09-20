tax_per_year = int(input())

shoes = tax_per_year - (tax_per_year * 0.40)
basketball_wear = shoes - (shoes * 0.20)
basketball_ball = basketball_wear * 0.25
basketball_accessories = basketball_ball * 0.20

total_sum = tax_per_year + shoes + basketball_accessories + basketball_ball + basketball_wear

print(total_sum)