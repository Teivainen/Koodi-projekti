
library = [
    {
        "isbn": "978-951-1-49901-5",
        "title": "Opettaja",
        "author": "Freida McFadden",
        "genre": "Psychological thriller",
        "copies": 3
    },
    {
        "isbn": "978-951-1-48900-9",
        "title": "Työkaveri",
        "author": "Freida McFadden",
        "genre": "Psychological thriller",
        "copies": 1
    }
]
def add_books():
    isbn = input("Please enter ISBN: ")
    title = input("Please enter title: ")
    author = input("Please enter author: ")
    genre = input("Please enter genre: ")
    copies = int(input("Please enter the number of available copies: "))

    library.append({
        "isbn": isbn,
        "title": title,
        "author": author,
        "genre": genre,
        "copies": copies

})
    print("Book added successfully!")

    for book in library:
        print(
        f"{book["title"]} by {book["author"]}, {book["isbn"]}", 
        f"{book["genre"]}, available copies: {book["copies"]}"
    )


def show_all_books():
    if not library:
        print("No books in the library.")
        return

    print("\nAll books:")
    for book in library:
        print("--------------------")
        print("ISBN:", book["isbn"])
        print("Title:", book["title"])
        print("Author:", book["author"])
        print("Genre:", book["genre"])
        print("Copies:", book["copies"])

def remove_book():
    isbn = input("Enter ISBN of the book you want to remove: ")

    for book in library:
        if book["isbn"] == isbn:
            library.remove(book)
            print("Book removed successfully!")
            return

    print("Book not found.")

def search_books():
    search = input("Search a book by its name or author: ").lower()
    found = False
    
    for book in library:
        if search in book["title"].lower() or search in book ["author"].lower():
            print("Found:", book["title"], "-", book ["author"])
            found = True
    
    if not found:
        print("No results.")

def borrow_book():
    isbn = input("Enter ISBN of the book you want to borrow:")

    for book in library:
        if book["isbn"] == isbn:
            if book["copies"] > 0:
                book["copies"] -= 1
                print(f"Borrowed '{book['title']}'.")
            else:
                print("Sorry, no copies available.")
            return
        
    print("Book not found.")

def return_book():
    isbn = input("Enter the ISBN of the book you want to borrow")
    for book in library:
        if book["isbn"] == isbn:
            book["copies"] += 1
            print(f"Returned '{book['title']}'.")
            return
    print("Book not found.")




while True:
    print("\nLibrary system")
    print("1. Show all books")
    print("2. Remove a book")
    print("3. Add a books")
    print("4. Borrow book")
    print("5. Return book")
    print("6. Search books")
    print("7. Exit")

    choice = input("Choose an option: ")

    if choice == "1":
        show_all_books()
    elif choice == "2":
        remove_book()
    elif choice == "3":
        add_books()
    elif choice == "4":
        borrow_book()
    elif choice == "5":
        return_book()
    elif choice == "6":
        search_books()
    elif choice == "7":
        print("Goodbye!")
        break
    else:
        print("Invalid choice")

