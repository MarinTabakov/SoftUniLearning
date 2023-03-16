degrees = float(input())

if degrees > 35:
    print("unknown")
if degrees >= 25:
    if degrees <= 35:
        print("Hot")
elif degrees >= 20.1:
    if degrees <= 25.9:
        print("Warm")
elif degrees >= 15.00:
    if degrees <= 20.00:
        print("Mild")
elif degrees >= 12.00:
    if degrees <= 14.9:
        print("Cool")
elif degrees >= 5.0:
    if degrees <= 11.9:
        print('Cold')
elif degrees <= 4.9:
    print("unknown")


