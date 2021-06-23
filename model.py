
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class User(db.Model):
    """ Stores information about each user """

    __tablename__ = 'users'

    user_id = db.Column(db.Integer,
                primary_key = True,
                autoincrement = True,)
    username = db.Column(db.String(25), nullable = False, unique = True,) 
    first_name = db.Column(db.String(25), nullable = False,)
    last_name = db.Column(db.String(25), nullable = False,)
    email = db.Column(db.String(50), nullable = False,)
    password = db.Column(db.String(50), nullable = False,)
      
    def __repr__(self):
        return f'<User user_id={self.user_id} email={self.email}>'


class Favorite(db.Model):
    """ Store information about user's favorite books"""   

    __tablename__ = 'favorites'

    favorite_id = db.Column(db.Integer,
                primary_key = True,
                autoincrement = True,)
    user_id = db.Column(db.Integer, db.ForeignKey('users.user_id')) 
    book_id = db.Column(db.Integer, db.ForeignKey('books.book_id')) 

    book = db.relationship('Book', backref='favorites')
    user = db.relationship('User', backref='favorites')

    def __repr__(self):
        return f'<Favorite favorite_id={self.favorite_id} book_id={self.book_id}>'
    

class Comment(db.Model):
    """ A BOOK COMMENT """

    __tablename__ = 'comments'

    comment_id = db.Column(db.Integer,
                primary_key = True,
                autoincrement = True,)  
    user_id = db.Column(db.Integer, db.ForeignKey('users.user_id')) 
    book_id = db.Column(db.Integer, db.ForeignKey('books.book_id')) 
    comment = db.Column(db.String, nullable = False,)

    book = db.relationship('Book', backref='comments')
    user = db.relationship('User', backref='comments')
    
    def __repr__(self):
        return f'<Comment comment_id={self.comment_id} comment={self.comment}>'



class Rating(db.Model):
    """ A BOOK RATINGS """

    __tablename__ = 'ratings'

    rating_id = db.Column(db.Integer,
                primary_key = True,
                autoincrement = True,)  
    user_id = db.Column(db.Integer, db.ForeignKey('users.user_id')) 
    book_id = db.Column(db.Integer, db.ForeignKey('books.book_id')) 
    rating = db.Column(db.Integer, nullable = False,) # maybe chamge for String because I want the user make a review

    book = db.relationship('Book', backref='ratings')
    user = db.relationship('User', backref='ratings')

    def __repr__(self):
        return f'<Rating rating_id={self.rating_id} score={self.rating}>'


class Book(db.Model):
    """ BOOK """

    __tablename__ = 'books'

    book_id = db.Column(db.Integer,
                primary_key = True,
                autoincrement = True,)  
    title = db.Column(db.String, nullable = False,) 
    authors = db.Column(db.String, nullable = False,)
    average_rating = db.Column(db.Float, nullable = False,)
    rating_count = db.Column(db.Integer, nullable = True,)
    isbn = db.Column(db.String, nullable = False,)
    num_pages = db.Column(db.Integer, nullable = False,)

    def __repr__(self):
        return f'<Book book_id={self.book_id} title={self.title} authors={self.authors}>'


class Genre(db.Model):
    """ A BOOK GENRE """

    __tablename__ = 'genres'
    
    genre_id = db.Column (db.Integer,
                  primary_key = True,
                  autoincrement = True,)    
    genre = db.Column(db.String, nullable = False,)    

    def __repr__(self):
        return f'<Genre genre_id={self.book_id} genre={self.genre}>'   


class Genrebook(db.Model):

    __tablename__ = 'genrebooks'

    genrebook_id = db.Column (db.Integer,
                            primary_key = True,
                            autoincrement = True,)   
    genre_id = db.Column(db.Integer, db.ForeignKey('genres.genre_id')) 
    book_id = db.Column(db.Integer, db.ForeignKey('books.book_id')) 

    book = db.relationship('Book', backref='genrebooks')
    genre = db.relationship('Genre', backref='genrebooks')     
    
    def __repr__ (self):
        return f'<Genrebook genrebook_id={self.genrebook_id} genrebook={self.genrebook}>'                               


def connect_to_db(flask_app, db_uri='postgresql:///mybookshelf', echo=True):
    flask_app.config['SQLALCHEMY_DATABASE_URI'] = db_uri
    flask_app.config['SQLALCHEMY_ECHO'] = echo
    flask_app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.app = flask_app
    db.init_app(flask_app)

    print('Connected to the db!')


if __name__ == '__main__':
    from server import app

    connect_to_db(app)           