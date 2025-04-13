from flask import Blueprint, jsonify, request
from .models import db, User, Book, Category

bp = Blueprint('routes', __name__)

@bp.route('/users', methods=['GET'])
def get_users():
    users = User.query.all()
    return jsonify([{'id': u.id, 'name': u.name, 'email': u.email} for u in users])

@bp.route('/users', methods=['POST'])
def add_user():
    data = request.json
    user = User(name=data['name'], email=data['email'], password=data['password'])
    db.session.add(user)
    db.session.commit()
    return jsonify({'message': 'User created'}), 201

@bp.route('/books', methods=['GET'])
def get_books():
    books = Book.query.all()
    return jsonify([{'id': b.id, 'title': b.title, 'author': b.author, 'year': b.publication_year} for b in books])

@bp.route('/books', methods=['POST'])
def add_book():
    data = request.json
    book = Book(title=data['title'], author=data['author'],
                publication_year=data['publication_year'],
                category_id=data['category_id'])
    db.session.add(book)
    db.session.commit()
    return jsonify({'message': 'Book added'}), 201

@bp.route('/categories', methods=['GET'])
def get_categories():
    categories = Category.query.all()
    return jsonify([{'id': c.id, 'name': c.name} for c in categories])

@bp.route('/categories', methods=['POST'])
def add_category():
    data = request.json
    category = Category(name=data['name'])
    db.session.add(category)
    db.session.commit()
    return jsonify({'message': 'Category created'}), 201