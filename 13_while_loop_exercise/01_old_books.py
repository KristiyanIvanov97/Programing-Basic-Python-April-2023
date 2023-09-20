correct_book = input()
current_book = input()
book_count = 0

while current_book != correct_book:
    if current_book == "No More Books":
        print(f"The book you search is not here!\nYou checked {book_count} books.")
        break
    book_count += 1
    current_book = input()

if current_book == correct_book:
    print(f"You checked {book_count} books and found it.")
