# TweetyBird
Captures pictures of animals and uses AI to detect species. Uploads a capture of the animal and logs data about the animals appearance

We followed [this guide](https://magpi.raspberrypi.org/articles/wildlife-camera-object-recognition) to help in knowing which libraries might be best for this project and how to go about it. 

# Dependencies Required:
## pi-timolo
### Instructions:
Plug in a camera to the Raspberry Pi.
The link for the one used in this project is [here](https://www.amazon.com/gp/product/B07JPLV5K1/).

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

"Check the pictures by waving your hand in front of the camera, then looking in Pi-timolo > Media Recent > Motion. You may need to change the image size and orientation of the camera; in the Terminal window, enter nano config.py and edit these variables: imageWidth, imageHeight, and imageRotation" [(source).](https://magpi.raspberrypi.org/articles/wildlife-camera-object-recognition)

### Setting up Tweepy 
Set up a Twitter account or use an existing one.
Install Tweepy:
 
 ```sudo pip install tweepy```
Go [here](https://developer.twitter.com/apps) to create a new Twitter app
- Click Create an app (you may have to apply for a developer account and this may take some time).
- Once your account is approved as a developer account, click on "Keys and Access Tokens".
- You will need these keys and tokens for the next step

#### Inside of the ~/pi-timolo directory:
- Replace the pi-timolo.py file with the one in this repository
- Replace the user_motion_code.py with the one in this repository
- Edit the following user_motion_code.py variable values of 'XXX' with your keys and tokens you setup on Twitter 
```
    consumer_key = ‘XXX’
    consumer_secret = ‘XXX’
    access_token = ‘XXX’
    access_token_secret = ‘XXX’
```

## Google Cloud Vision API
Follow these [Cloud Vision API](https://cloud.google.com/vision/docs/before-you-begin) instructions to create a new project, enable the API and set up authentication

Once your project is created and the API is enabled, you should have clicked the link to Crease service account key.

"Click Create and you’ll be prompted to download a JSON file. You need this as it contains your service account key to allow you to make calls to the API locally. Rename and move the JSON file into your `~/pi-timolo` folder and make a note of the file path. Next, go back to pi-timolo.py and add the line: 

```os.environ["GOOGLEAPPLICATIONCREDENTIALS"] ="pathtoyour.jsoncredential_file"```

below `import os` to reference the credentials in your JSON file" ([source](https://magpi.raspberrypi.org/articles/wildlife-camera-object-recognition)).
