number_a = int(input())
number_b = int(input())
magic_number = int(input())
counter = 0
did_got_magic = False
for value_a in range(number_a, number_b + 1):
    for value_b in range(number_a, number_b + 1):
        counter += 1
        if value_a + value_b == magic_number:
            print(f"Combination N:{counter} ({value_a} + {value_b} = {magic_number})")
            did_got_magic = True
            break
    if did_got_magic:
        break
else:
    print(f"{counter} combinations - neither equals {magic_number}")
