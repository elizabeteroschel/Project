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
with open ('data/books.csv', newline = '') as csvfile:
    book_data = csv.DictReader(csvfile)

 
  


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
