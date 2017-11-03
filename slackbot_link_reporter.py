from slackclient import SlackClient
import os, sys, datetime
import csv

try:
    slack_token = os.environ['SLACK_API_TOKEN']
except:
    print("Could not find slack API token on this machine.")
    print("Aborting.")
    sys.exit()

sc = SlackClient(slack_token)

# Note the start time.

# Run check_links.sh

# Note the end time.

# Open the latest csv file

# Count the number of lines in the file.

# Post the file, number of lines in the file to slack.s

def get_data_from_file():
    with open("test.csv", "r") as f:
        file_data = csv.reader(f)
        data_out = ""
        for row in file_data:
            data_out = data_out + str(row) + "\n"

    return data_out

print get_data_from_file()


sc.api_call(
  "chat.postMessage",
  channel="#website-broken-links",
  text=get_data_from_file()
)
