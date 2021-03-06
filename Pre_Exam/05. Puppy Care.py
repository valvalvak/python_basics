target_food = int(input()) * 1000
command = int(input())
food_eaten = 0
while command != "Adopted":
    current_food = int(command)
    food_eaten += current_food
    command = input()

if food_eaten <= target_food:
    print(f"Food is enough! Leftovers: {abs(food_eaten - target_food)} grams.")
else:
    print(f"Food is not enough. You need {abs(food_eaten - target_food)} grams more.")
