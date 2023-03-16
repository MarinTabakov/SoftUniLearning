veggies_price = float(input()) / 1.94
fruits_price = float(input()) / 1.94
total_kilos_veggies = int(input())
total_kilos_fruits = int(input())

total_price = (veggies_price * total_kilos_veggies) + (fruits_price * total_kilos_fruits)

print(f'{total_price:.2f}')

