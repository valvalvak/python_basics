import math

average_speed = float(input())
fuel_per_100km = float(input())

distance = 384400 * 2
time = math.ceil(distance / average_speed) + 3
fuel = fuel_per_100km * distance / 100

print(f"{time}\n"
      f"{int(fuel)}")
