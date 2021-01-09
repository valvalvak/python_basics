name = input()
annual_grade = float(input())
fails_counter = 0
grade_sum = 0
average_grade = 0
grade_class = 0
while grade_class <= 12:
    grade_class += 1
    grade_sum += annual_grade
    average_grade = grade_sum / grade_class
    if annual_grade < 4:
        fails_counter += 1
        if fails_counter != 2:
            grade_class -= 1
    if fails_counter == 2:
        print(f"{name} has been excluded at {int(grade_class)} grade")
        break
    if grade_class == 12 and average_grade >= 4:
        print(f"{name} graduated. Average grade: {average_grade:.2f}")
        break
    annual_grade = float(input())
