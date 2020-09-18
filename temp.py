# -*- coding: utf-8 -*-
"""
Created on Thu Sep 15 21:53:19 2020

@author: noahr
"""

#import the urlretrieve library
from urllib.request import urlretrieve

URL_PATH = 'https://s3.amazonaws.com/tcmg476/http_access_log'
LOCAL_FILE = 'local_copy.log'

# Use urlretrieve() to fetch a remote copy and save into the local file path
local_file, headers = urlretrieve(URL_PATH, LOCAL_FILE)
#This retrieves the log data, input your file path to the log copy on your local machine.
#This part of the script counts the total requests in the log.
FILE_NAME = 'C:/Users/noahr/.spyder-py3/local_copy.log'
count = 0
for line in open(FILE_NAME):
    count = count + 1
print('The number of total requests is' ,count)
