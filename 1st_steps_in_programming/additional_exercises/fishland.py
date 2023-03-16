mackerel_price = float(input())  # skumriq cena
sprinkle_price = float(input())  # caca cena
bonito_kilos = float(input())  # palamud obshto kilogrami
scad_kilo = float(input())  # safrid
mussels_kilo = int(input())  # midi obshto kilogrami

bonito_price = mackerel_price * 1.60  # palamud cena/kg
scad_price = sprinkle_price * 1.8  # safrdi cena/kg
mussels_price = 7.5  # cena na midi

total_price = (bonito_kilos * bonito_price) + (scad_kilo * scad_price) + (mussels_kilo * mussels_price)
print(f'{total_price:.2f}')

