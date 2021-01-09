width = int(input())
length = int(input())
height = int(input())
new_house = width * length * height
variable = input()
while variable != "Done":
    inventory_boxes = int(variable)
    new_house -= inventory_boxes
    if new_house < 0:
        print(f"No more free space! You need {abs(new_house)} Cubic meters more.")
        break
    variable = input()
else:
    print(f"{abs(new_house)} Cubic meters left.")