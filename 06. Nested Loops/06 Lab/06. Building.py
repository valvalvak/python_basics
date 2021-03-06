all_flours = int(input())
rooms_on_flour = int(input())
for current_flour in range(all_flours, 0, - 1):
    for room_number in range(0, rooms_on_flour):
        if current_flour == all_flours:
            print(f"L{current_flour}{room_number}", end=" ")
        elif current_flour % 2 == 0:
            print(f"O{current_flour}{room_number}", end=" ")
        elif current_flour % 2 != 0:
            print(f"A{current_flour}{room_number}", end=" ")
    print()
