annual_tax = int(input())  # this row should be included in total

shoes_price = annual_tax * 0.6
cloths = shoes_price * 0.8
ball_price = cloths * 0.25
accessories = ball_price * 0.2
total_expenses = shoes_price + cloths + ball_price + accessories + annual_tax

print(total_expenses)
