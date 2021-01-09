import sys

location = input()
package = input()
vip_discount = input()
days = int(input())

if days <= 0:
    print("Days must be positive number!")
    sys.exit(0)

price_per_day = 0
discount = 0

if location == "Bansko" or location == "Borovets":
    if package == "noEquipment":
        price_per_day = 80
        discount = 0.05
    elif package == "withEquipment":
        price_per_day = 100
        discount = 0.10
    else:
        print("Invalid input!")
        sys.exit(0)
elif location == "Varna" or location == "Burgas":
    if package == "noBreakfast":
        price_per_day = 100
        discount = 0.07
    elif package == "withBreakfast":
        price_per_day = 130
        discount = 0.12
    else:
        print("Invalid input!")
        sys.exit(0)
else:
    print("Invalid input!")
    sys.exit(0)

if vip_discount == "yes":
    price_per_day -= price_per_day * discount

if days > 7:
    days -= 1

total_sum = price_per_day * days

print(f"The price is {total_sum:.2f}lv! Have a nice time!")