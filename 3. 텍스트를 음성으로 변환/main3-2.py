from gtts import gTTS
from playsound import playsound     # playsound 모듈로부터 playsound를 불러와 사용함
import os                           # 경로 이동을 위해 os 라이브러리를 불러옴

# 경로를 .py파일의 실행경로로 이동
os.chdir(os.path.dirname(os.path.abspath(__file__))) 
# playsound에서 한글을 인식하지 못하여 경로를 이동

text = "안녕하세요. 파이썬과 40개의 작품들 입니다."

tts = gTTS(text = text, lang ='ko')
tts.save("hi.mp3")

playsound("hi.mp3")