nylon = int(input()) + 2
paint = int(input()) * 1.10
thinner = int(input())
hours = int(input())

nylon_cost = nylon * 1.5
paint_cost = paint * 14.50
thinner_cost = thinner * 5

materials_cost = nylon_cost + paint_cost + thinner_cost + 0.40
workers_salary = materials_cost * hours * 0.30
total_expenses = materials_cost + workers_salary

print(f"Total expenses: {total_expenses:.2f} lv.")
