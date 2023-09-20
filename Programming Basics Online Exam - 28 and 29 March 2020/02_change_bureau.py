bitcoin_amount = int(input())
chinese_yuan_amount = float(input())
commission = float(input())

bitcoin_price_in_bgn = 1168
yuan_price_in_bgn = 0.15 * 1.76

total_sum_in_euro = (bitcoin_amount * bitcoin_price_in_bgn + chinese_yuan_amount * yuan_price_in_bgn) / 1.95
commission_amount = commission / 100 * total_sum_in_euro

total_sum_with_commission = total_sum_in_euro - commission_amount
print(f"{total_sum_with_commission:.2f}")