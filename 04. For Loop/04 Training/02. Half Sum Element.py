import sys

n = int(input())
values_sum = 0
greatest_number = -sys.maxsize
for loop in range(0, n):
    value = int(input())
    if value > greatest_number:
        greatest_number = value
    values_sum += value

difference = abs(greatest_number - (values_sum - greatest_number))

if greatest_number == values_sum - greatest_number:
    print(f"Yes\n"
          f"Sum = {greatest_number}")
else:
    print(f"No\n"
          f"Diff = {difference}")
