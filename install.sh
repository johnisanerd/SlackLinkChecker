#!/bin/sh

# LinkChecker comes as a debian package for Stretch and Jessie.

sudo apt-get update
sudo apt-get install linkchecker

# Install Slack
sudo pip install slackclient
sudo pip install Flask      # Says we need it to do OAuth (http://slackapi.github.io/python-slackclient/auth.html)
