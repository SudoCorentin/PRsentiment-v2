# https://replit.com/talk/learn/How-to-make-Rest-Api-in-Python/9038

# Create webserver
from flask import Flask
from threading import Thread
from flask_restful import Resource, Api
from process import *

app = Flask('')
# Flask restful comes with an Api function that makes your life much better than with Flask only.
api = Api(app)

class Home(Resource):
  def get(self):
    return "Hello, my dear friend!"

class DoNothing(Resource):

  def get(self, word):
    return do_nothing(word)


class PrComment(Resource):

  def get(self, comment):
    return get_comment_polarity(comment)


class PrCommentsList(Resource):

  def post(self, comment_list):
    return get_many_comments_polarity(comment_list)


api.add_resource(Home, '/')
api.add_resource(DoNothing, '/api/donothing/<string:word>')
api.add_resource(PrComment, '/api/prcomment/<string:comment>')
# api.add_resource(PrCommentsList, '/api/prcommentlist/<string:comment_list>')


def run():
  app.run(host='0.0.0.0', port=7210)


t = Thread(target=run)
t.start()
