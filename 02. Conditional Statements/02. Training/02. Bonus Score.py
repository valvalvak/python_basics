points = int(input())
bonus = 0
if points <= 100:
    bonus += 5
elif points > 1000:
    bonus = points * 0.1
else:
    bonus = points * 0.2
if points % 2 == 0:
    bonus = bonus + 1
elif points % 10 == 5:
    bonus = bonus + 2
print(f"{bonus}")
print(f"{points + bonus}")
