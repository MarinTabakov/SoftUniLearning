x_height = float(input())
y_lenght = float(input())
h_height_roof = float(input())

square_walls = ((x_height * x_height) * 2) - (1.2 * 2)
rectangle_walls = ((x_height * y_lenght) * 2) - ((1.5 * 1.5) * 2)
green_paint_sq = square_walls + rectangle_walls
green_paint_liters = green_paint_sq / 3.4

roof_triangles_face = ((x_height * h_height_roof) / 2) * 2
roof_rectangles_face = x_height * y_lenght * 2
red_paint_sq = roof_rectangles_face + roof_triangles_face
red_paint_liters = red_paint_sq / 4.3

print(f'{green_paint_liters:.2f}')
print(f'{red_paint_liters:.2f}')