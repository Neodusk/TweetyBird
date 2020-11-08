# TweetyBird
Captures pictures of animals and uses AI to detect species. Uploads a capture of the animal and logs data about the animals appearance

We followed [this guide](https://magpi.raspberrypi.org/articles/wildlife-camera-object-recognition) to help in knowing which libraries might be best for this project.

# Dependencies Required:
## pi-timolo
### Instructions:
Plug in a camera to the Raspberry Pi.
The link for the one used in this project is [here](https://www.amazon.com/gp/product/B07JPLV5K1/)
```
wget https://raw.github.com/pageauc/pi-timolo/master/source/pi-timolo-install.sh
chmod +x pi-timolo-install.sh
./pi-timolo-install.sh
```
This may take some time.
Once that is complete, run `sudo raspi-config Interfacing Options` and enable I2C and Pi Camera.

It is recommended to run ```sudo apt-get update && sudo apt-get dist-upgrade```
and then restart with ```sudo reboot```
