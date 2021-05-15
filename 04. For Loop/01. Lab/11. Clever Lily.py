years = int(input())
laundry_machine = float(input())
doll_price = int(input())

money_gift = 0
money_sum = 0
dolls_gift = 0

for birthdays in range(1, years + 1):
    if birthdays % 2 == 0:
        money_gift += 10
        money_sum += money_gift - 1
    else:
        dolls_gift += 1

dolls_sum = dolls_gift * doll_price
total_sum = dolls_sum + money_sum
diff_sum = abs(total_sum - laundry_machine)

if total_sum >= laundry_machine:
    print(f"Yes! {diff_sum:.2f}")
else:
    print(f"No! {diff_sum:.2f}")
