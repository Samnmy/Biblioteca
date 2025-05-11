# library_management.py

import sys  # Module used to access system-specific parameters and functions
from typing import List, Dict  # Used to define list and dictionary type annotations for better clarity and validation

# Sample initial data: List of preloaded book entries with keys: title, author, year, quantity, and price
library: List[Dict] = [
    {"title": "Cien anos de soledad", "author": "Gabriel Garcia Marquez", "year": 1967, "quantity": 3, "price": 25.50},
    {"title": "1984", "author": "George Orwell", "year": 1949, "quantity": 5, "price": 15.75},
    {"title": "El principito", "author": "Antoine de Saint-Exupery", "year": 1943, "quantity": 4, "price": 12.00}
]

# --- Core Functions ---

# Function to register a new book into the library system
def register_book(title: str, author: str, year: int, quantity: int, price: float):
    # Check if the year is within valid range and quantity/price are non-negative
    if year < 1800 or year > 2024 or quantity < 0 or price < 0:
        print("Invalid input. Year must be between 1800 and 2024. Quantity and price must be positive.")
        return
    # Loop through books in the library to check if book already exists
    for book in library:
        if book['title'].lower() == title.lower():  # Case-insensitive comparison
            print("Book already exists.")
            return
    # If book doesn't exist, append new book to the library list
    library.append({"title": title, "author": author, "year": year, "quantity": quantity, "price": price})
    print("Book registered successfully.")

# Function to find and return a book by its title
def search_book_by_title(title: str):
    for book in library:  # Loop through books
        if book['title'].lower() == title.lower():  # Match title ignoring case
            return book  # Return matching book
    return None  # Return None if no match found

# Function to update a book's quantity and/or price
def update_book(title: str, quantity: int = None, price: float = None):
    for book in library:  # Loop through library to find the book
        if book['title'].lower() == title.lower():
            # If quantity is provided and valid, update it
            if quantity is not None and quantity >= 0:
                book['quantity'] = quantity
            # If price is provided and valid, update it
            if price is not None and price >= 0:
                book['price'] = price
            print("Book updated successfully.")
            return
    print("Book not found.")  # Notify if book was not found

# Function to remove a book from the library by title
def delete_book(title: str):
    global library  # Use global keyword to modify global library variable
    # Use list comprehension to remove book with matching title
    library = [book for book in library if book['title'].lower() != title.lower()]
    print("Book deleted if it existed.")

# Function to generate statistical report of the library
def generate_reports():
    # Calculate the total inventory value using quantity * price for all books
    total_value = sum(book['quantity'] * book['price'] for book in library)
    # Sort the books by publication year in ascending order
    sorted_books = sorted(library, key=lambda x: x['year'])
    if sorted_books:  # If there are books in the library
        # Display the oldest book
        print(f"Oldest book: {sorted_books[0]['title']}, Year: {sorted_books[0]['year']}")
        # Display the most recent book
        print(f"Most recent book: {sorted_books[-1]['title']}, Year: {sorted_books[-1]['year']}")
    # Print the total inventory value formatted to 2 decimal places
    print(f"Total inventory value: ${total_value:.2f}")

# --- Optional Interactive Menu ---

# Function to display a command-line menu interface
def menu():
    while True:  # Infinite loop until user chooses to exit
        # Display menu options
        print("\nLibrary Management System")
        print("1. Register new book")
        print("2. Search book")
        print("3. Update book")
        print("4. Delete book")
        print("5. Generate report")
        print("6. Exit")

        # Ask the user to select an option
        choice = input("Choose an option: ")

        # Handle book registration
        if choice == "1":
            t = input("Title: ")  # Ask for book title
            a = input("Author: ")  # Ask for author
            y = int(input("Year: "))  # Ask for year and convert to int
            q = int(input("Quantity: "))  # Ask for quantity and convert to int
            p = float(input("Price: "))  # Ask for price and convert to float
            register_book(t, a, y, q, p)  # Call the register_book function
        # Handle book search
        elif choice == "2":
            t = input("Title to search: ")
            book = search_book_by_title(t)  # Search for book
            print(book if book else "Book not found. Would you like to register it?")  # Display result
        # Handle book update
        elif choice == "3":
            t = input("Title to update: ")
            q = int(input("New quantity (-1 to skip): "))
            p = float(input("New price (-1 to skip): "))
            update_book(t, q if q >= 0 else None, p if p >= 0 else None)  # Use None if input is -1
        # Handle book deletion
        elif choice == "4":
            t = input("Title to delete: ")
            delete_book(t)
        # Handle report generation
        elif choice == "5":
            generate_reports()
        # Handle program exit
        elif choice == "6":
            print("Goodbye!")
            break  # Exit loop
        else:
            print("Invalid choice.")  # Handle invalid input

# Entry point of the script: run menu if script is executed directly
if __name__ == "__main__":
    menu()
