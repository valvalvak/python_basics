n = int(input())
p1 = 0
p2 = 0
p3 = 0
p4 = 0
p5 = 0
for loop in range(n):
    value = int(input())
    if value < 200:
        p1 += 1
    elif value <= 399:
        p2 += 1
    elif value <= 599:
        p3 += 1
    elif value <= 799:
        p4 += 1
    elif value >= 800:
        p5 += 1
print(f"{p1 / n * 100:.2f}%")
print(f"{p2 / n * 100:.2f}%")
print(f"{p3 / n * 100:.2f}%")
print(f"{p4 / n * 100:.2f}%")
print(f"{p5 / n * 100:.2f}%")
