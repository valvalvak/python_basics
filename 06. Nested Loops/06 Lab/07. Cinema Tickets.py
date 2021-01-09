student_ticket = 0
standard_ticket = 0
kid_ticket = 0
movie = ""
all_tickets = 0
command = input()
while command != "Finish":
    current_movie = command
    current_tickets = 0
    free_seats = int(input())
    sold_tickets_type = input()
    while sold_tickets_type != "End":
        if sold_tickets_type == "student":
            student_ticket += 1
        elif sold_tickets_type == "standard":
            standard_ticket += 1
        elif sold_tickets_type == "kid":
            kid_ticket += 1
        current_tickets += 1
        if current_tickets >= free_seats:
            break
        sold_tickets_type = input()
    all_tickets += current_tickets
    print(f"{current_movie} - {current_tickets/free_seats*100:.2f}% full.")
    command = input()
print(f"Total tickets: {all_tickets}\n"
      f"{student_ticket/all_tickets*100:.2f}% student tickets.\n"
      f"{standard_ticket/all_tickets*100:.2f}% standard tickets.\n"
      f"{kid_ticket/all_tickets*100:.2f}% kids tickets.")