w = float(input()) * 100
h = (float(input()) * 100) - 100
one_place = 120 * 70
print(one_place)
lost_places = 3 * one_place
print(lost_places)
room_face = w * h
print(room_face)
available_sits = (room_face - lost_places) / one_place

print(available_sits)

