import socket
from io import BytesIO
from PIL import Image
from mss import mss

con2 = '192.168.43.161', 16247
resizeRatio = 2

def retreive_screenshot(conn):
    with mss() as sct:
        mon = sct.monitors[0]
        img = sct.grab(mon)
        size = round(img.width/resizeRatio), round(img.height/resizeRatio)
        [conn.sendall(i.to_bytes(2, 'big')) for i in size]
        while True:
            conn.recv(1)
            img = sct.grab(mon) # get screenshot
            img = Image.frombytes('RGB', img.size, img.bgra, 'raw', 'BGRX') # to PIL.Image
            img = img.resize(size) # reducing size
            bs = BytesIO()
            img.save(bs, format='jpeg')
            bs = bs.getbuffer().tobytes()
            conn.sendall(len(bs).to_bytes(length=3, byteorder='big'))
            conn.sendall(bs)

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
    sock.connect(con2)
    retreive_screenshot(sock)
