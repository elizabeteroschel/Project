import os
import json
import csv
from random import choice, randint
from datetime import datetime

import crud
import model
import server

os.system('dropdb mybookshelf')
os.system('createdb mybookshelf')

model.connect_to_db(server.app)
model.db.create_all()

books_in_db = []
# genres_in_db = []
with open ('data/books.csv', newline = '') as csvfile:
    book_data = csv.DictReader(csvfile)

# 
  


    for book in book_data:
        title, authors,  average_rating, rating_count, isbn, num_pages = (book['title'],
                                        book['authors'],
                                        book['average_rating'],
                                        book['ratings_count'],
                                        book['isbn'],
                                        book.get('num_pages', 0))

    
        db_book = crud.create_book(title,
                                    authors,
                                    average_rating,
                                    rating_count,
                                    isbn,
                                    num_pages
                                    )
        books_in_db.append(db_book)

    # for genre in genre_data:
    #     genre = (book['genre'])
                                    
    
    #     db_book = crud.create_genre(genre
    #                                 )
    #     genres_in_db.append(db_genre)


for n in range(10):
    username = f'user{n}'
    first_name = 'test'
    last_name = 'testtest'
    email = f'user{n}@test.com'  
    password = 'test'

    user = crud.create_user(username, first_name, last_name, email, password)

    # for _ in range(10):
    #     random_book = choice(books_in_db)
    #     score = randint(1, 5)

    #     crud.create_rating(user, random_book, ratings)
