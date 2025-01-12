#!/usr/bin/env python
# coding: utf-8

# # Chrome Driver Auto Install

# In[21]:


from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

# ChromeDriver의 서비스 객체 생성
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)
# driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())

URL = 'https://www.google.co.kr/imghp'
driver.get(url=URL)

driver.implicitly_wait(time_to_wait=10)


# # Search Image

# In[22]:


from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

# CSS 선택 ... 개발자 도구 내 Copy Selector로 추출
elem = driver.find_element(By.CSS_SELECTOR, 
            "body > div.L3eUgb > div.o3j99.ikrT4e.om7nvf > form > div:nth-child(1) > div.A8SBwf > div.RNNXgb > div.SDkEP > div.a4bIc > textArea")

elem.send_keys("바다")
elem.send_keys(Keys.RETURN) # Enter 키 입력하여 "바다" 검색


# # Find Images

# In[27]:


import time
elem = driver.find_element(By.TAG_NAME, "body")
for i in range(60):
    elem.send_keys(Keys.PAGE_DOWN)
    time.sleep(0.1)

try:
    for i in range(60):
        elem.send_keys(Keys.PAGE_DOWN)
        time.sleep(0.1)
except:
    pass


# # Counting Image

# In[28]:


links=[]

# 이미지가 공통적으로 지닌 class로 추출
images = driver.find_elements(By.CSS_SELECTOR,
    ".YQ4gaf")

for image in images:
    if image.get_attribute('src') is not None:
        links.append(image.get_attribute('src'))

print('image count : ', len(links))

