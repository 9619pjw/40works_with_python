from gtts import gTTS 
# gttts 라이브러리의 gTTS 기능만 불러와 사용함

text = "안녕하세요. 파이썬과 40개의 작품들 입니다."

tts = gTTS(text = text, lang ='ko')
# text변수의 문자열을 ko(한글)로 변환하여 tts에 저장
tts.save(r"3. 텍스트를 음성으로 변환\hi.mp3")
# 3. 텍스트를 음성으로 변환 폴더에 hi.mp3 이름의 파일로 저장함
# r을 붙여주어 특별한 명령어로 파이썬에서 해석하지 않고 역슬래쉬 자체로 해석함.