screen = input()  # Premiere     Normal      Discount
rows = int(input())
columns = int(input())
seats = rows * columns
income = 0
if screen == "Premiere":  # premiere = 12.00
    income = seats * 12.00
    print(f"{income:.2f} leva")
elif screen == "Normal":  # normal = 7.50
    income = seats * 7.50
    print(f"{income:.2f} leva")
elif screen == "Discount":  # discount = 7.50
    income = seats * 5.00
    print(f"{income:.2f} leva")
