sq_meters = float(input())
price_per_sq = 7.61
discount = 0.18
total_price = sq_meters * price_per_sq
discount_value = total_price * discount
price_after_discount = total_price - discount_value
print(f'The final price is: {price_after_discount} lv.')
print(f'The discount is: {discount_value} lv.')
