#소켓으로 외부사이트에 접속한 정보를 바탕으로 IP확인

import socket

in_addr = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # 소켓 연결함
in_addr.connect (("www.google.co.kr", 443)) # 구글에 접속, https 기본 접속포트는 443

print(in_addr.getsockname()[0])