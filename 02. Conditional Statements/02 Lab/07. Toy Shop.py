puzzle = 2.60
doll = 3
bear = 4.10
minion = 8.20
truck = 2

travel = float(input())
puzzle_count = int(input())
doll_count = int(input())
bear_count = int(input())
minion_count = int(input())
truck_count = int(input())

all_toys_income = (puzzle * puzzle_count) + (doll * doll_count) + (bear * bear_count) + (minion * minion_count) + (
        truck * truck_count)

if puzzle_count + doll_count + bear_count + minion_count + truck_count >= 50:
    discount: float = all_toys_income * 0.25
else:
    discount = 0
rent = (all_toys_income - discount) * 0.10
total = all_toys_income - rent - discount
if total >= travel:
    print(f'Yes! {total - travel:.2f} lv left.')
else:
    print(f'Not enough money! {abs(travel - total):.2f} lv needed.')

# we make it clap
