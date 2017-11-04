from slackclient import SlackClient
import os, sys, datetime
import csv
import subprocess

write_debug_bool = True

filename_raw = "test.csv"
filename_out = "clean_test.csv"

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

# print data_out

# Note the end time.

# Count the number of lines in the file.

# Post the file, number of lines in the file to slack.s
