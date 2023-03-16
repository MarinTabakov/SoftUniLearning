num_pencils = int(input())
num_markers = int(input())
liters_cleaner = int(input())
discount = int(input()) / 100

pencils_price = 5.80 * num_pencils
marker_price = 7.20 * num_markers
cleaner_price = 1.20 * liters_cleaner
price_for_all_mat = pencils_price + marker_price + cleaner_price
price_with_disc = price_for_all_mat - (price_for_all_mat * discount)

print(price_with_disc)







