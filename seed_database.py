import os
import json
from random import choice, randint
from datetime import datetime

import crud
import model
import server

os.system('dropdb mybookshelf')
os.system('createdb mybookshelf')

model.connect_to_db(server.app)
model.db.create_all()

# Load movie data from JSON file
with open('data/books.json') as f:
    book_data = json.loads(f.read())

# Create movies, store them in list so we can use them
# to create fake ratings
books_in_db = []
for book in book_data:
    title, author, average_rating, isbn, num_pages = (book['title'],
                                    book['author],
                                    book['average_rating'],
                                    book['isbn']
                                    book['num_pages'])

    db_book = crud.create_book(title,
                                author,
                                average_rating,
                                isbn,
                                num_pages
                                 )
    books_in_db.append(db_book)

# Create 10 users; each user will make 10 ratings
for n in range(10):
    email = f'user{n}@test.com'  # Voila! A unique email!
    password = 'test'

    user = crud.create_user(email, password)

    for _ in range(10):
        random_book = choice(books_in_db)
        score = randint(1, 5)

        crud.create_rating(user, random_book, ratings)
