def borrow_book(isbn):
    for book in library:
        if book["isbn"] == isbn:
            if book["copies"] > 0:
                book["copies"] -= 1
                print(f"You borrowed '{book['title']}'.")
            else:
                print("Sorry, no copies available.")
            return
    print("Book not found.")

def return_book(isbn):
    for book in library:
        if book["isbn"] == isbn:
            book["copies"] += 1
            print(f"You returned '{book['title']}'.")
            return
    print("Book not found.")