current_gamer = input()
best_player_points = 0
best_player = ""

while current_gamer != "Stop":
    current_points = 0
    for character in current_gamer:
        number = int(input())
        if number == ord(character):
            current_points += 10
        else:
            current_points += 2
    last_gamer = current_gamer
    current_gamer = input()

print(f"The winner is {best_player} with {best_player_points} points!")
