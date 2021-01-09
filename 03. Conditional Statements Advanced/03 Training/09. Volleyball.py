year_type = input()
holidays = int(input())
home_play = int(input())
weekends = 48
city_play = (weekends - home_play) * 3 / 4 + holidays * 2 / 3
games = city_play + home_play
if year_type == "leap":
    games *= 1.15
print(f"{int(games)}")
