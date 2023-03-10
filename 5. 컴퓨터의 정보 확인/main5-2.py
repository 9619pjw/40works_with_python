import psutil

cpu = psutil.cpu_freq()
cpu_current_ghz = round(cpu.current / 1000, 2) # CPU 속도 출력
print(f"cpu 속도 : {cpu_current_ghz}GHz")

cpu_core = psutil.cpu_count(logical=False)  # CPU의 물리코어 수 출력
print(f"코어 : {cpu_core} 개")

memory = psutil.virtual_memory()        # 메모리의 총량
memory_total = round(memory.total / 1024 ** 3)
print(f"메모리 : {memory_total}GB" )

disk = psutil.disk_partitions()     # 디스크 크기를 출력
for p in disk:                      # 디스크 개수만큼
    print(p.mountpoint, p.fstype, end=' ')
    du = psutil.disk_usage(p.mountpoint)
    disk_total = round(du.total / 1024 ** 3)
    print(f"디스크 크기 : {disk_total}GB")

net = psutil.net_io_counters()      # 네트워크를 통해 보내고 받은 누적된 데이터를 MB 단위로 출력함
sent = round(net.bytes_sent/1024**2, 1)
recv = round(net.bytes_recv/1024**2, 1)
print(f'보내기 : {sent}MB   받기 : {recv}MB')