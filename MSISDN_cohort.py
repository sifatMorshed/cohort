import pandas as pd
import numpy as np
from os import path
from pathlib import Path
import pathlib
import sys
import os
from datetime import date 
from datetime import timedelta
import datetime
import csv
from dateutil import parser

# yesterday = date.today() - timedelta(days = 1)
# last_month = yesterday.replace(day=15) - timedelta(days = 30)
# last_month_minus_1 = last_month.replace(day=15) - timedelta(days = 30)
# last_month_minus_2 = last_month_minus_1.replace(day=15) - timedelta(days = 30)
# start_of_this_month = yesterday.replace(day=1)

def compare_two_files(data_file_1, data_file_2, type):
	diff=pd.merge(data_file_1, data_file_2, left_on='msisdn', right_on='msisdn', indicator=True, how='outer')
	if type == 'file1_uniq':
		data=diff[diff['_merge']=='left_only']['msisdn']
	elif type == 'file2_uniq':
		data=diff[diff['_merge']=='right_only']['msisdn']
	elif type == 'both_file_common':
		data=diff[diff['_merge']=='both']['msisdn']
	return data

file_directory = "C:\\wamp\\www\\laravel\\fcmTopicSubscription\\python\\multi_comp\\"
# date_entry = input('Enter a date in YYYY,MM,DD format')
# year, month, day = map(int, date_entry.split(','))
# date = date(year, month, day) - timedelta(days=1)
# date += datetime.timedelta(days=1)

allfiles = os.listdir("C:\\wamp\\www\\laravel\\fcmTopicSubscription\\python\\multi_comp\\")

with open ("C:\\wamp\\www\\laravel\\fcmTopicSubscription\\python\\multi_comp\\output.csv", "a", newline='') as f:
            writer = csv.DictWriter(f, fieldnames=['file1','file2','in_common'])
            writer.writeheader()


for i in range(len(allfiles)):
    if i >= len(allfiles):break
    file_pd = pd.read_csv(file_directory + allfiles[0], names=['msisdn'])

    if i>0:
         allfiles.pop(0)
         
    for i in range(len(allfiles)):
        if i == len(allfiles)-1:break
        file_pd_new = pd.read_csv(file_directory + allfiles[i+1], names=['msisdn'])
        compared_pd= pd.DataFrame(compare_two_files(file_pd, file_pd_new,'both_file_common'), columns=['msisdn'])
        Recursive_list = [allfiles[0],allfiles[i+1],len(compared_pd)]
        print(Recursive_list)
        
        with open ("C:\\wamp\\www\\laravel\\fcmTopicSubscription\\python\\multi_comp\\output.csv", "a", newline='') as f:    
            writer = csv.writer (f)
            writer.writerows ([Recursive_list])
