import math

amount_people = int(input())
enter_prise = float(input())
sunbed_price = float(input())
umbrella_price = float(input())

umbrellas = math.ceil(amount_people / 2)
sunbeds = math.ceil(amount_people * 0.75)
total_sum = amount_people * enter_prise + umbrellas * umbrella_price + sunbeds * sunbed_price

print(f"{total_sum:.2f} lv.")
