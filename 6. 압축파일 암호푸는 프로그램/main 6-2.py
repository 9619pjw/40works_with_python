# 비밀번호를 찾을 수 있으나 너무 빨라 출력값을 확인하기 힘듬

import itertools
import zipfile

passwd_string = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"

zFile = zipFile.ZipFile(r'6. 압축파일 암호푸는 프로그램\암호1234.zip')  # 비밀번호가 입력된 압축파일의 경로를 입력하여 불러옴

for len in range(1,6):
    to_attempt = itertools.product(passwd_string, repeat = len)
    for attempt in to_attempt:
        passwd = ''.join(attempt)
        print(passwd)
        try:    # 비밀번호 입력해서 맞으면 try, 틀리면 except를 실행
            zFile.extractall(pwd = passwd.encode()) # 비밀번호를 입력하여 맞으면 아랫줄 실행. 틀리면 except실행
            print(f"비밀번호는 {passwd} 입니다")
            break
        except:
            pass
    