n = int(input())
for number in range(1111, 10000):
    flag = True
    number_as_str = str(number)
    for digit in number_as_str:
        if int(digit) == 0 or n % int(digit) != 0:
            flag = False
            break
    if flag:
        print(f"{number_as_str}", end=" ")