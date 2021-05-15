n = int(input())
m = int(input())
s = int(input())
for address in range(m, n, -1):
    if address % 2 == 0 and address % 3 == 0:
        bad_robot = address
        if bad_robot == s:
            sys: exit(0)
    if address % 2 == 0 and address % 3 == 0:
        if address != s:
            print(f"{address}", end=" ")
