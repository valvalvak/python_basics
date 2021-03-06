n = int(input())
m = int(input())
s = int(input())
if m == 0 and s == 0:
    sys: exit(0)
for address in range(m, n, -1):
    if address % 2 == 0 and address % 3 == 0 and address != s:
        if address == s:
            sys: exit(0)
        print(f"{address}", end=" ")