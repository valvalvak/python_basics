sportsman1 = int(input())
sportsman2 = int(input())
sportsman3 = int(input())
sum_of_time = sportsman1 + sportsman2 + sportsman3
minutes = sum_of_time // 60
seconds = sum_of_time % 60
if seconds < 10:
    print(f"{minutes}:0{seconds}")
else:
    print(f"{minutes}:{seconds}")
