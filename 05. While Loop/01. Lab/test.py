name = input()
counter_years = 0
failed_times = 0
sum_all_grades = 0

while counter_years < 13:
    yearly_grade = float(input())
    if yearly_grade >= 4:
        sum_all_grades += yearly_grade
        counter_years += 1
        if counter_years == 12:
            average_grade = sum_all_grades / counter_years
            print(f"{name} graduated. Average grade: {average_grade:.2f}")
    if yearly_grade < 4:
        failed_times += 1
        if failed_times == 2:
            break
        print(f"{name} has been excluded at {counter_years + 1} grade")
