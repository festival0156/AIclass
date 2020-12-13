import socket
from io import BytesIO
from PIL import Image
import pygame

con2 = '', 5557

def recvall(conn, length):
    buf = b''
    while len(buf) < length:
        data = conn.recv(length - len(buf))
        if not data:
            return data
        buf += data
    return buf

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
    sock.bind(con2)
    sock.listen(5)
    print('Server started @ ' + str(con2[0]) + ':' + str(con2[1]))
    sock, addr = sock.accept()
    print('Client connected IP:', addr)

    size = int.from_bytes(sock.recv(2), 'big'), int.from_bytes(sock.recv(2), 'big')
    pygame.init()
    screen = pygame.display.set_mode(size)
    clock = pygame.time.Clock()
    watching = True

    while watching:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                watching = False
                break

        sock.sendall(b'\xff')
        leng = int.from_bytes(sock.recv(3), byteorder='big')
        bs = recvall(sock, leng)
        bs = BytesIO(bs)
        img = Image.open(bs)
        img = pygame.image.fromstring(img.tobytes(), img.size, img.mode)

        screen.blit(img, (0, 0))
        pygame.display.flip()
        clock.tick(60)
