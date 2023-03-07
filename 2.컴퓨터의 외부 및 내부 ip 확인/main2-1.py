#컴퓨터의 내부 IP 출력

import socket
in_addr = socket.gethostbyname(socket.gethostname())
# 연결된 소켓의 이름을 가져와 in_addr 변수와 바인딩함
print(in_addr)