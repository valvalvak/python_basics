deposit_sum = float(input())
deposit_time = int(input())
apr = float(input())
summarize = deposit_sum + deposit_time * ((deposit_sum * apr / 100) / 12)
print(f"{summarize}")
