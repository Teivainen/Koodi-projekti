#lista kirjoista, "kirjan nimi, kirjailija"
library = []

#hakukenttä
def search_books(library):
    search = input("Search a book by its name or author: ").lower()
found = False

for title, author in library: #hakee joko kirjan tai kirjailijan nimellä
    if search_books in title.lower() or search_books in author.lower():
        print("Found:", title, "-", author)
        found = True

if not found:
    print("No results.")

search_books(library)
