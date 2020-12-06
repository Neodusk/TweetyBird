import sys
sys.path.insert(1, './database')
import DB
import io
import tweepy
from google.cloud import vision
from google.cloud.vision import types
from google.cloud import storage
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
    for label in labels:
        print(label.description)
        tweetText = tweetText + " " + label.description
        if "cat" in tweetText:
            animalInPic = True

    # tweepy
    consumer_key = "XXXX"
    consumer_secret = "XXXX"
    access_token_secret = "XXXX"
    access_token = "XXXX"
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
    return

    """
    Users can put code here that needs to be run
    after motion detected and image/video taken
    Eg Notify or activate something.
    Note all functions and variables will be imported.
    pi-timolo.py will execute this function userMotionCode(filename)
    in pi-timolo.py per example below
        user_motion_code.userMotionCode(filename)
    """
