target = 10000
steps = 0
goal = False
command = input()
while command != "Going home":
    steps_increase = int(command)
    steps += steps_increase
    if steps >= target:
        goal = True
        break
    command = input()
if command == "Going home":
    home_steps = int(input())
    steps += home_steps
    if steps >= target:
        goal = True
more_or_less = abs(target - steps)
if goal:
    print(f"Goal reached! Good job!\n"
          f"{more_or_less} steps over the goal!")
else:
    print(f"{more_or_less} more steps to reach goal.")
