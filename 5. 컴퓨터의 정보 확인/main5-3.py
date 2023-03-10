import psutil

curr_sent = 0
curr_recv = 0

prev_sent = 0
prev_recv = 0

while True:
    cpu_p = psutil.cpu_percent(interval = 1)    # CPU의 사용량에서 1초동안의 평균값을 구함
    print(f"CPU 사용량: {cpu_p}%")          # CPU 사용량 출력

    memory = psutil.virtual_memory()    # 사용 가능한 메모리를 출력
    memory_avail = round(memory.available/1024**3, 1)
    print(f'사용 가능한 메모리 : {memory_avail}GB')

    net = psutil.net_io_counters()      # 네트워크에서 보내고 받은 크기 출력
    curr_sent = net.bytes_sent/1024**2
    curr_recv = net.bytes_recv/1024**2

    sent = round(curr_sent - prev_sent, 1)  # 현재 측정값 - 이전 측정값 = 1초동안 보내는 데이터
    recv = round(curr_recv - prev_recv, 1)  # 현재 측정값 - 이전 측정값 = 1초동안 받은 데이터

    print(f'보내기 : {sent}MB 받기: {recv}MB')

    prev_sent = curr_sent   # 이전 값에 현재 값을 적용해줌
    prev_recv = curr_recv 