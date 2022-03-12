f=open("str2.txt","r")
data=f.readlines()
data=[i.rstrip().split() for i in data[:len(data)-1]]
str2=[]
for i in range(len(data)):
		t=data[i][3][:2]
		#if not(t=="00" or t=="0" or t=="FF"):
		#	print(f"{t}->{chr(int(t,16))}")
		print(t)
		str2+=[t]
str2="\\x".join(str2)
print(str2)
