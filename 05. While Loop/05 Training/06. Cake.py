cake_side_a = int(input())
cake_side_b = int(input())
cake_pieces = cake_side_a * cake_side_b
not_enough = False
value = input()
while value != "STOP":
    pieces_taken = int(value)
    cake_pieces -= pieces_taken
    if cake_pieces < 0:
        not_enough = True
        break
    value = input()
if not_enough:
    print(f"No more cake left! You need {abs(cake_pieces)} pieces more.")
else:
    print(f"{cake_pieces} pieces are left.")
