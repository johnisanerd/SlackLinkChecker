from slackclient import SlackClient
import os, sys, datetime
import csv
import subprocess
from time import sleep
import time


import fileinput

write_debug_bool = True

filename_raw = "test.csv"
filename_out = "clean_test.csv"

'''
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


seen = set() # set for fast O(1) amortized lookup
for line in fileinput.FileInput(filename_out, inplace=1):
    if line in seen: continue # skip duplicate

    seen.add(line)
    print line, # standard output is now redirected to the file
'''

# Note the start time.
time_start = time.time()
print("Time in seconds since the epoch: %s" %time.time())

# Note the start time.
end_time = time.time()
print("Time in seconds since the epoch: %s" %time.time())

total_time = end_time - time_start
total_time = 80000
hours = total_time // (60*60)
print("Total crawl time (h) was: %s" %hours)
