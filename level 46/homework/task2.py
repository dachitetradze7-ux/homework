library = {}
def add_book(library, isbn, book_info):
    
    library[isbn] = book_info
def search_by_author(library, author):
    found_books = []
    for isbn, info in library.items():
        if info["author"].lower() == author.lower():
            found_books.append((isbn, info))
    return found_books 

def get_available_books(library):
    available_books = []
    for isbn, info in library.items():
        if info["available"]:
            available_books.append((isbn, info))
    return available_books

def oldest_book(library):
    if not library:
        return None
    
    isbns = list(library.keys())
    oldest_isbn = isbns[0]

    for isbn in isbns:
        if library[isbn]["year"] < library[oldest_isbn]["year"]:
            oldest_isbn = isbn
    return oldest_isbn, library[oldest_isbn]
add_book(
    library,
    "978-1",
    {
        "title": "green mile",
        "author": "stiven king",
        "year": 1980,
        "available": True,
    },
)

add_book(
    library,
    "978-2",
    {
        "title": "vefxistyaosani",
        "author": "shota-rustaveli",
        "year": 1950,
        "available": False
    }
)

print( "\n stiven king's books" )
print(search_by_author(library, "stiven king"))

print(" available books ")
print(get_available_books(library))

print(" old books ")
print(oldest_book(library))

