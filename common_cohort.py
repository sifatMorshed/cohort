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

yesterday = date.today() - timedelta(days = 1)
last_month = yesterday.replace(day=15) - timedelta(days = 30)
last_month_minus_1 = last_month.replace(day=15) - timedelta(days = 30)
last_month_minus_2 = last_month_minus_1.replace(day=15) - timedelta(days = 30)
start_of_this_month = yesterday.replace(day=1)

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


allfiles = os.listdir("C:\\wamp\\www\\laravel\\fcmTopicSubscription\\python\\multi_comp\\")


# for i in range(len(allfiles)):

i=0

file_pd0 = pd.read_csv(file_directory + allfiles[i], names=['msisdn'])
file_pd1 = pd.read_csv(file_directory + allfiles[i+1], names=['msisdn'])
file_pd2 = pd.read_csv(file_directory + allfiles[i+2], names=['msisdn'])
file_pd3 = pd.read_csv(file_directory + allfiles[i+3], names=['msisdn'])
file_pd4 = pd.read_csv(file_directory + allfiles[i+4], names=['msisdn'])
file_pd5 = pd.read_csv(file_directory + allfiles[i+5], names=['msisdn'])
file_pd6 = pd.read_csv(file_directory + allfiles[i+6], names=['msisdn'])
file_pd7 = pd.read_csv(file_directory + allfiles[i+7], names=['msisdn'])
file_pd8 = pd.read_csv(file_directory + allfiles[i+8], names=['msisdn'])
file_pd9 = pd.read_csv(file_directory + allfiles[i+9], names=['msisdn'])
file_pd10 = pd.read_csv(file_directory + allfiles[i+10], names=['msisdn'])
file_pd11 = pd.read_csv(file_directory + allfiles[i+11], names=['msisdn'])
file_pd12 = pd.read_csv(file_directory + allfiles[i+12], names=['msisdn'])
file_pd13 = pd.read_csv(file_directory + allfiles[i+13], names=['msisdn'])
file_pd14 = pd.read_csv(file_directory + allfiles[i+14], names=['msisdn'])
file_pd15 = pd.read_csv(file_directory + allfiles[i+15], names=['msisdn'])
file_pd16 = pd.read_csv(file_directory + allfiles[i+16], names=['msisdn'])
file_pd17 = pd.read_csv(file_directory + allfiles[i+17], names=['msisdn'])
file_pd18 = pd.read_csv(file_directory + allfiles[i+18], names=['msisdn'])
file_pd19 = pd.read_csv(file_directory + allfiles[i+19], names=['msisdn'])
file_pd20 = pd.read_csv(file_directory + allfiles[i+20], names=['msisdn'])
file_pd21 = pd.read_csv(file_directory + allfiles[i+21], names=['msisdn'])
file_pd22 = pd.read_csv(file_directory + allfiles[i+22], names=['msisdn'])
file_pd23 = pd.read_csv(file_directory + allfiles[i+23], names=['msisdn'])
file_pd24 = pd.read_csv(file_directory + allfiles[i+24], names=['msisdn'])
file_pd25 = pd.read_csv(file_directory + allfiles[i+25], names=['msisdn'])
file_pd26 = pd.read_csv(file_directory + allfiles[i+26], names=['msisdn'])
file_pd27 = pd.read_csv(file_directory + allfiles[i+27], names=['msisdn'])
file_pd28 = pd.read_csv(file_directory + allfiles[i+28], names=['msisdn'])
file_pd29 = pd.read_csv(file_directory + allfiles[i+29], names=['msisdn'])
file_pd30 = pd.read_csv(file_directory + allfiles[i+30], names=['msisdn'])
file_pd31 = pd.read_csv(file_directory + allfiles[i+31], names=['msisdn'])

output0= pd.DataFrame(compare_two_files(file_pd0, file_pd1,'both_file_common'), columns=['msisdn'])
output1= pd.DataFrame(compare_two_files(output0, file_pd2,'both_file_common'), columns=['msisdn'])
output2= pd.DataFrame(compare_two_files(output1, file_pd3,'both_file_common'), columns=['msisdn'])
output3= pd.DataFrame(compare_two_files(output2, file_pd4,'both_file_common'), columns=['msisdn'])
output4= pd.DataFrame(compare_two_files(output3, file_pd5,'both_file_common'), columns=['msisdn'])
output5= pd.DataFrame(compare_two_files(output4, file_pd6,'both_file_common'), columns=['msisdn'])
output6= pd.DataFrame(compare_two_files(output5, file_pd7,'both_file_common'), columns=['msisdn'])
output7= pd.DataFrame(compare_two_files(output6, file_pd8,'both_file_common'), columns=['msisdn'])
output8= pd.DataFrame(compare_two_files(output7, file_pd9,'both_file_common'), columns=['msisdn'])
output9= pd.DataFrame(compare_two_files(output8, file_pd10,'both_file_common'), columns=['msisdn'])
output10= pd.DataFrame(compare_two_files(output9, file_pd11,'both_file_common'), columns=['msisdn'])
output11= pd.DataFrame(compare_two_files(output10, file_pd12,'both_file_common'), columns=['msisdn'])
output12= pd.DataFrame(compare_two_files(output11, file_pd13,'both_file_common'), columns=['msisdn'])
output13= pd.DataFrame(compare_two_files(output12, file_pd14,'both_file_common'), columns=['msisdn'])
output14= pd.DataFrame(compare_two_files(output13, file_pd15,'both_file_common'), columns=['msisdn'])
output15= pd.DataFrame(compare_two_files(output14, file_pd16,'both_file_common'), columns=['msisdn'])
output16= pd.DataFrame(compare_two_files(output15, file_pd17,'both_file_common'), columns=['msisdn'])
output17= pd.DataFrame(compare_two_files(output16, file_pd18,'both_file_common'), columns=['msisdn'])
output18= pd.DataFrame(compare_two_files(output17, file_pd19,'both_file_common'), columns=['msisdn'])
output19= pd.DataFrame(compare_two_files(output18, file_pd20,'both_file_common'), columns=['msisdn'])
output20= pd.DataFrame(compare_two_files(output19, file_pd21,'both_file_common'), columns=['msisdn'])
output21= pd.DataFrame(compare_two_files(output20, file_pd22,'both_file_common'), columns=['msisdn'])
output22= pd.DataFrame(compare_two_files(output21, file_pd23,'both_file_common'), columns=['msisdn'])
output23= pd.DataFrame(compare_two_files(output22, file_pd24,'both_file_common'), columns=['msisdn'])
output24= pd.DataFrame(compare_two_files(output23, file_pd25,'both_file_common'), columns=['msisdn'])
output25= pd.DataFrame(compare_two_files(output24, file_pd26,'both_file_common'), columns=['msisdn'])
output26= pd.DataFrame(compare_two_files(output25, file_pd27,'both_file_common'), columns=['msisdn'])
output27= pd.DataFrame(compare_two_files(output26, file_pd28,'both_file_common'), columns=['msisdn'])
output28= pd.DataFrame(compare_two_files(output27, file_pd29,'both_file_common'), columns=['msisdn'])
output29= pd.DataFrame(compare_two_files(output28, file_pd30,'both_file_common'), columns=['msisdn'])
output30= pd.DataFrame(compare_two_files(output29, file_pd31,'both_file_common'), columns=['msisdn'])
Y = [len(output0), len(output1), len(output2), len(output3), len(output4), len(output5), len(output6), len(output7), len(output8), len(output9), len(output10), len(output11),
        len(output12), len(output13), len(output14), len(output15), len(output16), len(output17), len(output18), len(output19), len(output20), len(output21), len(output22), len(output23),
        len(output24), len(output25),len(output26),len(output27),len(output28),len(output29),len(output30)]

print(Y)
    
with open ("C:\\wamp\\www\\laravel\\fcmTopicSubscription\\python\\multi_comp\\result1.csv", "a", newline='') as f:    
            writer = csv.writer (f)
            writer.writerows ([Y])

