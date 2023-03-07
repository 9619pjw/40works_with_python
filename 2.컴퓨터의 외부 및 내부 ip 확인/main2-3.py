import requests # 사이트 접속을 위한 requests 모듈
import re       # IP주소를 찾기 위한 정규식 사용위해 re 모듈

req = requests.get("http://ipconfig.kr") # 해당 사이트에 접속

out_addr = re.search(r'IP Address : (\d{1,3}\. \d{1,3}\. \d{1,3}\. \d{1,3})', req.text)[1]
# 정규식 표현을 사용하여 IP주소를 가져와 out_addr 변수와 바인딩함
print(out_addr) # 외부 IP주소 출력