#!/usr/bin/python
import time, datetime, os
from os import path

today = datetime.date.today()
todaystr = today.isoformat()
if os.path.exists(todaystr) == True:
	print('directory exists')
else:
	os.mkdir(todaystr)
	print('directory created')

