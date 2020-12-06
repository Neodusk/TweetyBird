# TweetyBird
Captures pictures of animals and uses AI to detect species. Uploads a capture of the animal and logs data about the animals appearance

We followed [this guide](https://magpi.raspberrypi.org/articles/wildlife-camera-object-recognition) to help in knowing which libraries might be best for this project and how to go about it. 

# Hardware Used:
- Raspberry Pi 3B
- Power cables for the Raspberry Pi
- SD storage for the Raspberry Pi
- A Raspberry Pi [camera](https://www.amazon.com/gp/product/B07JPLV5K1/).

# Dependencies Required:
## pi-timolo
### Instructions:
Plug in a camera to the Raspberry Pi.

Install pi-timolo:
```
wget https://raw.github.com/pageauc/pi-timolo/master/source/pi-timolo-install.sh
chmod +x pi-timolo-install.sh
./pi-timolo-install.sh
```
This may take some time.
Once that is complete, run `sudo raspi-config Interfacing Options` and enable I2C and Pi Camera.

It is recommended to run ```sudo apt-get update && sudo apt-get dist-upgrade```
and then restart with ```sudo reboot```

To make sure your camera is detected, navigate to the pi-timolo directory and run the .`py` script.
```cd ./pi-timolo && ./pi-timolo.py```

"Check the pictures by waving your hand in front of the camera, then looking in `~/pi-timolo/media/recent/motion`. You may need to change the image size and orientation of the camera; in the Terminal window, enter `nano config.py` and edit these variables: imageWidth, imageHeight, and imageRotation" [(source).](https://magpi.raspberrypi.org/articles/wildlife-camera-object-recognition)

## Setting up Tweepy 
Set up a Twitter account or use an existing one.
Install Tweepy:
 
 ```sudo pip install tweepy```
 
Go [here](https://developer.twitter.com/apps) to create a new Twitter app
- Click Create an app (you may have to apply for a developer account and this may take some time).
- Once your account is approved as a developer account, click on "Keys and Access Tokens".
- You will need these keys and tokens for the next step

### Inside of the ~/pi-timolo directory:
- Replace the pi-timolo.py file with the one in this repository
- Replace the user_motion_code.py with the one in this repository
- Edit the following user_motion_code.py variable values of 'XXX' with your keys and tokens you setup on Twitter 
```
    consumer_key = "XXX"
    consumer_secret = "XXX"
    access_token = "XXX"
    access_token_secret = "XXX"
```
## Pymongo
Install pymongo using pip:
```sudo pip install pymongo```
Install MongoDB using apt-get:
```sudo apt-get install mongodb```
## Database
NOTE: Database is not created until it gets content (a collection(table) and at least on document(record))
- Program when ran will set database and collection, if it has been created it would be used as a reference  
- Once species has been found in camera it will be logged and stored in the collection
- Go to DB.py found in the database directory to make changes as you see fit
- To modify what is logged look at user_motion_code.py
## Google Cloud Vision API
Follow these [Cloud Vision API](https://cloud.google.com/vision/docs/before-you-begin) instructions to create a new project, enable the API and set up authentication

Once your project is created and the API is enabled, you should have clicked the link to Create service account key.

"Click Create and you’ll be prompted to download a JSON file. You need this as it contains your service account key to allow you to make calls to the API locally" ([source](https://magpi.raspberrypi.org/articles/wildlife-camera-object-recognition)). Rename the file to `TweetyBird.json` and move the JSON file into your `~/pi-timolo` folder.

Install Google Cloud Vision dependencies:

```sudo pip install google-cloud-vision && sudo pip install google-cloud-storage```

## Run It
At this point you can run the project using `./pi-timolo.py`
To change the animal tweeted,  "change the line `if "bird" in tweetText: animalInPic = true`"([source](https://magpi.raspberrypi.org/articles/wildlife-camera-object-recognition)).

