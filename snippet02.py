#! /usr/bin/env python
"""
This is another practice snippet
"""

__author__ = "O.A"
__author_email__ = "oa@live.com"

from datetime import datetime

log_file = "snippet02.log"

def read_log(log):
   """
    Open the log file in the working directory and print on the terminal
   """
   with open(log, "r") as f:
        print(f.read())
def write_log(log, name):
    """
    Add new logfile enrty with datestamp
    """
    #Get current date and time
    log_time = str(datetime.now())
    with open(log, "a") as f:
        f.writelines("Entry logged at: {} by {}\n".format(log_time, name))

#Program entry point
if __name__ == '__main__':
    # Get users name
    name = input("What is your name? ")
    #Add entry to the log file
    print("Adding new log entry")
    write_log(log_file, name)
    print("")

    #Access Starting Log File
    print("Log File Contents")
    print("-----------------")
    read_log(log_file)

