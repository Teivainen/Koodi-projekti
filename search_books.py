#lista kirjoista, "kirjan nimi, kirjailija"
library = []

#hakukenttä
def search_books(library):
    search = input("Search a book by its name or author: ").lower()
found = False

for title, author in library: #hakee joko kirjan tai kirjailijan nimellä
    if search in title.lower() or search in author.lower():
        print("Found:", title, "-", author)
        found = True

if not found:
    print("No results.")
