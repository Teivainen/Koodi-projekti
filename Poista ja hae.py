
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
    print("3. Add a books")
    print("4. Borrow book")
    print("5. Return book")
    print("6. Exit")

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
    elif choice == "4":
        print("Goodbye!")
        break
    else:
        print("Invalid choice")
        