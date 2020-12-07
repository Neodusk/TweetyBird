import sys
sys.path.insert(1, './database')
from DB import mycol
from DB import animals
import io
import tweepy
import base64
import json
from google.cloud import vision
from google.cloud.vision import types
from google.cloud import storage
from datetime import date
"""
SOURCE: https://github.com/themagpimag/magpi-issue71/blob/master/WildlifeTrap/listing2.py
This module will be imported into pi-timolo.py and will
execute the userMotionCode function after
motion is detected.  The filenamePath will be passed
in case you want to process the file as an attachment
or include in a message, Etc.  If you need to import other
python modules they can be added to the top of this
module and used in the userMotionCode.
You can also include other functions within this module
as long as they are directly or indirectly called
within the userMotionCode function since that is
the only function that is called in the pi-timolo.py
program when motion is detected.
For more information see pi-timolo github Wiki
"""

#------------------------------------------------------------------------------
def userMotionCode(filename):
    with open('./database/animalData.json') as jsonFile:
        AnimalData = json.load(jsonFile)
        animals.insert_many(AnimalData);
    client = storage.Client()
    client = vision.ImageAnnotatorClient()

    with io.open(filename, 'rb') as image_file:
        content = image_file.read()

    image = types.Image(content=content)

    response = client.label_detection(image=image)
    labels = response.label_annotations

    # we have our labels, now create a string to add to the tweet message
    print('Labels:')
    tweetText = "Labels: "
    animalInPic = False
    
    result = animals.find()
    animalsInDB = ([document["commonName"] for document in result])
    utf8Animal = [i.encode('UTF8') for i in animalsInDB]
    uniqueAnimal = set(utf8Animal)
    uniqueAnimalList = []
    for ani in uniqueAnimal:
        uniqueAnimalList.append(ani)
    for label in labels:
        print(label.description)
        tweetText = tweetText + " " + label.description
        for anim in uniqueAnimalList:
            if anim in tweetText:
                print("Animal detected!")
                animalInPic = True

    # tweepy
    consumer_key = "XXX"
    consumer_secret = "XXX"    
    access_token_secret = "XXX"
    access_token = "XXX"
    # authorisation process, using the keys and tokens
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    # creation of the actual interface, using authentication
    api = tweepy.API(auth)

    # send the tweet with photo and message
    photo_path = filename
    # only send tweet if it contains a desired animal
    if animalInPic:
      api.update_with_media(photo_path, status=tweetText)
      # if animalNotInDatabase
      # store animal to database/ log appearance
    else:
        with open(filename, "rb") as img_file:
            encoded_string = base64.b64encode(img_file.read())
            img = encoded_string
            unknownMotion = { 	 	
              "labels": tweetText, 	
              "timestamp": date.today().strftime('%m/%d/%Y'),
              "image": {
              "data": img,
            }
        }	
        mycol.insert_one(unknownMotion)
