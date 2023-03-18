import itertools

passwd_string ="0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"

for len in range(1, 4):
    to_attempt = itertools.product(passwd_string, repeat = len) # passwd_string 모든 문자열을 repeat = 길이로 정렬하여 반환함
    for attempt in to_attempt:      # 정렬하여 반환된 문자의 수만큼 반복
        passwd = ''.join(attempt)   # 리스트로 반환된 값(''.join(리스트))을 문자열로 변환함
        print(passwd)