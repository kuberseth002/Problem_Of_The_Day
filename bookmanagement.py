library = []

def add_book(title, author, genre):
    """
    Add a new book to the library.

    Parameters:
    title (str): The title of the book.
    author (str): The author of the book.
    genre (str): The genre of the book.
    """
    library.append({
        "title": title,
        "author": author,
        "genre": genre,
        "available": True
    })

def search_books(keyword, field):
    """
    Search for books by a specific field like title, author, or genre.

    Parameters:
    keyword (str): The search keyword.
    field (str): The field to search in ('title', 'author', or 'genre').

    Returns:
    list: A list of matching book dictionaries.
    """
    keyword = keyword.lower()
    return [
        book for book in library
        if keyword in book.get(field, "").lower()
    ]

def borrow_book(title):
    """
    Borrow a book by its title. Marks it as unavailable.

    Parameters:
    title (str): The title of the book to borrow.

    Raises:
    Prints an error if the book is not found or already borrowed.
    """
    for book in library:
        if book["title"].lower() == title.lower():
            if not book["available"]:
                print(f"Error: '{book['title']}' is already borrowed.")
                return
            book["available"] = False
            print(f"You borrowed '{book['title']}'.")
            return
    print(f"Error: Book titled '{title}' not found.")

def return_book(title):
    """
    Return a borrowed book by its title. Marks it as available.

    Parameters:
    title (str): The title of the book to return.

    Raises:
    Prints an error if the book is not found or already available.
    """
    for book in library:
        if book["title"].lower() == title.lower():
            if book["available"]:
                print(f"Error: '{book['title']}' is already available.")
                return
            book["available"] = True
            print(f"You returned '{book['title']}'.")
            return
    print(f"Error: Book titled '{title}' not found.")

def print_book(book):
    """
    Print the details of a book in a readable format.

    Parameters:
    book (dict): The book dictionary to print.
    """
    status = "Available" if book["available"] else "Borrowed"
    print(f"'{book['title']}' by {book['author']} ({book['genre']}) - {status}")

if __name__ == "__main__":
    # calling  all function
    
    add_book("Atomic Habits", "James Clear", "Self-Improvement")
    add_book("Think and Grow Rich", "Napoleon Hill", "Motivation")
    add_book("Deep Work", "Cal Newport", "Productivity")
    add_book("Can't Hurt Me", "David Goggins", "Memoir")

    print("\n Search by author 'Goggins':")
    results = search_books("Goggins", "author")
    for book in results:
        print_book(book)

    print("\n Borrowing 'Can't Hurt Me':")
    borrow_book("Can't Hurt Me")
    borrow_book("Can't Hurt Me")  

    print("\n Returning 'Can't Hurt Me':")
    return_book("Can't Hurt Me")
    return_book("Can't Hurt Me")  
    
    print("\n📘 Borrowing 'Invisible Man':")
    borrow_book("Invisible Man")
