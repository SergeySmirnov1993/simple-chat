import socket


def create_server():
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)     # позволяет нескольким приложениям «слушать» сокет
    sock.bind(('0.0.0.0', 11719))      # прослушиваются все интерфейсы (аналогично '')
    return sock
