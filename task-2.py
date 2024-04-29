def add_book(library, title, author):
    new_book = (title, author)
    if new_book in library:
        print("This book is already in the library.")
    else:
        library.append(new_book)
        print(f"'{title}' by {author} has been added to the library.")


library = [("1984", "George Orwell"), ("Brave New World", "Aldous Huxley")]
add_book(library, "To Kill a Mockingbird", "Harper Lee")
add_book(library, "1984", "George Orwell")
print(library)
