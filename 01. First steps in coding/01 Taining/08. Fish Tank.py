length = int(input())
width = int(input())
height = int(input())
percentage = float(input())
tank_vol = length * width * height
tank_liters = tank_vol * 0.001
percent = percentage * 0.01
liters = tank_liters * (1 - percent)
print(liters)
