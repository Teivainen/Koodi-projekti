libary = []

def add_books(isbn, title, author, genre, copies):
    book = {
        "ISBN": isbn,
        "Title": title,
        "Author": author,
        "Genre": genre,
        "Copies": copies
    }
    libary.append(book)

add_books("978-951-1", "Kotiapulainen valvoo", "Freida McFadden", "Psychological thriller", 12)
print(libary)

