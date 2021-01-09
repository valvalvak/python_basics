import sys

n = int(input())
maximum = -sys.maxsize
minimum = sys.maxsize
for numbers in range(1, n + 1):
    values = int(input())
    if values > maximum:
        maximum = values
    if values < minimum:
        minimum = values
print(f"Max number: {maximum}")
print(f"Min number: {minimum}")
