f=open("str1.txt","r")
data=f.readlines()
data=[i.rstrip().split() for i in data[:len(data)-1]]
for i in range(len(data)):
	if not i%8:
		t=data[i][3][:2]
		print(f"{i} :{t}")
str1=[data[i][3][:2] for i in range(len(data))]
str1="\\x".join(str1)
print(str1)
