
import base64,struct,string
from Crypto.Cipher import AES
iv_part2=''
algorithm = AES.MODE_CBC
key = 'supersecretkey!?'
iv_part1 = "0xcafedeadbeef"
iv_part2='x0'
iv=iv_part1+iv_part2
f=open("cipher.txt","rb")
encoded_flag=f.read()
print("iv: ",iv)
decoded_flag=AES.new(key, algorithm, iv).decrypt(encoded_flag).decode().rstrip()
print("Len: ",len(decoded_flag))
print(decoded_flag)
print("---------------------------------")