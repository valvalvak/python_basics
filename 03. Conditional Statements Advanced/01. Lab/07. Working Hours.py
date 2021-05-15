time = int(input())
day = input()
# като работното време на офисът е от 10-18 часа, от понеделник до събота включително
if (10 <= time <= 18) and (day == "Monday" or day == "Tuesday" or day == "Wednesday" or day == "Thursday"
                           or day == "Friday" or day == "Saturday"):
    print("open")
else:
    print("closed")
