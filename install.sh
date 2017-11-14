#!/bin/sh

# LinkChecker comes as a debian package for Stretch and Jessie.

sudo apt-get update
sudo apt-get install linkchecker

# Install Slack
sudo pip install slackclient
sudo apt-get install python-pip python-dev build-essential
sudo pip install --upgrade pip
