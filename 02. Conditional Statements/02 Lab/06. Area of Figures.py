import math

input_type = input()
if input_type == "square":
    input_a = float(input())
    print(f'{(input_a * input_a):.3f}')
elif input_type == "rectangle":
    input_a = float(input())
    input_b = float(input())
    print(f'{input_a * input_b:.3f}')
elif input_type == "circle":
    input_a = float(input())
    print(f'{math.pi*(input_a*input_a):.3f}')
elif input_type == "triangle":
    input_a = float(input())
    input_b = float(input())
    print(f'{input_a * input_b/2:.3f}')