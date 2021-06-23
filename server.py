from flask import Flask, render_template, request
import requests
from model import connect_to_db
import crud
from jinja2 import StrictUndefined

app = Flask(__name__)
app.secret_key = "dev"
app.jinja_env.undefined = StrictUndefined

@app.route('/')
def homepage():
    """View homepage."""

    return render_template('homepage.html')


@app.route('/books')
def all_books():
    """View all books."""

    books = crud.get_book()

    return render_template('all_books.html', books=books)


@app.route('/books/<book_id>')
def show_movie(book_id):
    """Show details on a particular book."""

    movie = crud.get_book_by_id(book_id)

    return render_template('book_details.html', book=book)


# @app.route('/users')
# def all_users():
#     """View all users."""

#     users = crud.get_users()

#     return render_template('all_users.html', users=users)


@app.route('/users', methods=['POST'])
def register_user():
    """Create a new user."""

    usernama = request.form.get('username')
    email = request.form.get('email')
    password = request.form.get('password')

    user = crud.get_user_by_email(email)
    if user:
        flash('Cannot create an account with that email. Try again.')
    else:
        crud.create_user(email, password)
        flash('Account created! Please log in.')

    return redirect('/')


# @app.route('/register', methods=['POST'])
# def register_user():
#     email = request.form['email']
#     password = request.form['password']

#     user = User.query.filter(User.email == email).first()
#     if user:
#         return 'A user already exists with that email.'
#     else:
#         new_user = User(email=email, password=password)
#         db.session.add(new_user)
#         db.session.commit(new_user)

#         return redirect('/login-form')    


@app.route('/users/<user_id>')
def show_user(user_id):
    """Show details on a particular user."""

    user = crud.get_user_by_id(user_id)

    return render_template('user_details.html', user=user)




if __name__ == '__main__':
    connect_to_db(app)
    app.debug = True
    app.run(host='0.0.0.0')