from goodreads import client
import pandas as pd
import re

api_key = "U2CUrCrMyOk5snwBlF7mCg"
api_secret = "OhC7UkQPm6AmX5FPmOW4WVrN0XCJ7ebtKLdNyDGbA"
gc = client.GoodreadsClient(api_key, api_secret)

books = pd.read_csv('dataset_final.csv', delimiter=";", header=0)
print(books.columns)

def extract_id(string):
    try:
        x = re.search(r"\d+", string).group()
    except AttributeError:
        x = ""
    return x

books["goodreads_id"] = books["link to goodreads"].apply(lambda x: extract_id(x))
#print(books["goodreads_id"])
print("hi")
books["goodreads_average_rating"] = books["goodreads_id"].apply(lambda x: gc.book(x).average_rating)
#print(books["goodreads_average_rating"])
print("hi")
books["goodreads_ratings_count"] = books["goodreads_id"].apply(lambda x: gc.book(x).ratings_count)
#print(books["goodreads_ratingscount"])
print("hi")
books["goodreads_text_reviews_count"] = books["goodreads_id"].apply(lambda x: gc.book(x).text_reviews_count)
#print(books["goodreads_text_reviews_count"])
print("hi")

#book = gc.book("827")
#print(dir(book))
#print(book.title)
#print(book.rating_dist)
#print(book.ratings_count)
#print(book.text_reviews_count)
#print(book.average_rating)

books.to_csv('dataset_extended.csv', index=False)
