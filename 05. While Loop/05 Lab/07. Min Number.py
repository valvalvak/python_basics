import sys

value = input()
min_number = sys.maxsize
while value != "Stop":
    if min_number > int(value):
        min_number = int(value)
    value = input()
print(min_number)
