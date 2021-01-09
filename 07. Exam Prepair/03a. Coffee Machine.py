type_of_drink = input()
sugar_amount = input()
amount_of_drinks = int(input())

final_sum = 0

if type_of_drink == "Espresso":
    if amount_of_drinks >= 5:
        if sugar_amount == "Without":
            final_sum = amount_of_drinks * 0.90 * 0.65 * 0.75
        elif sugar_amount == "Normal":
            final_sum = amount_of_drinks * 1.00 * 0.75
        elif sugar_amount == "Extra":
            final_sum = amount_of_drinks * 1.20 * 0.75
    else:
        if sugar_amount == "Without":
            final_sum = amount_of_drinks * 0.90 * 0.65
        elif sugar_amount == "Normal":
            final_sum = amount_of_drinks * 1.00
        elif sugar_amount == "Extra":
            final_sum = amount_of_drinks * 1.20

elif type_of_drink == "Cappuccino":
    if sugar_amount == "Without":
        final_sum = amount_of_drinks * 0.65
    elif sugar_amount == "Normal":
        final_sum = amount_of_drinks * 1.20
    elif sugar_amount == "Extra":
        final_sum = amount_of_drinks * 1.60

elif type_of_drink == "Tea":
    if sugar_amount == "Without":
        final_sum = amount_of_drinks * 0.50 * 0.65
    elif sugar_amount == "Normal":
        final_sum = amount_of_drinks * 0.6
    elif sugar_amount == "Extra":
        final_sum = amount_of_drinks * 0.7

if final_sum > 15:
    final_sum *= 0.80

print(f"You bought {amount_of_drinks} cups of {type_of_drink} for {final_sum:.2f} lv.")
