
library = [
    {
        "isbn": "978-951-1-49901-5",
        "title": "Opettaja",
        "author": "Freida McFadden",
        "genre": "Psychological thriller",
        "copies": "3"
    },
    {
        "isbn": "978-951-1-48900-9",
        "title": "Työkaveri",
        "author": "Freida McFadden",
        "genre": "Psychological thriller",
        "copies": "1"
    }
]


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


while True:
    print("\nLibrary system")
    print("1. Show all books")
    print("2. Remove a book")
    print("3. Exit")

    choice = input("Choose an option: ")

    if choice == "1":
        show_all_books()
    elif choice == "2":
        remove_book()
    elif choice == "3":
        print("Goodbye!")
        break
    else:
        print("Invalid choice")
        