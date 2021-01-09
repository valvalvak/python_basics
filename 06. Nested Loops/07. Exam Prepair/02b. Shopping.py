budget = float(input())
agp_amount = int(input())
cpu_amount = int(input())
ram_amount = int(input())

agp_price = agp_amount * 250
cpu_price = agp_price * 0.35 * cpu_amount
ram_price = agp_price * 0.10 * ram_amount

total_sum = agp_price + cpu_price + ram_price

if agp_amount > cpu_amount:
    total_sum *= 0.85

diff = abs(budget - total_sum)

if budget >= total_sum:
    print(f"You have {diff:.2f} leva left!")
else:
    print(f"Not enough money! You need {diff:.2f} leva more!")
