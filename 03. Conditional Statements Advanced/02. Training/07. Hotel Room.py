month = input()
nights = int(input())
studio = 0
apartment = 0
bill = 0
if month == "May" or month == "October":
    studio = 50
    apartment = 65
    if 7 < nights < 14:
        studio *= 0.95
    elif nights > 14:
        studio *= 0.70
elif month == "June" or month == "September":
    studio = 75.20
    apartment = 68.70
    if nights > 14:
        studio *= 0.8
elif month == "July" or month == "August":
    studio = 76
    apartment = 77
if nights > 14:
    apartment *= 0.9
print(f"Apartment: {apartment * nights:.2f} lv.\nStudio: {studio * nights:.2f} lv.")
