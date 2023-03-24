#Import pymongo for connectivity to Mongo Atlas cloud DB
import pymongo
from pymongo import MongoClient

#Import settings file for connection details to Mongo Atlas cloud DB
from settings import mongo_path

#Import flask & request for interface with API calls based on url path
import flask
from flask import Flask, request

#Point at Mongo DB cluster with credentials and set which collection and DB being utilized.
cluster = MongoClient(mongo_path)
db = cluster["FilmSearch"]
collection = db["FilmSearchDB"]

#Query the DB for the show with the ID 's1' which is a column in our DB, print results.
results = collection.find_one({"show_id":"s1"})
print(results)