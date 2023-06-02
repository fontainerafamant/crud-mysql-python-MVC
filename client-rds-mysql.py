import requests


# Base URL of the backend Flask application
BASE_URL = 'http://localhost:5000'


# Function to display the main menu
def display_menu():
    print("***** Bookstore Management *****")
    print("1. Get all books")
    print("2. Add a book")
    print("3. Update a book")
    print("4. Delete a book")
    print("5. Exit")
    print("*******************************")


# Function to get all books
def get_books():
    response = requests.get(f'{BASE_URL}/books')
    if response.status_code == 200:
        books = response.json()
        for book in books:
            print(f"ID: {book['id']}, Author: {book['author']}, Title: {book['title']}, ISBN: {book['isbn']}")
    else:
        print('Failed to retrieve books.')


# Function to add a new book
def add_book():
    print("***** Add a Book *****")
    author = input("Enter the author: ")
    title = input("Enter the title: ")
    isbn = input("Enter the ISBN: ")
    book_data = {
        'author': author,
        'title': title,
        'isbn': isbn
    }
    response = requests.post(f'{BASE_URL}/books', json=book_data)
    if response.status_code == 201:
        print('Book added successfully.')
    else:
        print('Failed to add book.')


# Function to update an existing book
def update_book():
    print("***** Update a Book *****")
    book_id = input("Enter the ID of the book to update: ")
    author = input("Enter the new author: ")
    title = input("Enter the new title: ")
    isbn = input("Enter the new ISBN: ")
    book_data = {
        'author': author,
        'title': title,
        'isbn': isbn
    }
    response = requests.put(f'{BASE_URL}/books/{book_id}', json=book_data)
    if response.status_code == 200:
        print('Book updated successfully.')
    else:
        print('Failed to update book.')


# Function to delete a book
def delete_book():
    print("***** Delete a Book *****")
    book_id = input("Enter the ID of the book to delete: ")
    response = requests.delete(f'{BASE_URL}/books/{book_id}')
    if response.status_code == 200:
        print('Book deleted successfully.')
    else:
        print('Failed to delete book.')


# Main CLI loop
def main():
    while True:
        display_menu()
        choice = input("Enter your choice (1-5): ")

        if choice == '1':
            get_books()
        elif choice == '2':
            add_book()
        elif choice == '3':
            update_book()
        elif choice == '4':
            delete_book()
        elif choice == '5':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.\n")


# Run the main CLI loop
if __name__ == '__main__':
    main()
