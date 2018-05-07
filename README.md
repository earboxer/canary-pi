
# Setup

## Server


Install dependencies

```sh
brew install mosquitto
brew services start mosquitto
brew install waon
sudo easy_install pip
sudo pip install paho-mqtt
sudo pip install git+https://github.com/vishnubob/python-midi
```

Create user account for pis

```sh
# From https://superuser.com/a/1156225
sudo dscl . -create /Users/pi
sudo dscl . -create /Users/pi UserShell /bin/bash
sudo dscl . -create /Users/pi RealName "Raspberry Pi"
sudo dscl . -create /Users/pi UniqueID "1234"
sudo dscl . -create /Users/pi PrimaryGroupID 52
sudo dscl . -create /Users/pi NFSHomeDirectory /Users/pi
sudo mkdir /Users/pi
sudo chown pi /Users/pi
```

Set the password to something secure

```sh
sudo passwd pi
```

Go to system preferences, sharing, enable remote login, allow access for All Users.

To run the server:

```sh
python primary.py pi1 pi2
```

## Client

```sh
sudo pip install paho-mqtt
```

As the user who will be running the script, do

```sh
ssh-keygen
ssh-copy-id pi@serveraddress
```

to run

```sh
python client.py pi1 serveraddress
```
