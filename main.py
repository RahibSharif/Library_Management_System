import json
from pathlib import Path
from datetime import datetime, timedelta

BASE_DIR = Path(__file__).parent
book_path = BASE_DIR / "books.json"

class Book:
    def __init__(self, title, author, available=True):
        self.title = title
        self.author = author
        self.available = available
        self.borrowed_date = None
        self.due_date = None

    def to_dict(self):
        return {
        "Title": self.title,
        "Author": self.author,
        "Available": self.available,
        "Borrowed Date": self.borrowed_date,
        "Due Date": self.due_date
        }

library = []

def add_book():
    title = input("Enter title: ")
    author = input("Enter author's name: ")

    for item in library:
        if item.title.lower() == title.lower():
            print("Book already exists!")
            return
        else:
             book = Book(title, author, available=True)
             library.append(book)
             print("Book added!")

def view_book():
    for item in library:
        print()
        print(f"Title: {item.title}")
        print(f"Author: {item.author}")
        print(f"Available: {item.available}")
        print(f"Borrowed Date: {item.borrowed_date}")
        print(f"Due Date: {item.due_date}")

def load_books():
    if book_path.exists():
        with open(book_path, "r") as f:
            books = json.load(f)
        
        for item in books:
            book = Book(
                item["Title"],
                item["Author"],
                item["Available"]
            )

            book.borrowed_date = item.get("Borrowed Date")
            book.due_date = item.get("Due Date")

            library.append(book)

load_books()

def borrow_book():
    title = input("Enter title: ")

    for item in library:
        if item.title.lower() == title.lower():
            if item.available == True:
                item.available = False
                today = datetime.now()
                item.borrowed_date = today.strftime("%Y-%m-%d")
                item.due_date = (today + timedelta(days=14)).strftime("%Y-%m-%d")
                print("Book borrowed!")

def return_book():
    title = input("Enter title: ")

    for item in library:
        if item.title.lower() == title.lower():
            if item.available == False:
                item.available = True
                item.borrowed_time = None
                item.due_date = None
                print("Book returned!")

def search_book():
    title = input("Enter title: ")

    for item in library:
        if item.title.lower() == title.lower():
            print()
            print(f"Title: {item.title}")
            print(f"Author: {item.author}")
            print(f"Available: {item.available}")
            return
    print("Book not found!")

def delete_book():
    title = input("Enter title: ")

    for item in library:
        if item.title.lower() == title.lower():
            print()
            library.remove(item)
            print("Book removed!")
            return
    print("Book not found!")

def count_book():
    total_books = len(library)

    available_count = 0
    borrowed_count = 0

    for item in library:
        if item.available:
            available_count += 1
        else:
            borrowed_count += 1

    print()
    print(f"Total books: {total_books}")
    print(f"Available books: {available_count}")
    print(f"Borrowed books: {borrowed_count}")

def view_borrowed_books():
    for item in library:
        if item.available == False:
            print()
            print(f"Title: {item.title}")
            print(f"Author: {item.author}")
            print(f"Borrowed Date: {item.borrowed_date}")
            print(f"Due Date: {item.due_date}")

def view_available_books():
    for item in library:
        if item.available == True:
            print()
            print(f"Title: {item.title}")
            print(f"Author: {item.author}")
            print(f"Borrowed Date: {item.borrowed_date}")
            print(f"Due Date: {item.due_date}")

def view_overdue_books():
    for item in library:
        print(item.title, item.available, item.due_date)
        if item.available == False:
            today = datetime.now().strftime("%Y-%m-%d")

            if item.due_date is not None:
                if today > item.due_date:
                    print("Overdue!")
                else:
                    print("Not Overdue!")
        else:
            print("No due date saved for this borrowed book.")

def sort_books():
    sorted_books = sorted(library, key= lambda item: item.title.lower())
    
    for i, item in enumerate(sorted_books, start=1):
        print(f"\n{i}.")
        print(f"Title: {item.title}")
        print(f"Author: {item.author}")
        print(f"Available: {item.available}")

def sort_authors():
    sorted_authors = sorted(library, key= lambda item: item.author.lower())

    for i, item in enumerate(sorted_authors, start=1):
        print(f"\n{i}.")
        print(f"Title: {item.title}")
        print(f"Author: {item.author}")
        print(f"Available: {item.available}")



menu = """
1. Add book.
2. View book.
3. Quit.
4. Borrow book.
5. Return book.
6. Search book.
7. Delete book.
8. Count book.
9. View borrowed books.
10. View available books.
11. View overdue books.
12. Sort the books by title.
13. Sort the books by author.
"""

while True:
    print(menu)
    choice = input("Enter choice number: ")

    if choice == "1":
        add_book()

        with open(book_path, "w") as f:
            json.dump([item.to_dict() for item in library], f)

    elif choice == "2":
        with open(book_path, "r") as f:
            item = json.load(f)
        view_book()

    elif choice == "3":
        print("Goodbye!")
        break

    elif choice == "4":
        borrow_book()

        with open(book_path, "w") as f:
            json.dump([item.to_dict() for item in library], f)

    elif choice == "5":
        return_book()

        with open(book_path, "w") as f:
            json.dump([item.to_dict() for item in library], f)

    elif choice == "6":
        search_book()

    elif choice == "7":
        delete_book()

        with open(book_path, "w") as f:
            json.dump([item.to_dict() for item in library], f)

    elif choice == "8":
        count_book()

    elif choice == "9":
        view_borrowed_books()

    elif choice == "10":
        view_available_books()

    elif choice == "11":
        view_overdue_books()

    elif choice == "12":
        sort_books()

    elif choice == "13":
        sort_authors()

    else:
        print("Invalid options!")

