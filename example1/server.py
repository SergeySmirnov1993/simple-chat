import socket

# socket.AF_INET — для сокета используем IPv4 .
# socket.SOCK_DGRAM — тип сокета.
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Cвяжем сокет с адресом(интерфейсом) и портом
# Пустые кавычки значат что сокет слушает все доступные интерфейсы.
sock.bind(('0', 11719))
client = []     # Массив где храним адреса клиентов

print('Start Server')
while 1:
    data, addres = sock.recvfrom(1024)  # Вернет данные и адрес сокета с которого получены эти данные.
    print(addres[0], addres[1])
    if addres not in client:
        client.append(addres)   # Если такого клиента нету , то добавить
    for clients in client:
        if clients == addres:
            continue    # Не отправлять данные клиенту, который их прислал
        sock.sendto(data, clients)
