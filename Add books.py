libary = []

def add_books(isbn, title, author, genre, copies):
    book = {
        "isbn": isbn,
        "title": title,
        "author": author,
        "genre": genre,
        "copies": copies
    }
    libary.append(book)
