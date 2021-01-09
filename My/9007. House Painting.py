height = float(input())
width = float(input())
roof_height = float(input())
red = 4.3
green = 3.4
front_door = 1.2 * 2
side_windows = 1.5 * 1.5 * 2
front_n_rear = height * height * 2 - front_door # green
sides = height * width * 2 - side_windows # green
roof_sides = sides + side_windows # red
roof_triangle = height * roof_height / 2 # red
red_paint = ( roof_sides + roof_triangle * 2) / red
green_paint = (front_n_rear + sides ) / green
print(f"{green_paint:.2f}")
print(f"{red_paint:.2f}")