jury = int(input())
command = str(input())
all_grades = 0
counter = 0
while command != "Finish":
    presentation = command
    average_grade = 0
    for grades in range(jury):
        current_grade = float(input())
        counter += 1
        average_grade += current_grade
        all_grades += current_grade
    average_grade /= jury
    print(f"{presentation} - {average_grade:.2f}.")
    command = input()
all_grades /= counter
print(f"Student's final assessment is {all_grades:.2f}.")