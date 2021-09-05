# Junior Hacking Talents Writeup
## Quay ngược thời gian
Memory dump: [mem.mem](https://drive.google.com/file/d/1G2Ndl58ypp_Uz8Zq1nBXVkh3qyDEcHIo/view?usp=sharing)

Mục tiêu: Xác định user, host, key_rsa/passowrd để truy cập ssh.

Lần này mình sẽ không sử dụng volatility, thay vào đó mình sẽ dùng ... strings và grep :3 

Dump hết string về 1 file cho dễ thao tác:

**$ strings mem.mem > strings.out**

Tìm từ những dòng liên quan đến shh

**$ cat strings.out | grep ssh**



