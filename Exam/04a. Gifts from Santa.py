n = int(input())
m = int(input())
s = int(input())
if 0 > n > m and n > n > 10000 and n > s > m:
    sys: exit(0)
for address in range(m, n, -1):
    if address % 2 == 0 and address % 3 == 0:
        if address == s:
            break
        else:
            print(f"{address}", end=" ")