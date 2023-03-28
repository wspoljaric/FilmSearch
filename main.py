#Import pymongo for connectivity to Mongo Atlas cloud DB
from pymongo import MongoClient

#Import Flask & request for interface with API calls based on url path
from flask import Flask
from flask_restful import Api, Resource

#Import settings file for connection details to Mongo Atlas cloud DB
from settings import mongo_path

#import re for regex for case insensitive searches
import re


#Point at Mongo DB cluster with credentials and set which collection and DB being utilized.
cluster = MongoClient(mongo_path)
db = cluster["FilmSearch"]
collection = db["FilmSearchDB"]


#Initialize Flask
app = Flask(__name__)
api = Api(app)

#class for showtype API, takes in 'type' - eg. 'Movie' or 'Show' and returns all items from Mongo Atlas DB that match.
#Removes _id as this is not useful for client, and flags to include the title and type in return json
#Uses regex to make the search non case sensitive and returns results for partial strings
class ShowType(Resource):
    def get(self, type):
        data = collection.find({"type":re.compile(type, re.IGNORECASE)},{"_id": 0, "title": 1, "type": 1})
        resp = list(data)
        return resp

#class for genre API, takes in 'genre' - eg. 'Thriller' or 'Documentary' and returns all items from Mongo Atlas DB that match.
#Removes _id as this is not useful for client, and flags to include the title and genre in return json    
#Uses regex to make the search non case sensitive and returns results for partial strings
class Genre(Resource):
    def get(self, genre):
        data = collection.find({"listed_in":re.compile(genre, re.IGNORECASE)},{"_id": 0, "title": 1, "listed_in": 1})
        resp = list(data)
        return resp

#class for cast API, takes in 'cast' - eg. 'John Smith' or 'John' and returns all items from Mongo Atlas DB that match.
#Removes _id as this is not useful for client, and flags to include the title and genre in return json    
#Uses regex to make the search non case sensitive and returns results for partial strings
class Cast(Resource):
    def get(self, cast):
        data = collection.find({"cast":re.compile(cast, re.IGNORECASE)},{"_id": 0, "title": 1, "cast": 1})
        resp = list(data)
        return resp

#class for Title API, takes in 'title' - returns the item from Mongo Atlas DB that match.
#Removes _id as this is not useful for client, and flags to include the title in return json       
#Uses regex to make the search non case sensitive and returns results for partial strings
class Title(Resource):
    def get(self, title):
        data = collection.find_one({"title":re.compile(title, re.IGNORECASE)},{"_id": 0, "title": 1})
        resp = list(data)
        return resp

#adding the api resources and mapping to the url to return the correct data 
api.add_resource(ShowType,"/showtype/<string:type>")
api.add_resource(Genre,"/genre/<string:genre>")
api.add_resource(Cast,"/cast/<string:cast>")
api.add_resource(Title,"/title/<string:title>")

if __name__ == "__main__":
    app.run(debug=True)
