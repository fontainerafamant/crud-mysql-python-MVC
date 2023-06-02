import tkinter as tk
from tkinter import messagebox
import requests


# Base URL of the backend Flask application
BASE_URL = 'http://localhost:5000'


# Function to get all books
def get_books():
    response = requests.get(f'{BASE_URL}/books')
    if response.status_code == 200:
        books = response.json()
        book_details = ""
        for book in books:
            book_details += f"ID: {book['id']}\nAuthor: {book['author']}\nTitle: {book['title']}\nISBN: {book['isbn']}\n\n"
        messagebox.showinfo("Book Details", book_details)
    else:
        messagebox.showerror("Error", "Failed to retrieve books.")


# Function to add a new book
def add_book():
    def add_book_submit():
        author = author_entry.get()
        title = title_entry.get()
        isbn = isbn_entry.get()
        book_data = {
            'author': author,
            'title': title,
            'isbn': isbn
        }
        response = requests.post(f'{BASE_URL}/books', json=book_data)
        if response.status_code == 201:
            messagebox.showinfo("Success", "Book added successfully.")
            add_book_window.destroy()
        else:
            messagebox.showerror("Error", "Failed to add book.")

    add_book_window = tk.Toplevel()
    add_book_window.title("Add Book")

    author_label = tk.Label(add_book_window, text="Author:")
    author_label.pack()
    author_entry = tk.Entry(add_book_window)
    author_entry.pack()

    title_label = tk.Label(add_book_window, text="Title:")
    title_label.pack()
    title_entry = tk.Entry(add_book_window)
    title_entry.pack()

    isbn_label = tk.Label(add_book_window, text="ISBN:")
    isbn_label.pack()
    isbn_entry = tk.Entry(add_book_window)
    isbn_entry.pack()

    submit_button = tk.Button(add_book_window, text="Add Book", command=add_book_submit)
    submit_button.pack()


# Function to update an existing book
def update_book():
    def update_book_submit():
        book_id = id_entry.get()
        author = author_entry.get()
        title = title_entry.get()
        isbn = isbn_entry.get()
        book_data = {
            'author': author,
            'title': title,
            'isbn': isbn
        }
        response = requests.put(f'{BASE_URL}/books/{book_id}', json=book_data)
        if response.status_code == 200:
            messagebox.showinfo("Success", "Book updated successfully.")
            update_book_window.destroy()
        else:
            messagebox.showerror("Error", "Failed to update book.")

    update_book_window = tk.Toplevel()
    update_book_window.title("Update Book")

    id_label = tk.Label(update_book_window, text="Book ID:")
    id_label.pack()
    id_entry = tk.Entry(update_book_window)
    id_entry.pack()

    author_label = tk.Label(update_book_window, text="Author:")
    author_label.pack()
    author_entry = tk.Entry(update_book_window)
    author_entry.pack()

    title_label = tk.Label(update_book_window, text="Title:")
    title_label.pack()
    title_entry = tk.Entry(update_book_window)
    title_entry.pack()

    isbn_label = tk.Label(update_book_window, text="ISBN:")
    isbn_label.pack()
    isbn_entry = tk.Entry(update_book_window)
    isbn_entry.pack()

    submit_button = tk.Button(update_book_window, text="Update Book", command=update_book_submit)
    submit_button.pack()


# Function to delete
# Function to delete a book
def delete_book():
    def delete_book_submit():
        book_id = id_entry.get()
        response = requests.delete(f'{BASE_URL}/books/{book_id}')
        if response.status_code == 200:
            messagebox.showinfo("Success", "Book deleted successfully.")
            delete_book_window.destroy()
        else:
            messagebox.showerror("Error", "Failed to delete book.")

    delete_book_window = tk.Toplevel()
    delete_book_window.title("Delete Book")

    id_label = tk.Label(delete_book_window, text="Book ID:")
    id_label.pack()
    id_entry = tk.Entry(delete_book_window)
    id_entry.pack()

    submit_button = tk.Button(delete_book_window, text="Delete Book", command=delete_book_submit)
    submit_button.pack()


# Create the main application window
root = tk.Tk()
root.title("Bookstore Management")

# Create buttons for each operation
get_books_button = tk.Button(root, text="Get All Books", command=get_books)
get_books_button.pack(pady=10)

add_book_button = tk.Button(root, text="Add Book", command=add_book)
add_book_button.pack(pady=10)

update_book_button = tk.Button(root, text="Update Book", command=update_book)
update_book_button.pack(pady=10)

delete_book_button = tk.Button(root, text="Delete Book", command=delete_book)
delete_book_button.pack(pady=10)

# Start the Tkinter event loop
root.mainloop()
