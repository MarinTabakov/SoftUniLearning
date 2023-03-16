deposit_sum = int(input())
deposit_time = int(input())
year_interest = float(input())

sum_at_end = deposit_sum + deposit_time * (deposit_sum * (year_interest / 100 / 12))

print(sum_at_end)
