#Kirjan lainaus
def borrow_book(isbn):
    for book in library:
        if book["isbn"] == isbn:
            if book["copies"] > 0:
                book["copies"] -= 1
                print(f"Borrowed '{book['title']}'.")
            else:
                print("Sorry, no copies available.")
            return
    print("Book not found.")

#Kirjan palautus
def return_book(isbn):
    for book in library:
        if book["isbn"] == isbn:
            book["copies"] += 1
            print(f"Returned '{book['title']}'.")
            return
    print("Book not found.")
