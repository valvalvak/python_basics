budget = float(input())
crew = int(input())
wardrobe = float(input())
decor = budget * 0.1
costumes = crew * wardrobe
if crew > 150:
    costumes *= 0.9
# 	Ако  парите за декора и дрехите са повече от бюджета:
if (decor + costumes) > budget:
    print(f"Not enough money!\n"
          f"Wingard needs {abs(budget - decor - costumes) :.2f} leva more.")
#  Ако парите за декора и дрехите са по малко или равни на бюджета:
if (decor + costumes) <= budget:
    print(f"Action!\n"
          f"Wingard starts filming with {budget - decor - costumes :.2f} leva left.")
