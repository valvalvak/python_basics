import sys

value = input()
max_number = -sys.maxsize
while_limit = sys.maxsize
while value != "Stop":
    if max_number < int(value):
        max_number = int(value)
    if max_number == while_limit:
        break
    value = input()
print(max_number)
