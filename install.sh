#!/bin/sh

# LinkChecker comes as a debian package for Stretch and Jessie.

sudo apt-get update
sudo apt-get install linkchecker -y
sudo apt-get install curl -y

# Install Slack
sudo apt-get install python-pip python-dev build-essential -y
sudo pip install --upgrade pip
sudo pip install slackclient
