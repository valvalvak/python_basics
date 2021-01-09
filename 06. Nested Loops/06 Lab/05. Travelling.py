destination = input()
while destination != "End":
    destination_cost = float(input())
    saved_money = 0
    while saved_money < destination_cost:
        income = float(input())
        saved_money += income
    print(f"Going to {destination}!")
    destination = input()