flowers_type = input()
flowers_amount = int(input())
budget = int(input())
cost = 0
if flowers_type == "Roses" and flowers_amount <= 80:
    cost = flowers_amount * 5
elif flowers_type == "Roses" and flowers_amount > 80:
    cost = (flowers_amount * 5) * 0.90
if flowers_type == "Dahlias" and flowers_amount <= 90:
    cost = flowers_amount * 3.80
elif flowers_type == "Dahlias" and flowers_amount > 90:
    cost = (flowers_amount * 3.80) * 0.85
if flowers_type == "Tulips" and flowers_amount <= 80:
    cost = flowers_amount * 2.80
elif flowers_type == "Tulips" and flowers_amount > 80:
    cost = (flowers_amount * 2.80) * 0.85
if flowers_type == "Narcissus" and flowers_amount < 120:
    cost = (flowers_amount * 3) * 1.15
elif flowers_type == "Narcissus" and flowers_amount >= 120:
    cost = flowers_amount * 3
if flowers_type == "Gladiolus" and flowers_amount < 80:
    cost = (flowers_amount * 2.5) * 1.20
elif flowers_type == "Gladiolus" and flowers_amount >= 80:
    cost = flowers_amount * 2.5
if budget >= cost:
    print(f"Hey, you have a great garden with {flowers_amount} {flowers_type} and {(budget - cost):.2f} leva left.")
elif budget < cost:
    print(f"Not enough money, you need {abs(budget - cost):.2f} leva more.")
