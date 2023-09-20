NYLON_PER_SQR_METER = 1.50
PAINT = 14.50
PAINT_THINNER = 5
EXTRA_NYLON = 2
BAGS = 0.40

nylon = int(input())
paint_liters = int(input())
paint_thinner_liters = int(input())
hours_for_the_job = int(input())
extra_paint = paint_liters * 0.10

bill = (nylon + EXTRA_NYLON) * NYLON_PER_SQR_METER + (paint_liters + extra_paint) * PAINT + paint_thinner_liters * PAINT_THINNER + BAGS
money_for_work_per_hour = bill * 0.30
total_bill = bill + money_for_work_per_hour * hours_for_the_job

print(total_bill)