nylon_sq_m = int(input())
paint_liters = int(input())
thinner_liters = int(input())
hours_needed = int(input())

price_nylon = (nylon_sq_m + 2) * 1.50
price_paint = (paint_liters * 1.1) * 14.50
price_thinner = thinner_liters * 5

materials_total = price_nylon + price_paint + price_thinner + 0.40
workers_salaries = materials_total * 0.3
total_inc_salaries = materials_total + (workers_salaries * hours_needed)

print(total_inc_salaries)
