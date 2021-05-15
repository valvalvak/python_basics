max_bad_grades = int(input())
total_score = 0
number_of_problems = 0
last_problem = ""
bad_grades_count = 0
fail = False
quest = input()
while quest != "Enough":
    last_problem = quest
    current_grade = int(input())
    if current_grade <= 4:
        bad_grades_count += 1
        if bad_grades_count == max_bad_grades:
            fail = True
            break
    number_of_problems += 1
    total_score += current_grade
    quest = input()
average_score = total_score / number_of_problems
if fail:
    print(f"You need a break, {max_bad_grades} poor grades.")
else:
    print(f"Average score: {average_score:.2f}\n"
          f"Number of problems: {number_of_problems}\n"
          f"Last problem: {last_problem}")
