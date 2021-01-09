period = int(input())
cooks = int(input())
cakes = int(input())
waffles = int(input())
pancakes = int(input())
cakes_income = cakes * 45
waffles_income = waffles * 5.80
pancakes_income = pancakes * 3.20
charity_income = (cakes_income + waffles_income + pancakes_income) * cooks * period
deduction = charity_income * 1 / 8
total = charity_income - deduction
print(total)
