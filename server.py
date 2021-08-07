from flask import Flask, flash, redirect, render_template, request, session
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
def show_book(book_id):
    """Show details on a particular book."""

    book = crud.get_book_by_id(book_id)

    return render_template('book_detail.html', book=book)


@app.route('/users')
def all_users():
    """View all users."""

    users = crud.get_users()
    return render_template('all_users.html', users=users)


@app.route('/users', methods=['POST'])
def register_user():
    """Create a new user."""

    username = request.form.get('username')
    first_name = request.form.get('first_name')
    last_name = request.form.get('last_name')
    email = request.form.get('email')
    password = request.form.get('password')

    user = crud.get_user_by_username(username)
    if user:
        flash('Cannot create an account with that email. Try again.')
    else:
        crud.create_user(username, first_name, last_name, email, password)
        flash('Account created! Please log in.')

    return render_template('homepage.html')


@app.route('/detail')
def user_detail():
    """View user profile"""

    logged_in_user = session.get('user_id')

    if logged_in_user != None:
        user = crud.get_user_by_id(session['user_id'])
        favorite_books = crud.get_favorites_by_user_id(user.user_id)
        
        return render_template('user_detail.html', user=user, favorite_books=favorite_books)

    return redirect('/')
    

@app.route('/login_form')
def login_form():

    return render_template('login.html')

@app.route('/signup_form')
def signup_form():
    return render_template('create_a.html')

@app.route('/add_favorite', methods=['POST'])
def add_favorite():
    book_id = request.form.get('book_id')
    user_id = session['user_id']
    favorite = crud.create_favorite(user_id, book_id)
    
    return redirect ('/detail')
    
    

@app.route('/login', methods=['POST'])
def log_in():
    username = request.form.get('username')
    password = request.form.get('password') 
    # print(username)
    user = crud.get_user_by_username(username)

    if user and user.password == password:
        flash("Logged in!")
        session['user_id'] = user.user_id
        
        return redirect('/')
    
    else:
        flash ('Incorrect username or password. Try again.')

        return redirect ('/')


@app.route('/logout')
def log_out():
    session.clear()
    flash("Logged out!")
    return redirect ('/') 


@app.route('/search')
def search_books():
   
   title_keywords = request.args.get('title_keywords')
   title_keywords = title_keywords.title()

   book_results_list = crud.search_books(title_keywords)

   return render_template('all_books.html', books=book_results_list)

           
if __name__ == '__main__':
    connect_to_db(app)
    app.debug = True
    app.run(host='0.0.0.0')