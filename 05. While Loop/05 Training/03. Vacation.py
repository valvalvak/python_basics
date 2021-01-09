money_needed = float(input())
money_she_got = float(input())
days_counter = 0
spending_counter = 0
while money_she_got < money_needed and spending_counter < 5:
    command = input()
    money = float(input())
    days_counter += 1
    if command == "save":
        spending_counter = 0
        money_she_got += money
    elif command == "spend":
        spending_counter += 1
        money_she_got -= money
        if money_she_got < 0:
            money_she_got = 0
if spending_counter == 5:
    print(f"You can't save the money.\n"
          f"{days_counter}")
if money_she_got >= money_needed:
    print(f"You saved the money for {days_counter} days.")