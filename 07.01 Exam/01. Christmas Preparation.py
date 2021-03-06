paper_rolls_count = int(input())
fabric_rolls_count = int(input())
glue_l = int(input())
discount = int(input())

wrap_paper = paper_rolls_count * 5.80
wrap_fabric = fabric_rolls_count * 7.20
glue = 1.20

discount_multiply = ((wrap_paper + wrap_fabric + glue) * discount) / 100

result = wrap_fabric + wrap_paper + glue - discount_multiply

print(f"{result}:.3f")
