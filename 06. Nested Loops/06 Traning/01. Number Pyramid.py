n = int(input())
is_true = False
current = 1
for row in range(1, n + 1):
    for column in range(1, row + 1):
        if current > n:
            is_true = True
            break
        print(f"{current}", end=" ")
        current += 1
    if is_true:
        break
    print()
