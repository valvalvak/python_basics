current_team_name = input()
current_season_gameplay = int(input())

if current_season_gameplay <= 0:
    print(f"{current_team_name} hasn't played any games during this season.")
    sys: exit(0)

points_won = 0
wins = 0
draw = 0
loses = 0

for current_game in range(current_season_gameplay):
    game_result = input()
    if game_result == "W":
        points_won += 3
        wins += 1
    elif game_result == "D":
        points_won += 1
        draw += 1
    elif game_result == "L":
        loses += 1

print(f"{current_team_name} has won {points_won} points during this season.\n"
      f"Total stats:\n"
      f"## W: {wins}\n"
      f"## D: {draw}\n"
      f"## L: {loses}\n"
      f"Win rate: {wins / current_season_gameplay * 100:.2f}%")
