import sys

target = float(input())
command = input()

total_income = 0

while command != "Party!":
    cocktail_type = command
    cocktails_count = int(input())
    current_income = len(cocktail_type) * cocktails_count
    if current_income % 2 != 0:
        current_income *= 0.75
    total_income += current_income
    if total_income >= target:
        print("Target acquired.")
        print(f"Club income - {total_income:.2f} leva.")
        sys.exit(0)
    command = input()
print(f"We need {abs(target - total_income):.2f} leva more.")
print(f"Club income - {total_income:.2f} leva.")
