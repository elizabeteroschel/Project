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
        return render_template('user_detail.html', user=user)

    return redirect('/')
    


@app.route('/login', methods=['POST'])
def log_in():
    username = request.form.get('username')
    password = request.form.get('password') 
    # print(username)
    user = crud.get_user_by_username(username)

    if user and user.password == password:
        flash("Logged in!")
        session['user_id'] = user.user_id
        
        return redirect('/detail')
    
    else:
        flash ('Incorrect username or password. Try again.')

        return redirect ('/')
       
    

# get all forms input (username and password)
# crud function query user based on that input(username )
# if get user right user name and password and add to session (ex user id)

#if dont find the user back none (flash message log in failed)
#  return to any page I want (wx: homepage or user) 
# flash message
    

if __name__ == '__main__':
    connect_to_db(app)
    app.debug = True
    app.run(host='0.0.0.0')