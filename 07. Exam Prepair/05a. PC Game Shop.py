n = int(input())
Hearthstone = 0
Fornite = 0
Overwatch = 0
Others = 0

if n == 0:
    sys: exit(0)

for games_sold in range(n):
    current_game = str(input())
    if current_game == "Hearthstone":
        Hearthstone += 1
    elif current_game == "Fornite":
        Fornite += 1
    elif current_game == "Overwatch":
        Overwatch += 1
    else:
        Others += 1

print(f"Hearthstone - {Hearthstone * 100 / n:.2f}%\n"
      f"Fornite - {Fornite * 100 / n:.2f}%\n"
      f"Overwatch - {Overwatch * 100 / n:.2f}%\n"
      f"Others - {Others * 100 / n:.2f}%")
