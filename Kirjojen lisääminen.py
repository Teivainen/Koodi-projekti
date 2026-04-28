libary = [
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

isbn = input("Please enter ISBN: ")
title = input("Please enter title: ")
author = input("Please enter author: ")
genre = input("Please enter genre: ")
copies = int(input("Please enter the number of available copies: "))

libary.append({
    "isbn": isbn,
    "title": title,
    "author": author,
    "genre": genre,
    "copies": copies

})

print("Book added successfully!")

for book in libary:
    print(
        f"{book["title"]} by {book["author"]}, {book["isbn"]}" 
        f"{book["genre"]}, available copies: {book["copies"]}"
    )