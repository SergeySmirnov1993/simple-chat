import socket
import threading


def read_sok():
    while 1:
        data = sor.recv(1024)
        print(data.decode('utf-8'))

server = '192.168.100.106', 11719  # Данные сервера
alias = input('Введите псевдоним: ')     # Вводим наш псевдоним
sor = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sor.bind(('', 0))   # Задаем сокет как клиент
sor.sendto((alias+' Connect to server').encode('utf-8'), server)    # Уведомляем сервер о подключении
potok = threading.Thread(target=read_sok)
potok.start()


while 1:
    mensahe = input('message: ')
    sor.sendto(('['+alias+']'+mensahe).encode('utf-8'), server)