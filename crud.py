
from model import db, User, Favorite, Comment, Rating, Book

def create_user(username, email, password):
    """Create and return a new user."""

    user = User(username=username, email=email, password=password)

    db.session.add(user)
    db.session.commit()

    return user


def get_users():
    """Return all users."""

    return User.query.all()

def get_user_by_username(username):
    """Return user by username"""

    return User.query.get(username)


def get_user_by_id(user_id):
    """Return a user by primary key."""

    return User.query.get(user_id)


def get_user_by_email(email):
    """Return a user by email."""

    return User.query.filter(User.email == email).first()


def create_book(title, authors, average_rating, isbn, num_pages):
    """Create and return a new book."""

    book = Book(title = title,
                  authors = authors,
                  average_rating = average_rating,
                  isbn = isbn,
                  num_pages = num_pages
                  )

    db.session.add(book)
    db.session.commit()

    return book


def get_book():
    """Return all books ."""

    return Book.query.all()


def get_book_by_id(movie_id):
    """Return a book by primary key."""

    return Book.query.get(book_id)


def create_rating(user, book):
    """Create and return a new rating."""

    rating = Rating(user=user, book=book, )

    db.session.add(rating)
    db.session.commit()

    return rating



# if __name__ == '__main__':
    # from server import app
    # connect_to_db(app)
