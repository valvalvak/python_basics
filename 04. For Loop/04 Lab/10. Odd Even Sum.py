n = int(input())
even_value = 0
odd_value = 0
for value in range(1, n + 1):
    number = int(input())
    if value % 2 == 0:
        even_value += number
    else:
        odd_value += number
if even_value == odd_value:
    print(f"Yes\n"
          f"Sum = {even_value}")
difference = abs(even_value - odd_value)
if even_value != odd_value:
    print(f"No\n"
          f"Diff = {difference}")
