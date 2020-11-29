import sys
sys.path.append('/backend')
import DB

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
def userMotionCode(filenamePath):
    # we need to create an instance of the Google Vision API
    client = storage.Client()
    # instantiates a client
    client = vision.ImageAnnotatorClient()

    # loads the image into memory
    with io.open(filename, 'rb') as image_file:
        content = image_file.read()

    image = types.Image(content=content)

    # performs label detection on the image file
    response = client.label_detection(image=image)
    # pass the response into a variable
    labels = response.label_annotations

    # we have our labels, now create a string to add to the tweet message
    # for debugging - let’s see what Google thinks is in the image
    print('Labels:')
    # add labels to our tweet text
    tweetText = "Labels: "
    animalInPic = False
    for label in labels:
        print(label.description)
        tweetText = tweetText + " " + label.description
        # edit this line to change the animal you want to detect
        if "bird" in tweetText: animalInPic = true

    # set up Tweepy
    # consumer keys and access tokens, used for authorisation
    consumer_key = ‘XXX’
    consumer_secret = ‘XXX’
    access_token = ‘XXX’
    access_token_secret = ‘XXX’

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
    #How we hold certain values such as species and data ?
    #subject to change
    myAnimal = { 
        "id": _id, 
        "species": "bird", 
        "timestamp": Date.now(), 
            }
    mycol.insert_one(myAnimal)

    """
    Users can put code here that needs to be run
    after motion detected and image/video taken
    Eg Notify or activate something.

    Note all functions and variables will be imported.
    pi-timolo.py will execute this function userMotionCode(filename)
    in pi-timolo.py per example below

        user_motion_code.userMotionCode(filename)

    """
    # Insert User code Below
    # print("User Code Executing from userMotionCode function")
    # print("file path is %s" % filenamePath)
