
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class User(db.Model):
    """ USER """

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


class Favorite (db.Model):
        """ FAVORITE BOOKS"""   

     __tablename__ = 'favorites'

    favorite_id = db.Column(db.Integer,
                primary_key = True,
                autoincrement = True,)
    user_id = db.Column(db.String(25), db.ForeignKey('users.user_id')) 
    book_id = db.Column(db.String(25), db.ForeignKey('books.book_id')) 

    def __repr__(self):
        return f'<Favorite favorite_id={self.favorite_id} book_id={self.book_id}>'
    

class Comment (db.Model):
    """ A BOOK COMMENT """

    __tablename__ = 'comments'

    comment_id = db.Column(db.Integer,
                primary_key = True,
                autoincrement = True,)  
    user_id = db.Column(db.String(25), db.ForeignKey('users.user_id')) 
    book_id = db.Column(db.String(25), db.ForeignKey('books.book_id')) 
    comment = db.Column(db.String(), nullable = False,)
    
    def __repr__(self):
        return f'<Comment comment_id={self.comment_id} comment={self.comment}>'



class Ratings (db.Model):
    """ A BOOK RATINGS """

    __tablename__ = 'ratings'

    rating_id = db.Column(db.Integer,
                primary_key = True,
                autoincrement = True,)  
    user_id = db.Column(db.String(25), db.ForeignKey('users.user_id')) 
    book_id = db.Column(db.String(25), db.ForeignKey('books.book_id')) 
    rating = db.Column(db.Integer(), nullable = False,)

    def __repr__(self):
        return f'<Rating rating_id={self.rating_id} score={self.rating}>'

class Books (db.Model):
    """ BOOK """

    __tablename__ = 'books'
    book_id = db.Column(db.Integer,
                primary_key = True,
                autoincrement = True,)  
    title = db.Column(db.String(), nullable = False, unique = True,) 
    author = db.Column(db.String(), nullable = False,)
    genre_id = db.Column(db.String(), db.ForeignKey('genres.genre_id')) 
    average_rating = db.Column(db.Float(5), nullable = False,)
    rating_count = db.Column(db.Integer(), nullable = False,)
    isbn = db.Column(db.String(50), nullable = False,)
    num_pages = db.Column(db.Integer(), nullable = False,)

    def __repr__(self):
        return f'<Book book_id={self.book_id} title={self.title} author={self.author}>'

class Genres(db.Model):
    """ A BOOK GENRE """

    __tablename__ = 'genres'
    genre_id = db.Column (db.Integer,
                  primary_key = True,
                  autoincrement = True,)    
    genre = db.Column(db.String(), nullable = False,)    

    def __repr__(self):
        return f'<Genre genre_id={self.book_id} genre={self.genre}>'   





if __name__ == '__main__':
    from server import app

    connect_to_db(app)           