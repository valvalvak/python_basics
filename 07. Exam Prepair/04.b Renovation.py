import math
import sys

wall_height = int(input())
wall_width = int(input())
miss_painted_percentage = int(input()) / 100

windows_area = wall_width * wall_height * 4 * miss_painted_percentage
all_walls_area = math.ceil((wall_height * wall_width * 4) - windows_area)

area_painted = 0
diff = 0

command = input()

while command != "Tired!":
    liters_painted = int(command)
    area_painted += liters_painted
    diff = abs(all_walls_area - area_painted)
    if all_walls_area - area_painted == 0:
        print(f"All walls are painted! Great job, Pesho!")
        sys.exit(0)
    elif all_walls_area < area_painted:
        print(f"All walls are painted and you have {int(diff)} l paint left!")
        sys.exit(0)
    command = input()
print(f"{int(diff)} quadratic m left.")
