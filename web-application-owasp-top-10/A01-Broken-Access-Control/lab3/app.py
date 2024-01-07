#https://github.com/saeedzaze/Web-Application-Security

from flask import Flask, render_template, jsonify, request

app = Flask(__name__)

# Dummy data as a simple in-memory database
books = {'1': {'title': 'Book 1', 'author': 'Author 1', 'description': 'Description for Book 1'},
         '2': {'title': 'Book 2', 'author': 'Author 2', 'description': 'Description for Book 2'},
         '3': {'title': 'Book 3', 'author': 'Author 3', 'description': 'Description for Book 3'},
         '4': {'title': 'Book 4', 'author': 'Author 4', 'description': 'Description for Book 4'}}

# Home page to display book names
@app.route('/')
def index():
    return render_template('index.html', books=books)

# API endpoint for DELETE request (without proper access controls)
@app.route('/api/books/<book_id>', methods=['DELETE'])
def delete_book(book_id):
    if book_id in books:
        del books[book_id]
        return jsonify({'message': 'Book deleted successfully. FLAG_LAB3_SAZE'})
    else:
        return jsonify({'error': 'Book not found'})

# Route to display detailed information for a selected book
@app.route('/book/<book_id>')
def book_detail(book_id):
    book = books.get(book_id)
    if book:
        return render_template('book_detail.html', book=book)
    else:
        return render_template('error.html', message='Book not found')

if __name__ == '__main__':
    app.run(debug=True)

