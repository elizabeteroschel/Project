
from model import db, User, Favorite, Comment, Rating, Book, connect_to_db


def create_user(username, first_name, last_name, email, password):
    """Create and return a new user."""

    user = User(username=username, first_name=first_name, last_name=last_name, email=email, password=password)

    db.session.add(user)
    db.session.commit()

    return user

def create_favorite(user_id, book_id):
    """Create and return a new user favorite ."""

    favorite = Favorite(user_id=user_id, book_id=book_id)

    db.session.add(favorite)
    db.session.commit()

    return favorite 

def get_users():
    """Return all users."""

    return User.query.all()

def get_user_by_username(username):
    """Return user by username"""

    return User.query.filter(User.username == username).first()

def get_user_by_id(user_id):
    """Return a user by primary key."""

    return User.query.get(user_id)

def get_user_by_email(email):
    """Return a user by email."""

    return User.query.filter(User.email == email).first()

def create_book(title, authors, average_rating, rating_count, isbn, num_pages):
    """Create and return a new book."""

    book = Book(title = title,
                  authors = authors,
                  average_rating = average_rating,
                  rating_count = rating_count,
                  isbn = isbn,
                  num_pages = num_pages
                  )

    db.session.add(book)
    db.session.commit()

    return book

def get_book():
    """Return all books ."""

    return Book.query.all()

def get_favorites_by_user_id(user_id):
    """Return favorite books by user_id ."""

    return Favorite.query.filter(Favorite.user_id == user_id).all()

def get_book_by_id(book_id):
    """Return a book by primary key."""

    return Book.query.get(book_id)
   
def create_rating(user, book, rating):
    """Create and return a new rating."""

    rating = Rating(user=user, book=book, rating=rating)

    db.session.add(rating)
    db.session.commit()


    return rating

def search_books(title_keywords):

    books = Book.query.filter(Book.title.like('%' + title_keywords +'%')).all()

    return books
       
def all_users():
     """Show all users."""

     return User.query.all()   

if __name__ == '__main__':
    from server import app
    connect_to_db(app)
