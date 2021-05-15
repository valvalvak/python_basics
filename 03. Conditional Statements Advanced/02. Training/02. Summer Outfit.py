outside_degrees = int(input())
part_of_the_day = input()
outfit = ""
shoes = ""
if part_of_the_day == "Morning" and 10 <= outside_degrees <= 18:
    outfit = "Sweatshirt"
    shoes = "Sneakers"
elif part_of_the_day == "Morning" and 18 < outside_degrees <= 24:
    outfit = "Shirt"
    shoes = "Moccasins"
elif part_of_the_day == "Morning" and outside_degrees >= 25:
    outfit = "T-Shirt"
    shoes = "Sandals"
elif part_of_the_day == "Afternoon" and 10 <= outside_degrees <= 18:
    outfit = "Shirt"
    shoes = "Moccasins"
elif part_of_the_day == "Afternoon" and 18 < outside_degrees <= 24:
    outfit = "T-Shirt"
    shoes = "Sandals"
elif part_of_the_day == "Afternoon" and outside_degrees >= 25:
    outfit = "Swim Suit"
    shoes = "Barefoot"
elif part_of_the_day == "Evening":
    outfit = "Shirt"
    shoes = "Moccasins"
print(f"It's {outside_degrees} degrees, get your {outfit} and {shoes}.")
