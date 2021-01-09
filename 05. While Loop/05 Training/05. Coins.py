change = float(input())
change = int(change * 100)
coins_count = 0
coins_count += change // 200
change = change % 200
coins_count += change // 100
change = change % 100
coins_count += change // 50
change = change % 50
coins_count += change // 20
change = change % 20
coins_count += change // 10
change = change % 10
coins_count += change // 5
change = change % 5
coins_count += change // 2
change = change % 2
if change == 1:
    coins_count += 1
print(int(coins_count))