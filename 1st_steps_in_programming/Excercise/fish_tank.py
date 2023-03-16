length = int(input())
width = int(input())
height = int(input())
percent_from_all = float(input()) / 100
# all input data is in CM
tank_volume = (length * width * height) / 1000  # convert to DM3/L
buffer_filling = tank_volume * percent_from_all
usable_volume = tank_volume - buffer_filling

print(usable_volume)
