import pymongo
import json # parse as a dict
from collections import OrderedDict

#connection
myclient = pymongo.MongoClient("mongodb://localhost:27017/")

#DB name creates if does not exist
mydb = myclient["TweetyBird"]

#Collection
mycol = mydb["capture_metadata"]

# save JSON as a Schema to MongoDB 
with open('./models/Animal.json', 'r') as j:
  d = json.loads(j.read())
d = OrderedDict(d)
mydb.command(d)