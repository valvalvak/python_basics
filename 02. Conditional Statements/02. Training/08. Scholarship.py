# current_income = float(input())
# current_grade = float(input())
# salary = float(input())
# social_scholarship = int (salary * 0.35)
# excellent_scholarship= int (current_grade * 25)
# if current_grade >= 5.5:
#     if excellent_scholarship> social_scholarship:
#         print(f"You get a scholarship for excellent results {excellent_scholarship} BGN")
#     elif current_income < salary and social_scholarship > excellent_scholarship:
#         print(f"You get a Social scholarship {social_scholarship} BGN")
#     elif current_income < salary and social_scholarship == excellent_scholarship:
#         print(f"You get a scholarship for excellent results {excellent_scholarship} BGN")
# elif current_grade > 4.5 and current_income < salary:
#     print(f"You get a Social scholarship {social_scholarship} BGN")
# else:
#     print("You cannot get a scholarship!")
current_income = float(input())
current_grade = float(input())
social_salary = float(input())
social_scholarship = int(social_salary * 0.35)
excellent_scholarship = int(current_grade * 25)
if current_grade >= 5.5:
    if current_income < social_salary:
        if excellent_scholarship >= social_scholarship:
            print(f"You get a scholarship for excellent results {excellent_scholarship} BGN")
        elif social_scholarship > excellent_scholarship:
            print(f"You get a Social scholarship {social_scholarship} BGN")
    else:
        print(f"You get a scholarship for excellent results {excellent_scholarship} BGN")
elif current_grade > 4.5:
    if current_income < social_salary:
        print(f"You get a Social scholarship {social_scholarship} BGN")
    else:
        print("You cannot get a scholarship!")
else:
    print("You cannot get a scholarship!")
