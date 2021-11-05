import socket
s=socket.socket()
s.connect(("programming.letspentest.org", 8111))
def sum(arr):
    sum=0
    for i in arr:
       try:
           int(i)
       except:
           continue
       else:
           sum+=int(i)
    return str(sum)
while True:
    print(s.recv(1024).decode())
    num_list=s.recv(1024).decode()
    print(num_list)
    num_list=num_list.split(' ')
    print(sum(num_list[0:len(num_list)-7]))
    s.send(sum(num_list[0:len(num_list)-7]).encode()+b'\n')
