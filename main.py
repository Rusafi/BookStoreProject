import json
import os

# File to store book data
BOOKS_FILE = "books.json"

# Load existing book data from file
def load_books():
    if os.path.exists(BOOKS_FILE):
        with open(BOOKS_FILE, "r") as f:
            return json.load(f)
    return []

# Save books to file
def save_books(books):
    with open(BOOKS_FILE, "w") as f:
        json.dump(books, f, indent=4)

# Add a new book
def add_book():
    books = load_books()
    isbn = input("Enter ISBN: ")
    if any(book['ISBN'] == isbn for book in books):
        print("Book with this ISBN already exists!")
        return
    
    title = input("Enter Title: ")
    author = input("Enter Author: ")
    genre = input("Enter Genre: ")
    price = float(input("Enter Price: "))
    quantity = int(input("Enter Quantity: "))
    
    books.append({
        "ISBN": isbn,
        "Title": title,
        "Author": author,
        "Genre": genre,
        "Price": price,
        "Quantity": quantity
    })
    
    save_books(books)
    print("Book added successfully!")

# View all books
def view_books():
    books = load_books()
    if not books:
        print("No books available.")
        return
    
    for book in books:
        print(f"ISBN: {book['ISBN']}, Title: {book['Title']}, Author: {book['Author']}, Genre: {book['Genre']}, Price: {book['Price']}, Quantity: {book['Quantity']}")

# Remove a book
def remove_book():
    books = load_books()
    isbn = input("Enter ISBN of the book to remove: ")
    books = [book for book in books if book['ISBN'] != isbn]
    save_books(books)
    print("Book removed successfully!")

# Main menu
def main():
    while True:
        print("\nBook Store Management System")
        print("1. Add Book")
        print("2. View Books")
        print("3. Remove Book")
        print("4. Exit")
        choice = input("Enter your choice: ")
        
        if choice == "1":
            add_book()
        elif choice == "2":
            view_books()
        elif choice == "3":
            remove_book()
        elif choice == "4":
            print("Exiting...")
            break
        else:
            print("Invalid choice, please try again.")

if __name__ == "__main__":
    main()
