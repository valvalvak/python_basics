n = int(input())
left = 0
right = 0
for numbers in range(1, n + 1):
    value = int(input())
    left += value
for numbers in range(1, n + 1):
    value = int(input())
    right += value
if left == right:
    print(f"Yes, sum = {left}")
else:
    print(f"No, diff = {abs(right - left)}")
