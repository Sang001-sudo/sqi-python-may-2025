library = []

def add_book():
    title = input("Enter the title of the book: ").strip()
    author = input("Enter the name of the author of the book: ").strip()
    year_of_publication = int(input("Enter the year of publication of the book: "))
    isbn = input("Enter the Book ISBN: ").strip()
    library.append({
        "title": title,
        "author": author,
        "year_of_publication": year_of_publication,
        "isbn": isbn,
        "available": True
    })
    return f"Book '{title}' by {author} added successfully."


def view_books():
    if not library:
        print("No books in the library.")
        return
    for index, book in enumerate(library, start=1):
        print(f"{index}. {book['title']} by {book['author']}, "
              f"published in {book['year_of_publication']}, "
              f"ISBN: {book['isbn']}, "
              f"Available: {'Yes' if book['available'] else 'No'}")


def update_book():
    title = input("Enter the Title of the book to update: ").strip()
    for book in library:
        if book["title"] == title:
            print("Leave blank to keep current value.")
            new_title = input(f"New title (current: {book['title']}): ").strip()
            new_author = input(f"New author (current: {book['author']}): ").strip()
            new_year = input(f"New publication year (current: {book['year_of_publication']}): ").strip()
            new_isbn = input(f"New isbn (current: {book['isbn']}): ").strip()

            if new_title:
                book["title"] = new_title
            if new_author:
                book["author"] = new_author
            if new_year.isdigit():
                book["year_of_publication"] = int(new_year)
            if new_isbn:
                book["isbn"] = new_isbn

            print("Book updated successfully.")
            return
    print("Book not found.")


def delete_book():
    title = input("Enter the Title of the book to delete: ").strip()
    for book in library:
        if book["title"] == title:
            library.remove(book)
            print(f"Book with Title: {title} deleted successfully.")
            return
    print("Book not found.")


def search_book():
    keyword = input("Enter title or author to search: ").strip().lower()
    found = False
    for book in library:
        if keyword in book["title"].lower() or keyword in book["author"].lower():
            print(f"{book['title']} by {book['author']}, "
                  f"published in {book['year_of_publication']}, "
                  f"ISBN: {book['isbn']}, Available: {'Yes' if book['available'] else 'No'}")
            found = True
    if not found:
        print("No matching books found.")


def borrow_book():
    title = input("Enter the Title of the book to borrow: ").strip()
    for book in library:
        if book["title"] == title:
            if book["available"]:
                book["available"] = False
                print(f"You have successfully borrowed '{book['title']}'.")
            else:
                print("Sorry, this book is already borrowed.")
            return
    print("Book not found.")


def return_book():
    title = input("Enter the Title of the book to return: ").strip()
    for book in library:
        if book["title"] == title:
            if not book["available"]:
                book["available"] = True
                print(f"You have successfully returned '{book['title']}'.")
            else:
                print("This book wasn't borrowed.")
            return
    print("Book not found.")


menu = """
1. Add Book
2. View Books
3. Update Book
4. Delete Book
5. Search Book
6. Borrow Book
7. Return Book
8. Exit
"""

print("Welcome to our Library")

while True:
    print(menu)
    choice = input("Choose an option from the menu above: ").strip()

    if choice == "1":
        print(add_book())
    elif choice == "2":
        view_books()
    elif choice == "3":
        update_book()
    elif choice == "4":
        delete_book()
    elif choice == "5":
        search_book()
    elif choice == "6":
        borrow_book()
    elif choice == "7":
        return_book()
    elif choice == "8":
        print("Bye")
        break
    else:
        print("Invalid choice. Please choose from 1 to 8.")