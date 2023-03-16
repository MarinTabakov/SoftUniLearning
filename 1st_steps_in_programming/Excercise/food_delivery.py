chicken_meal = int(input())
fish_meal = int(input())
veggie_meal = int(input())
import math
chicken_total = 10.35 * chicken_meal
fish_total = 12.40 * fish_meal
veggie_total = 8.15 * veggie_meal

total = ((chicken_total + fish_total + veggie_total) * 1.2) + 2.50

print(total)



