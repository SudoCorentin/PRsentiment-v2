import nltk
import pandas as pd

nltk.download('punkt')
from textblob import TextBlob

def do_nothing(word):
  return word

def jsonify_csv_input(n):
  comments = pd.read_csv("dummy_comments.csv").drop(columns='createdAt').head(n)
  return comments.body.to_json()

def get_file_polarity():
  comments = pd.read_csv("dummy_comments.csv").drop(columns='createdAt').head(5)
  # for each row, run textblob on the column body and write the result   in a new column called "polarity"
  comments['polarity'] = comments.body.apply(
    lambda x: TextBlob(x).sentiment.polarity)
  return comments.to_json()

def get_comment_polarity(comment):
  return {
    "COMMENT": comment,
    "POLARITY": TextBlob(comment).sentiment.polarity
  }

def get_many_comments_polarity(comment_list):
  return [get_comment_polarity(comment) for comment in comment_list]
     
  