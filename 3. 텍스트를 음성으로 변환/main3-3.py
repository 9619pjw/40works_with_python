from gtts import gTTS
from playsound import playsound
import os

# 경로를 .py 파일의 실행경로로 이동, 현재 경로로 이동
os.chdir(os.path.dirname(os.path.abspath(__file__)))

file_path = '나의텍스트.txt' # '나의텍스트.txt' 경로로 변경

with open(file_path, 'rt', encoding= 'UTF8') as f:  # 파일을 f의 이름으로 오픈함. with는 파일열고 종료되면 자동으로 파일을 닫음
    #한글로 작성된 파일을 열기 때문에 'rt', encoding='UTF8' 형식으로 열어 글자가 안깨지게 함 
    read_file = f.read()    # 파일 전체 내용을 읽어 read_file에 저장

tts = gTTS(text=read_file, lang='ko') # text변수의 문자열을 ko(한글)로 변환하여 tts에 저장

tts.save("myText.mp3")
# myText.mp3 이름의 파일로 저장함
playsound("myText.mp3")
# 파일 재생함