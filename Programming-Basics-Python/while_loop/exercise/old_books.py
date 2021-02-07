favourite_book = input()

book_name = input()
is_book_found = False
books_counter = 0
while True:
    books_counter += 1
    if book_name == favourite_book:
        books_counter -= 1
        is_book_found = True
        break
    if book_name == 'No More Books':
        books_counter -= 1
        break

    book_name = input()

if is_book_found:
    print(f"You checked {books_counter} books and found it.")
else:
    print("The book you search is not here!", end='\n'
          f"You checked {books_counter} books.")
