import qrcode

qr_data = 'www.naver.com' # qr_data 변수에 링크 삽입
qr_img = qrcode.make(qr_data) # qrcode.make로 qr코드 이미지 생성

save_path = '4. QR코드 생성기\\' + qr_data + '.png' # save_path로 저장할 경로 지정. 이름은 "{qr_data}.png"
qr_img.save(save_path) # 이미지를 저장함