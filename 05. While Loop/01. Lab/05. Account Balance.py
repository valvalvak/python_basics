value = input()
total = 0
increase = 0
while value != "NoMoreMoney":
    increase = float(value)
    if increase < 0:
        print("Invalid operation!")
        break
    print(f"Increase: {increase:.2f}")
    total += increase
    value = input()
print(f"Total: {float(total):.2f}")

# the following is test to get int from str, made by me: Val.Val.Vak.
# test = input()
# get_number = 0
# while test != "vaki":
#     get_number += int(test)
#     print(test)
#     test = input()
# print(f"You've got int from test{get_number:.2f}!")
