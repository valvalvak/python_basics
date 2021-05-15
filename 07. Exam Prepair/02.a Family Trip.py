budget = float(input())
nights = int(input())
bed_price = float(input())
extra_budget_percentage = int(input()) / 100

if nights > 7:
    bed_price *= 0.95

total_cost = nights * bed_price + budget * extra_budget_percentage

if budget >= total_cost:
    print(f"Ivanovi will be left with {abs(budget - total_cost):.2f} leva after vacation.")
else:
    print(f"{abs(budget - total_cost):.2f} leva needed.")
