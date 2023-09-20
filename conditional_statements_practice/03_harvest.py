from math import ceil, floor

vineyard = int(input())
grape = float(input())
wine_liters_needed = int(input())
workers_count = int(input())

grape_used_in_sqr_meter = vineyard * 0.40
grape_used_in_kg = grape_used_in_sqr_meter * grape
total_wine = grape_used_in_kg / 2.5

if wine_liters_needed > total_wine:
    print(f"It will be a tough winter! More {floor(wine_liters_needed - total_wine)} liters wine needed.")
elif total_wine >= wine_liters_needed:
    print(f"Good harvest this year! Total wine: {floor(total_wine)} liters.")
    wine_for_workers = (total_wine - wine_liters_needed) / workers_count
    print(f"{ceil(total_wine - wine_liters_needed)} liters left -> {ceil(wine_for_workers)} liters per person.")


