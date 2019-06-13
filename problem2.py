#!/usr/bin/python3

import os
import time
from googlesearch import search
web=input("enter topic t search ------->>>>" )
url=[]
for i in search(web,stop=10):
	time.sleep(1)
	url.append(i)
	print(i)
print(url)
