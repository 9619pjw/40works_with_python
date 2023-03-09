import qrcode

file_path = r'4. QR코드 생성기\qr코드모음.txt'
with open(file_path, 'rt', encoding='UTF-8') as f: # file_path 경로의 파일을 읽음
    read_lines = f.readlines() # 파일을 읽어 라인 별로 리스트의 값의 형태로 내어줌

    for line in read_lines: 
        line = line.strip() # line.strip()으로 마지막 줄바꿈 문자를 삭제함
        print(line) 