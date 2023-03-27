import requests
from bs4 import BeautifulSoup

# 환율비를 가져오는 함수
def get_exchange_rate(target1, target2):
    headers = {  # 헤더를 추가하여 일반적인 브라우저를 이용하여 접속한것처럼 보이게 함
        'User-Agent' : 'Mozilla/5.0',
        'Content-Type' : 'text/html; charset=utf-8'
    }
    # requests 라이브러리를 이용하여 https://kr.investing.com/currencies/usd-krw에 접속하여 응답값을 가지고옴
    response = requests.get("https://kr.investing.com/currencies/{}-{}".format(target1, target2), headers=headers)
    content = BeautifulSoup(response.content, 'html.parser') # BeautifulSoup 라이브러리를 이용하여 html로 보기 값을 찾기 좋게 함
    containers = content.find('span', {'data-test' : 'instrument-price-last'}) # 마지막 환율 정보 찾음
    print(containers.txt)  # 환율정보 출력

get_exchange_rate('usd', 'krw') # get_exchange_rate 함수를 이용하여 1달러대 원화비율을 크롤링하여 출력