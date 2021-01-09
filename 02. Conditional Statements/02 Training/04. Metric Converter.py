factor = float(input())
metric_in = input()
metric_out = input()
if metric_in == "mm":
    if metric_out == "cm":
        print(f"{(factor / 10):.3f}")
    elif metric_out == "m":
        print(f"{(factor / 1000):.3f}")
elif metric_in == "cm":
    if metric_out == "mm":
        print(f"{(factor * 10):.3f}")
    elif metric_out == "m":
        print(f"{(factor / 100):.3f}")
elif metric_in == "m":
    if metric_out == "mm":
        print(f"{(factor * 1000):.3f}")
    elif metric_out == "cm":
        print(f"{(factor * 100):.3f}")
