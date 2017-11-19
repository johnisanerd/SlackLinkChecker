from slackclient import SlackClient
import os, sys, datetime, time
import csv
import subprocess
import fileinput

write_debug_bool = True

filename_raw = "test.csv"
filename_out = "clean_test.csv"

try:
    slack_token = os.environ['SLACK_API_TOKEN']
    sc = SlackClient(slack_token)
except:
    print("Could not find slack API token on this machine.")
    print("Aborting.")
    sys.exit()

def write_debug(in_string):
    if(write_debug_bool):
        print("DEBUG: " + str(in_string))

def send_bash_command(bashCommand):
    write_debug(bashCommand)
    process = subprocess.Popen(bashCommand.split(), stdout=subprocess.PIPE) #, stderr=subprocess.PIPE)
    output = process.communicate()[0]
    return output

# Note the start time.
time_start = time.time()
print("Time in seconds since the epoch: %s" %time.time())

# Run check_links.sh
command = "bash /home/john/SlackLinkChecker/check_links.sh"
send_bash_command(command)

# Filter for things we don't want to show up.
# Return True if we find something we don't want
# Return False if we find somethign we DO want
def filter_test(string_in):
    # Things we don't want to see!
    filters = ["mailto", "add-to-cart", "SSLError"]
    for test in filters:
        if string_in.find(test) > 0:
            return True
    else:
            return False

# Clear out things you don't want.  Like mailto links
with open(filename_raw, "r") as f:
    data_in = f.read()
    data_in = data_in.split("\n")
    data_in = list(filter(None, data_in))
    data_out = []
    for row in data_in:
        if not filter_test(row):
            data_out.append(row)

with open(filename_out, "w") as f:
    for each in data_out:
        f.write(str(each)+"\n")

# Clean out all the duplicates.
seen = set() # set for fast O(1) amortized lookup
for line in fileinput.FileInput(filename_out, inplace=1):
    if line in seen: continue # skip duplicate

    seen.add(line)
    print line, # standard output is now redirected to the file

# Note the start time.
end_time = time.time()
print("Time in seconds since the epoch: %s" %time.time())

total_time = end_time - time_start
total_time = total_time // (60*60)
print("Total crawl time (h) was: %s" %total_time)

# Count the number of lines in the file.

# Post the file, number of lines in the file to slack.s

# Upload a file
command = "curl -F file=@" + filename_out + " -F title='Hello!' -F content='Hello' -F channels=#website-broken-links -F token=" + slack_token +" https://slack.com/api/files.upload"
send_bash_command(command)

text_for_chat = "Total time to run crawl in hours: " + str(total_time)

sc.api_call(
  "chat.postMessage",
  channel="#website-broken-links",
  text=text_for_chat
)
