# Import necessary modules
from flask import Flask, request, render_template, redirect, url_for
import pymysql

# Initialize Flask app
app = Flask(__name__)

# Configure MySQL connection
conn = pymysql.connect(
    host='mybooks.ck380qchkwiz.us-east-2.rds.amazonaws.com',
    user='admin',
    password='fontaine2019+',
    db='mybooks',
    charset='utf8mb4',
    cursorclass=pymysql.cursors.DictCursor
)

# Model - Database operations
class Book:
    @staticmethod
    def get_all_books():
        with conn.cursor() as cursor:
            cursor.execute('SELECT * FROM mybook')
            books = cursor.fetchall()
        return books

    @staticmethod
    def get_book(book_id):
        with conn.cursor() as cursor:
            cursor.execute('SELECT * FROM mybook WHERE id = %s', (book_id,))
            book = cursor.fetchone()
        return book

    @staticmethod
    def create_book(author, title, isbn):
        with conn.cursor() as cursor:
            cursor.execute(
                'INSERT INTO mybook (author, title, isbn) VALUES (%s, %s, %s)',
                (author, title, isbn)
            )
            conn.commit()

    @staticmethod
    def update_book(book_id, author, title, isbn):
        with conn.cursor() as cursor:
            cursor.execute(
                'UPDATE mybook SET author = %s, title = %s, isbn = %s WHERE id = %s',
                (author, title, isbn, book_id)
            )
            conn.commit()

    @staticmethod
    def delete_book(book_id):
        with conn.cursor() as cursor:
            cursor.execute('DELETE FROM mybook WHERE id = %s', (book_id,))
            conn.commit()


# Controller - Route handlers
@app.route('/')
def index():
    books = Book.get_all_books()
    return render_template('index.html', books=books)

@app.route('/add', methods=['GET', 'POST'])
def add_book():
    if request.method == 'POST':
        author = request.form['author']
        title = request.form['title']
        isbn = request.form['isbn']
        Book.create_book(author, title, isbn)
        return redirect(url_for('index'))
    return render_template('add.html')

@app.route('/edit/<int:book_id>', methods=['GET', 'POST'])
def edit_book(book_id):
    book = Book.get_book(book_id)
    if request.method == 'POST':
        author = request.form['author']
        title = request.form['title']
        isbn = request.form['isbn']
        Book.update_book(book_id, author, title, isbn)
        return redirect(url_for('index'))
    return render_template('edit.html', book=book)

@app.route('/delete/<int:book_id>', methods=['GET', 'POST'])
def delete_book(book_id):
    Book.delete_book(book_id)
    return redirect(url_for('index'))

# Run the Flask application
if __name__ == '__main__':
    app.run(debug=True)
