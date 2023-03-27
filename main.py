#Import pymongo for connectivity to Mongo Atlas cloud DB
import pymongo
from pymongo import MongoClient
#Import settings file for connection details to Mongo Atlas cloud DB
from settings import mongo_path

#Import Flask & request for interface with API calls based on url path
import flask
from flask import Flask, jsonify

from flask_restful import Api, Resource

#import the json_util to convert mongoDB data to JSON

#Point at Mongo DB cluster with credentials and set which collection and DB being utilized.
cluster = MongoClient(mongo_path)
db = cluster["FilmSearch"]
collection = db["FilmSearchDB"]


#Initialize Flask
app = Flask(__name__)
api = Api(app)

#class for showtype API, takes in 'type' - eg. 'Movie' or 'Show' and returns all items from Mongo Atlas DB that match.
#Removes _id as this is not useful for client, and flags to include the title and type in return json
class ShowType(Resource):
    def get(self, type):
        data = collection.find({"type":type},{"_id": 0, "title": 1, "type": 1})
        resp = list(data)
        return resp

#class for genre API, takes in 'genre' - eg. 'Thriller' or 'Documentary' and returns all items from Mongo Atlas DB that match.
#Removes _id as this is not useful for client, and flags to include the title and genre in return json    
class Genre(Resource):
    def get(self, genre):
        data = collection.find({"listed_in":genre},{"_id": 0, "title": 1, "listed_in": 1})
        resp = list(data)
        return resp
    
class Cast(Resource):
    def get(self):
        return

#class for Title API, takes in 'title' - returns the item from Mongo Atlas DB that match.
#Removes _id as this is not useful for client, and flags to include the title in return json       
class Title(Resource):
    def get(self, title):
        data = collection.find_one({"title":title},{"_id": 0, "title": 1})
        resp = list(data)
        return data

#adding the api resources and mapping to the url to return the correct data 
api.add_resource(ShowType,"/showtype/<string:type>")
api.add_resource(Genre,"/genre/<string:genre>")
api.add_resource(Cast,"/cast")
api.add_resource(Title,"/title/<string:title>")

if __name__ == "__main__":
    app.run(debug=True)
