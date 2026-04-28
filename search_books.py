#lista kirjoista, "kirjan nimi, kirjailija"
library = []

#hakukenttä
search = input("Hae kirja nimellä tai kirjailijan nimellä: ").lower()
found = False

for title, author in library: #hakee joko kirjan tai kirjailijan nimellä
    if search in title.lower() or search in author.lower():
        print("Löytyi:", title, "-", author)
        found = True

if not found:
    print("Ei osumia hakusanalla.")
