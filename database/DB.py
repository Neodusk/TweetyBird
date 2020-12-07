import pymongo

#connection
myclient = pymongo.MongoClient("mongodb://localhost:27017/")

#DB name creates if does not exist
mydb = myclient["TweetyBird"]

#Collection
animals = mydb["animals"]
mycol = mydb["unknownCaptures"]
