w = float(input()) * 100
h = (float(input()) * 100) - 100
lost_places = 3
# work_place_face = 70 х 120
from math import floor
sits_on_a_row = floor(h / 70)
rows_in_the_room = floor(w / 120)
sits_available = sits_on_a_row * rows_in_the_room - 3
print(sits_available)




