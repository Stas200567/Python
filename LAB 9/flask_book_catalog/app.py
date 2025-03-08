from flask import Flask, request, jsonify
from flask_restful import Resource, Api
import json

app = Flask(__name__)
api = Api(app)

# Файл для збереження даних
BOOKS_FILE = "books.json"

def load_books():
    """Завантаження книг з JSON файлу"""
    try:
        with open(BOOKS_FILE, "r") as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        return []

def save_books(books):
    """Збереження книг у JSON файл"""
    with open(BOOKS_FILE, "w") as f:
        json.dump(books, f, indent=4)

# Завантажуємо книги при старті
books = load_books()

class BookList(Resource):
    def get(self):
        return jsonify(books)

    def post(self):
        new_book = request.get_json()
        new_book["id"] = books[-1]["id"] + 1 if books else 1
        books.append(new_book)
        save_books(books)
        return new_book, 201

class Book(Resource):
    def get(self, book_id):
        book = next((book for book in books if book["id"] == book_id), None)
        if book:
            return jsonify(book)
        return {"message": "Book not found"}, 404

    def put(self, book_id):
        book = next((book for book in books if book["id"] == book_id), None)
        if book:
            data = request.get_json()
            book.update(data)
            save_books(books)
            return book, 200
        return {"message": "Book not found"}, 404

    def delete(self, book_id):
        global books
        books = [book for book in books if book["id"] != book_id]
        save_books(books)
        return {"message": "Book deleted"}, 200

api.add_resource(BookList, "/books")
api.add_resource(Book, "/books/<int:book_id>")

@app.errorhandler(404)
def not_found(error):
    return jsonify({"message": "Resource not found"}), 404

@app.errorhandler(400)
def bad_request(error):
    return jsonify({"message": "Bad request"}), 400

if __name__ == "__main__":
    app.run(debug=True)
