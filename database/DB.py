import pymongo
import json # parse as a dict

#connection
myclient = pymongo.MongoClient("mongodb://localhost:27017/")

#DB name creates if does not exist
mydb = myclient["TweetyBird"]

#Collection
mycol = mydb["capture_metadata"]
