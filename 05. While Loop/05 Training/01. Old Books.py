book_counter = 0
favorite_book = False
desired_book = input()
book_pick = input()
while book_pick != "No More Books":
    if book_pick == desired_book:
        favorite_book = True
        break
    book_counter += 1
    book_pick = input()
if favorite_book is True:
    print(f"You checked {book_counter} books and found it.")
else:
    print(f"The book you search is not here!\nYou checked {book_counter} books.")
